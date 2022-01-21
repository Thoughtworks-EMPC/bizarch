from neo4j import GraphDatabase
import json


class Neo4JClient(object):

    def __init__(self, host, user="neo4j", password="neo4j"):
        self._driver = GraphDatabase.driver("bolt://{}:7687".format(host), encrypted=False,
                                            max_transaction_retry_time=60)

    def clear(self):
        with self._driver.session() as session:
            session.write_transaction(self.__clear_nodes)

    def close(self):
        self._driver.close()

    def create_node(self, node_name, type, properties={}):
        with self._driver.session() as session:
            session.write_transaction(self.__create_node, node_name, type, properties)
            return node_name

    def update_node(self, node_name, properties={}):
        with self._driver.session() as session:
            session.write_transaction(self.__update_node, node_name, properties)
            return node_name

    def create_relationship(self, node1, node2, relation_name, properties={}):
        with self._driver.session() as session:
            return session.write_transaction(self.__create_update_relationship, node1, node2, relation_name, properties)

    def create_unique_relationship(self, node1, node2, relation_name="USE", properties={}):
        with self._driver.session() as session:
            session.write_transaction(self.__create_unique_relationship, node1, node2, relation_name, properties)

    def find_longest_path(self, label="Project"):
        with self._driver.session() as session:
            session.write_transaction(self.__find_longest_path, label)

    def merge_relationship(self):
        with self._driver.session() as session:
            session.write_transaction(self.__merge_relationship)

    def clear_by_label(self, label="Project"):
        with self._driver.session() as session:
            session.write_transaction(self.__clear, label)

    def create_graph(self, name, node, rel):
        with self._driver.session() as session:
            session.write_transaction(self.__create_graph, name, node,rel)

    def degree(self, name):
        with self._driver.session() as session:
            session.write_transaction(self.__degree_graph, name)

    def community(self, name):
        with self._driver.session() as session:
            return session.write_transaction(self.__community_graph, name)

    @staticmethod
    def __clear_nodes(tx):
        tx.run("MATCH (n) DETACH DELETE n")

    @staticmethod
    def __create_constrains(tx):
        tx.run("CREATE CONSTRAINT ON (service: Service) ASSERT project.name IS UNIQUE")

    @staticmethod
    def __create_node(tx, name, type, properties):
        try:
            merge_node = "MERGE (n:" + type + " {name: '" + name + "'})"
            update_props_cypher = "MATCH (n:" + type + " {name: '" + name + "'}) SET n += " + Neo4JClient.__properties_to_str(properties)

            tx.run(merge_node)
            tx.run(update_props_cypher)
            return name
        except Exception as ex:
            print(ex)
            pass

    @staticmethod
    def __update_node(tx, name, properties):
        # now only support update community property
        # MATCH (n { name:'交易策略'} ) SET n.community=3 return n
        properties["name"] = name
        k ,v = "community", str(properties["community"])
        try:
            query = "MATCH (n {name:'" + name + "'} ) SET n." + k + " = " + v + " return n"
            tx.run(query)
            return name
        except Exception as ex:
            print(ex)
            pass

    @staticmethod
    def __create_update_relationship(tx, node1, node2, relation_name='LINKS_TO', properties={}):
        Neo4JClient.__find_relationship(tx, node1, node2, relation_name, properties)
        query = "MATCH (a),(b) WHERE a.name = '" + node1 + "' AND b.name ='" + node2 + "' CREATE (a)-[r:" \
                + relation_name + " " + str(properties).replace('\'', '') + "]->(b)"
        tx.run(query)
        return relation_name

    @staticmethod
    def __find_relationship(tx, node1, node2, relation_name='LINKS_TO', properties={}):
        query = "MATCH p=()-[r:`" + relation_name + "`] -> () return p"
        rs = tx.run(query)
        for record in rs:
            record
        query = "MATCH p=()-[r:`" + relation_name + "`] -> () SET p.weight = 1 "
        return ""

    @staticmethod
    def __properties_to_str(properties):
        cql = []
        for k, v in properties.items():
            kv = ""
            kv = kv + k + ":"
            if type(v) == int:
                kv = kv + str(v)
            else:
                kv = kv + "\'" + v + "\'"
            cql.append(kv)
        cql = ','.join(cql)
        return "{" + cql + "}"

    @staticmethod
    def __create_unique_relationship(tx, node1, node2, relation_name, properties):

        query = "MATCH (a),(b) WHERE a.name = '" + node1 + "' AND b.name ='" + node2 + "' MERGE (a)-[r:" \
                + relation_name + " " + Neo4JClient.__properties_to_str(properties) + "]->(b)"
        tx.run(query)

    @staticmethod
    def __merge_relationship(tx):
        query = "MATCH (A)-[r]->(B) WITH  A,B, count(r) as relsCount MATCH (A)-[r]->(B) WHERE relsCount >= 1 " \
                "WITH A,B,collect(r) as rels CALL apoc.refactor.mergeRelationships(rels,{properties:'combine'}) " \
                "YIELD rel RETURN rel"
        tx.run(query)

    @staticmethod
    def __create_graph(tx,name,node,rel):
        result = tx.run("CALL gds.graph.exists('" + name + "')")
        for i in result:
            if i.get("exists"):
                print("drop existing graph {}".format(name))
                cmd = "CALL gds.graph.drop('" + name + "')"
                tx.run(cmd)
        cmd = "CALL gds.graph.create('{}','{}',{{{}: {{orientation: 'UNDIRECTED'}}}})".format(name,node,rel)
        tx.run(cmd)
            # self.injector.update_node(i["name"],{"community":i["communityId"]})

    @staticmethod
    def __community_graph(tx,name):
        ret = []
        cmd = "CALL gds.louvain.stream('" + name + "') YIELD nodeId, communityId, intermediateCommunityIds RETURN gds.util.asNode(nodeId).name AS name, communityId, intermediateCommunityIds ORDER BY name ASC"
        result = tx.run(cmd)
        for i in result:
            ret.append((i.get("name"),i.get("communityId")))
        return ret

    @staticmethod
    def __degree_graph(tx,name):
        ret = []
        cmd = "CALL gds.louvain.stream('" + name + "') YIELD nodeId, communityId, intermediateCommunityIds RETURN gds.util.asNode(nodeId).name AS name, communityId, intermediateCommunityIds ORDER BY name ASC"
        result = tx.run(cmd)
        for i in result:
            ret.append((i.get("name"),i.get("communityId")))
        return ret

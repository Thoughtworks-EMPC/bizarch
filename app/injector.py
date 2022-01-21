from app.repo_neo import Neo4JClient
from app.model import Journey,Operation,System
class Injector:
    def __init__(self,db_user = "repo", db_password = "", host = "localhost", database = "repo_fellow"):
        print("connect to neo4j {}".format(host))
        self.client = Neo4JClient(host = host)
        # self.client.clear()

    def create_node(self,name,type,properties):
        self.client.create_node(name,type,properties)

    def update_node(self,name,properties):
        self.client.update_node(name,properties)

    def create_edge(self,node1,node2,relation_name,properties):
        self.client.create_unique_relationship(node1,node2,relation_name,properties)

    def merge_relationship(self):
        self.client.merge_relationship()

    def clear(self):
        self.client.clear()
    # def add_role(self,role):
    #     self.client.create_node(system.name,"System")
    def graph(self,name,node,rel):
        self.client.create_graph(name,node,rel)
        return self.client.community(name)

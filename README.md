### Neo4J Env setup  
download plugins from github  
```
wget https://github.com/neo4j-contrib/neo4j-apoc-procedures/releases/download/4.0.0.17/apoc-4.0.0.17-all.jar
wget https://github.com/neo4j/graph-data-science/releases/download/1.3.1/neo4j-graph-data-science-1.3.1-standalone.jar
```
put the plugins into plugins folder, start the docker instance  
```
docker run -d -e NEO4J_dbms_security_procedures_unrestricted=apoc.\\\*,gds.\\\* -e NEO4J_AUTH=none -p 7474:7474 -v $PWD/data:/data:Z -v $PWD/plugins:/plugins -p 7687:7687 neo4j:4.0
```
open url to visit the graph
```
http://localhost:7474/browser/
```

### Setup  
```
pip3 install --no-cache-dir -r requirements.txt
```

### Write DFD and inject data  
1. create a DFD data, under data directory, create your dfd file and export the file in the __init__.py  
```
touch data/example.py
```

2. modify dfd content  
```
from app.dfd import DFD

def biz():
    dfd = DFD("Example")
    dfd.create_request("R","Operation").span("Sys1","Func1").span("Sys2","Func2",external=True)
    return dfd
```

3. run app to inject network data into neo4j db  
```
python3 -m app network example
python3 -m app graph example
```

### Query different view

1. Query all without roles

```
match(n) where not 'Role' in Labels(n) return n
```

CALL gds.graph.drop('myGraph')
CALL gds.graph.create(
    'myGraph',
    'Domain',
    {
        UseBy: {
            orientation: 'UNDIRECTED'
        }
    }
)

CALL gds.louvain.stream('myGraph')
YIELD nodeId, communityId, intermediateCommunityIds
RETURN gds.util.asNode(nodeId).name AS name, communityId, intermediateCommunityIds
ORDER BY name ASC

CALL gds.louvain.stream({
    nodeProjection: 'Node',
    relationshipProjection: {
        TYPE: {
            type: 'TYPE',
            orientation: 'undirected',
            aggregation: 'NONE'
        }
    },
    includeIntermediateCommunities: true
}) YIELD nodeId, communityId, intermediateCommunityIds
RETURN gds.util.asNode(nodeId).name AS name, communityId, intermediateCommunityIds
ORDER BY name ASC


test
### Generate a community  
```
CALL gds.louvain.stream({
    nodeProjection: 'System',
    relationshipProjection: {
        TYPE: {
            type: 'Use',
            orientation: 'undirected',
            aggregation: 'NONE'
        }
    },
    includeIntermediateCommunities: true
}) YIELD nodeId, communityId, intermediateCommunityIds
RETURN gds.util.asNode(nodeId).name AS name, communityId, intermediateCommunityIds
ORDER BY name ASC
```

### Caculte closeness  
```
CALL gds.alpha.closeness.stream({
  nodeProjection: 'System',
  relationshipProjection: 'Use'
})
YIELD nodeId, centrality
RETURN gds.util.asNode(nodeId).name AS system, centrality
ORDER BY centrality DESC
```
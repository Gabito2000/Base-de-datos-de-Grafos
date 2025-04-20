delete the old container:
```bash
    docker rm -f neo4j_container
    sudo rm -rf $HOME/neo4j/data
```

create dokerNeo4jConteiner:
```bash
    docker run -d \
    --publish=7474:7474 --publish=7687:7687 \
    --volume=$HOME/neo4j/data:/data \
    --volume=./data/courseProject2025.dump:/var/lib/neo4j/import/webdb.dump \
    --name neo4j_container \
    --env NEO4J_dbms_default__database=webdb \
    --env NEO4J_apoc_export_file_enabled=true \
    --env NEO4J_apoc_import_file_enabled=true \
    --env NEO4J_apoc_import_file_use__neo4j__config=true \
    --env NEO4JLABS_PLUGINS=\[\"apoc\",\"apoc-extended\"\,\"graph-data-science\"] \
    neo4j:community
```


import the dump:
```bash
    docker stop neo4j_container
    docker run --rm \
    -v $HOME/neo4j/data:/data \
    -v ./data/courseProject2025.dump:/var/lib/neo4j/import/webdb.dump \
    neo4j:community \
    neo4j-admin database load --from-path=/var/lib/neo4j/import/ webdb --overwrite-destination=true
    docker start neo4j_container
```
api Keys
```bash
c37e6364 
98e8c957
5e2dee8c 
198bb9d
dcaa75c2
392eb0a2 
3a173821 

a6244c18
4b29433d
```

MATCH (m1:Movie)
Match (m2:Movie)
WHERE m1.imdbRating IS NOT NULL AND m1.runtime IS NOT NULL AND m1.year IS NOT NULL AND m2.imdbRating IS NOT NULL AND m2.runtime IS NOT NULL AND m2.year IS NOT NULL AND m1 < m2
WITH m1, m2,
[toFloat(m1.imdbRating), toFloat(m1.runtime), toFloat(m1.year)] AS v1,
[toFloat(m2.imdbRating), toFloat(m2.runtime), toFloat(m2.year)] AS v2
WITH m1, m2,
vector.similarity.cosine(v1, v2) AS cosineSim,
vector.similarity.euclidean(v1, v2) AS pearsonSim
RETURN m1 AS node1, m2 AS node2, cosineSim, pearsonSim
ORDER BY cosineSim DESC
LIMIT 1000;
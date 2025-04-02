delete the old container:
```bash
    docker rm -f neo4j_container
```

create dokerNeo4jConteiner:
```bash
     docker run -d \
    --publish=7474:7474 --publish=7687:7687 \
    --volume=$HOME/neo4j/data:/data \
    --volume=./data/webdb.dump:/var/lib/neo4j/import/webdb.dump \
    --name neo4j_container \
    --env NEO4J_dbms_default__database=webdb \
    neo4j:community
```
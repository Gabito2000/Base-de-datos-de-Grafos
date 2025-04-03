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
    --volume=./data/webdb.db.dump:/var/lib/neo4j/import/webdb.dump \
    --name neo4j_container \
    --env NEO4J_dbms_default__database=webdb \
    --env NEO4J_apoc_export_file_enabled=true \
    --env NEO4J_apoc_import_file_enabled=true \
    --env NEO4J_apoc_import_file_use__neo4j__config=true \
    --env NEO4JLABS_PLUGINS=\[\"apoc\"\] \
    neo4j:community
```

move other files from host to container:
```bash
    docker cp ./data/minigraphweb.db.dump neo4j_container:/var/lib/neo4j/import/minigraphweb.dump
```

import the dump:
```bash
    docker stop neo4j_container
    docker run --rm \
    -v $HOME/neo4j/data:/data \
    -v ./data/webdb.db.dump:/var/lib/neo4j/import/webdb.dump \
    neo4j:community \
    neo4j-admin database load --from-path=/var/lib/neo4j/import/ webdb --overwrite-destination=true
    docker start neo4j_container
```

```bash
    docker stop neo4j_container
    docker run --rm \
    -v $HOME/neo4j/data:/data \
    -v ./data/minigraphweb.db.dump:/var/lib/neo4j/import/minigraphweb.dump \
    neo4j:community \
    neo4j-admin database load --from-path=/var/lib/neo4j/import/ minigraphweb --overwrite-destination=true 
    docker start neo4j_container
```

change the --env NEO4J_dbms_default__database= for the database you want to use.
```bash
    docker stop neo4j_container
    docker rm -f neo4j_container
    docker run -d \
    --publish=7474:7474 --publish=7687:7687 \
    --volume=$HOME/neo4j/data:/data \
    --volume=./data/minigraphweb.db.dump:/var/lib/neo4j/import/minigraphweb.dump \
    --name neo4j_container \
    --env NEO4J_dbms_default__database=minigraphweb \
    --env NEO4J_apoc_export_file_enabled=true \
    --env NEO4J_apoc_import_file_enabled=true \
    --env NEO4J_apoc_import_file_use__neo4j__config=true \
    --env NEO4JLABS_PLUGINS=\[\"apoc\"\] \
    neo4j:community
```

remember that in the comunity version you can't use multiple databases.

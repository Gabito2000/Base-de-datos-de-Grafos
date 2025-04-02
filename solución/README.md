# Neo4j Docker Setup

## Getting Started

0. Stop and delete any existing containers with the same name:
```bash
docker stop my-neo4j
docker rm my-neo4j
```

1. Build the Docker image:
```bash
docker build -t my-neo4j .

2. Run the Docker container:
```bash
docker run -d --name neo4j-db -p 7474:7474 -p 7687:7687 -v "c:/Users/gabri/OneDrive/Escritorio/Facultad/Base de datos de Grafos/solución/data:/data" my-neo4j
```

3. Update the database:
```bash
docker exec neo4j-db neo4j-admin database load webdb.db --from-path=/data --overwrite-destination=true
```

// ... existing setup steps ...

4. Verify the database is loaded:
   a. Access Neo4j Browser:
   - Open your web browser and navigate to: http://localhost:7474
   - Default credentials:
     - Username: neo4j
     - Password: password123
     (You'll be prompted to change the password on first login)

   b. Check available databases using Cypher:
   ```cypher
   SHOW DATABASES;

resume:
```bash
docker build -t my-neo4j .
docker run -d --name neo4j-db -p 7474:7474 -p 7687:7687 -v "c:/Users/gabri/OneDrive/Escritorio/Facultad/Base de datos de Grafos/solución/data:/data" my-neo4j
docker exec neo4j-db neo4j-admin database load webdb.db --from-path=/data --overwrite-destination=true
```
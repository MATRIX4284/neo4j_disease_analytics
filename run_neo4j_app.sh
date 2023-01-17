##Provide Permission on the local directory containing the csv to be loaded in neo4j:
sudo chmod -R 777 HOME/neo4j/import


##Run Neo4J with Graph Data Science and external csv for loading from Python:
docker run -d -it --rm   --publish=7474:7474 --publish=7687:7687   --user="$(id -u):$(id -g)" -v $HOME/neo4j/import:/var/lib/neo4j/import  -e NEO4J_AUTH=none   --env NEO4JLABS_PLUGINS='["apoc","graph-data-science"]'   neo4j:5.2.0


## Run Neo-Dash Docker:

docker run -d -it --rm -p 5005:5005 nielsdejong/neodash

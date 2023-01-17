from neo4j import GraphDatabase

driver=GraphDatabase.driver("bolt://localhost:7687",auth=("neo4j","neo4j"))

def add_disease_data(tx):
	tx.run("LOAD CSV WITH HEADERS FROM 'file:///disease.csv' AS row MERGE (n:disease {name: row.name, ko: row.ko, description: row.description, disease_category:row.disease_category})")
	tx.run("LOAD CSV WITH HEADERS FROM 'file:///drug.csv' AS row MERGE (n:drug {name: row.name, ko: row.ko})")
	tx.run("LOAD CSV WITH HEADERS FROM 'file:///pathogen.csv' AS row MERGE (n:pathogen {name: row.name, ko: row.ko, taxonomy: row.taxonomy})")
	tx.run("LOAD CSV WITH HEADERS FROM 'file:///drug_disease.csv' AS row MERGE (n1:drug {ko: row.from}) MERGE (n2:disease {ko: row.to}) MERGE (n1)-[r:treats]->(n2)")
	tx.run("LOAD CSV WITH HEADERS FROM 'file:///pathogen_disease.csv' AS row MERGE (n1:pathogen {ko: row.from}) MERGE (n2:disease {ko: row.to}) MERGE (n1)-[r:causes]->(n2)")

with driver.session() as session:
	session.write_transaction(add_disease_data)
	
driver.close()

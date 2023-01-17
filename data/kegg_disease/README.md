

# Introduction


1. The scripts are for data processing.

  

2. The data folder contains the five CSV to be imported into Neo4j.

  

  

# Prerequisite

Neo4j Desktop
  

# Run

The data folder contain data from 2021. If you want to download the newest data, do these:
  
1. Download the KEGG data with its API
```console
python download_various_kegg.py ds ./data
```
 
2. Generate nodes and edges
```console
python parse_disease.py ./data
```
3. Add taxonomy to pathogen. In step 2, a file called pathogen_tmp.csv is generated. We need to add the taxonomy to it via:

```console
python add_taxonomy.py pathogen_tmp.csv > pathogen.csv
```

4. Put all the CSV files, except pathogen_tmp.csv, into the Import folder of your Neo4j project. 

```console
cd ./data
cp *.csv ../../../import
```

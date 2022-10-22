# Preprocessing techniques of text data applied in the Brazilian Poverty Database

This GIT is the code of Automatic Spelling Correction project to correct wrongly typed neighborhood names of CECAD (https://cecad.cidadania.gov.br/painel03.php).

It is possible to find detailed information of this project on the Master Thesis "Preprocessing techniques of text data applied in the Brazilian Poverty Database" of Universidade NOVA IMS - Lisbon 

![Thesis_flowchart-Flowchart inicial](https://user-images.githubusercontent.com/71496553/197341385-f8a17d69-ce1f-4e0f-bd12-5988e69bd754.jpg)

The flowchart presents how this project was developed 

Code explaination:
- 1_filter_municipio.py: Code to filter the city of analysis 
- 2_reference_table.py: Code to create the dictionary table of the analysis' city
- 3_create_table_DLD.py: Code to compare the strings with Damerau-Levenshtein method
- damerau_levenshtein.py: code of Damerau-Levenshtein method
- 3_create_table_JD.py: Code to compare the string with Jaccard Distance method
- jaccard_distance.py: Code of Jaccard Distance method
- insert_SQLite_table.py: insert the data on the database for analysis
- create_SQLite_table.py: create the structure of table in the database 
- sqlite3.exe: library to use SQL database to data analysis

This project demands:
Python 3.10 (Libraries: pandas)
SQLite 3
IDE of preference (were developed in PyCharm Community Edition)

All doubts can be contact to: hnakashima.2022@gmail.com

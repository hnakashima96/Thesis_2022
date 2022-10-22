import pandas as pd
import sqlite3

#path for the SQL Database
con = sqlite3.connect(r'C:\Users\hirom\Documents\Tese\CODE\Data\project.db')
#general data base of neighborhoods
bairros_geral = pd.read_sql_query('SELECT * from bairros_202104', con)
print('Bairros_202104 updated')
#code of the city based on IBGE
geocodes = pd.read_sql_query('SELECT * from ids_ibge', con)
print('geocode updated')

con.close()

#function to filter the city from general database of neighborhoods
def filter_table(tabela_bairro, geocode, nome_municipio, nome_final_tabela):
    #find geocode ibge
    table = geocode[(geocode.nome == nome_municipio)]

    #filter by GEOCODIGO IBGE
    filtered = tabela_bairro[tabela_bairro.ibge == table['geocodigo'].iloc[0]]
    filtered.index.name = 'id'

    # ignore the nan neighborhoods
    filtered_2 = filtered[filtered['NO_LOCALIDADE_FAM']!='nan']

    #we cannot apply similarity with neighborhood with number names, so all we convert the table to a string table
    convert_to_str = filtered_2.astype(str)

    # connect to sqlite
    # object
    connection_obj = sqlite3.connect(r'C:\Users\hirom\Documents\Tese\CODE\Data\project.db')
    cursor_obj = connection_obj.cursor()

    # CREATE TABLE
    # transform the header into list
    column_names = list(convert_to_str.columns.values)
    SQL_query = []

    for head in column_names:
        SQL_query.append(head + ' ' + 'VARCHAR(255)')

    query = 'CREATE TABLE ' + '{}'.format(nome_final_tabela) + ' (' + ' ,'.join(SQL_query) + ');'
    print(query)
    cursor_obj.execute(query)

    #INSERT DATA
    # the number os inserts
    values_tuple = tuple('?' * len(column_names))
    convert_to_string = convert_to_str.astype(str)
    inserts = convert_to_string.to_records(index=False)

    try:

        sqlite_insert_query = 'INSERT INTO ' + '{}'.format(nome_final_tabela) + ' (' + ','.join(column_names) + ')' + \
                              ' VALUES (' + ','.join(values_tuple) + ');'
        print(sqlite_insert_query)
        cursor_obj.executemany(sqlite_insert_query, inserts)
        connection_obj.commit()
        print("Total", cursor_obj.rowcount, "Records inserted successfully into SqliteDb_developers table")
        connection_obj.commit()
        cursor_obj.close()

    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table", error)
    finally:
        if connection_obj:
            connection_obj.close()
            print("The SQLite connection is closed")

    print("table is on SQLite")

filter_table(bairros_geral,geocodes,'Recife','rec_2021')
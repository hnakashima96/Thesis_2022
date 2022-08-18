import sqlite3
import pandas as pd

#add the path of the data to convert and the table name desired between ''
def create_sqlite_table(table_to_add,table_name):
    #connect to sqlite
    #object
    connection_obj = sqlite3.connect(r'C:\Users\hirom\Documents\Tese\CODE\Data\project.db')
    #cursor object
    cursor_obj = connection_obj.cursor()
    #drop table if already exists
    cursor_obj.execute("DROP TABLE IF EXISTS GEEK")
    #Creating table
    #transform the header into list
    column_names = list(table_to_add.columns.values)

    SQL_query = []

    for head in column_names:
        SQL_query.append(head + ' ' + 'VARCHAR(255)')

    query = 'CREATE TABLE ' + '{}'.format(table_name) + ' (' + ' ,'.join(SQL_query) + ');'
    print(query)
    cursor_obj.execute(query)

    print("table is on SQLite")



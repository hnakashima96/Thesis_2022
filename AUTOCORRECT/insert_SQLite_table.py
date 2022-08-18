import sqlite3
import pandas as pd

def insertMultipleRecords(table_to_insert, table_name):

    #convert the table to string and then a tuple
    ref = table_to_insert
    convert_to_string = ref.astype(str)
    inserts = convert_to_string.to_records(index=False)

    #header of the table
    column_names = list(ref.columns.values)

    #the number os inserts
    values_tuple = tuple('?'*len(column_names))

    try:
        sqliteConnection = sqlite3.connect(r'C:\Users\hirom\Documents\Tese\CODE\Data\project.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_query = 'INSERT INTO ' + '{}'.format(table_name) + ' (' + ','.join(column_names) + ')' +\
                              ' VALUES ('+ ','.join(values_tuple) + ');'
        print(sqlite_insert_query)
        cursor.executemany(sqlite_insert_query, inserts)
        sqliteConnection.commit()
        print("Total", cursor.rowcount, "Records inserted successfully into SqliteDb_developers table")
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


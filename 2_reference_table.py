import pandas as pd
import sqlite3

#function to create the dictionary table of each city
def ref_table(nome_tab_muni, final_name):
    con = sqlite3.connect(r'C:\Users\hirom\Documents\Tese\CODE\Data\project.db')
    cursor_obj = con.cursor()
    bairro_municipios = pd.read_sql_query('SELECT * from ' + nome_tab_muni, con)
    sum_qtde = cursor_obj.execute('SELECT sum(qtde) from ' + nome_tab_muni).fetchone()

    #columns to create the final table
    column = ['ibge','bairro_name','qtde']
    final_table = pd.DataFrame(columns = column)

    for index in bairro_municipios.index:
        row = bairro_municipios.loc[bairro_municipios.index.isin([index])]
        if (int(row.iat[0,2])/sum_qtde[0]) >= 0.001:
            add_row = pd.Series(data = {'ibge': row.iat[0,0],
                                    'bairro_name': row.iat[0,1],
                                    'qtde': row.iat[0,2]}, name=len(final_table))
            final_table = final_table.append(add_row, ignore_index=False)

    # CREATE TABLE
    # transform the header into list
    column_names = list(final_table.columns.values)
    SQL_query = []

    for head in column_names:
        SQL_query.append(head + ' ' + 'VARCHAR(255)')

    query = 'CREATE TABLE ' + '{}'.format(final_name) + ' (' + ' ,'.join(SQL_query) + ');'
    print(query)
    cursor_obj.execute(query)

    #INSERT DATA
    # the number os inserts
    values_tuple = tuple('?' * len(column_names))
    convert_to_string = final_table.astype(str)
    inserts = convert_to_string.to_records(index=False)

    try:

        sqlite_insert_query = 'INSERT INTO ' + '{}'.format(final_name) + ' (' + ','.join(column_names) + ')' + \
                              ' VALUES (' + ','.join(values_tuple) + ');'
        print(sqlite_insert_query)
        cursor_obj.executemany(sqlite_insert_query, inserts)
        con.commit()
        print("Total", cursor_obj.rowcount, "Records inserted successfully into SqliteDb_developers table")
        con.commit()
        cursor_obj.close()

    except sqlite3.Error as error:
        print("Failed to insert multiple records into sqlite table", error)
    finally:
        if con:
            con.close()
            print("The SQLite connection is closed")

    print("table is on SQLite")


ref_table('rec_2021','ref_rec_2021')

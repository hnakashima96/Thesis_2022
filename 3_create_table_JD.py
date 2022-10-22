import pandas as pd
import sqlite3
from jaccard_distance import jaccard_distance
from create_SQLite_table import create_sqlite_table
from insert_SQLite_table import insertMultipleRecords

#function to apply similarity method of jaccard distance to identify the string similarity
def similarity(bd_municipio, ref_municipio, final_name):
    con = sqlite3.connect(r'C:\Users\hirom\Documents\Tese\CODE\Data\project.db')
    cursor_obj = con.cursor()
    bd = pd.read_sql_query('SELECT * from ' + bd_municipio, con)
    ref = pd.read_sql_query('SELECT * from ' + ref_municipio, con)

    #final result - Table
    column = ['bairro_name','ref_comparison','LD_value']

    #dice above 0.8
    ld_table = pd.DataFrame(columns = column)

    for ref_index in ref.index:
        for index in bd.index:
            comp = jaccard_distance(ref._get_value(ref_index,'bairro_name'), bd._get_value(index,'NO_LOCALIDADE_FAM'))
            add_row = pd.Series(data={'bairro_name': ref._get_value(ref_index,'bairro_name'),
                                      'ref_comparison': bd._get_value(index,'NO_LOCALIDADE_FAM'),
                                      'coefficient': comp}, name=len(ld_table))
            ld_table = ld_table.append(add_row, ignore_index=False)

    ld_table.index.name = 'id'

    #create tables
    create_sqlite_table(ld_table, final_name+'_JD')
    insertMultipleRecords(ld_table, final_name+'_JD')

    cursor_obj.close()


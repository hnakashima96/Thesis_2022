import pandas as pd
import sqlite3

con = sqlite3.connect(r'C:\Users\hirom\Documents\Tese\CODE\Data\project.db')
cursor_obj = con.cursor()
bd = pd.read_sql_query('SELECT * from ' + 'bsb_2021', con)

#word counting
def w_count(bd):
    word_count_dict = {}
    for id in bd.index:
        word_count_dict[bd.iloc[id,1]] = int(bd.iloc[id,2])
    return word_count_dict


#get probabilities
def w_prob(bd):
    word_probabilities = {}
    sum_of_words = sum(bd['qtde'].astype(int))
    for id in bd.index:
        word_probabilities[bd.iloc[id,1]] = int(bd.iloc[id,2])/sum_of_words
    return word_probabilities


'''Find similar words'''

#references
#https://www.analyticsvidhya.com/blog/2021/11/autocorrect-feature-using-nlp-in-python/
#https://medium.com/@ruchita.chimu/autocorrect-using-nlp-8c66249fe760
#https://www.section.io/engineering-education/building-autocorrect-feature-using-nlp-with-python/


import pandas as pd
import sqlite3
from jaccard_distance import jaccard_distance
from pre_processing import w_prob
from create_SQLite_table import create_sqlite_table
from insert_SQLite_table import insertMultipleRecords

con = sqlite3.connect(r'C:\Users\hirom\Documents\Tese\CODE\Data\project.db')
cursor_obj = con.cursor()
bd = pd.read_sql_query('SELECT * from ' + 'cwb_2021', con)
ref = pd.read_sql_query('SELECT * from ' + 'ref_cwb_2021', con)

def correct_name_JD(ref,name_neighborbood):

    # prob of the word (peso da palavra em relação ao total de famílias)
    probs = w_prob(ref)
    # criar um df para conseguir adicionar as possíveis palavras parecidas (word bag)
    df = pd.DataFrame.from_dict(probs, orient='index').reset_index()
    df = df.rename(columns={'index': 'Word', 0: 'Prob'})

    #evaluate if the name is already correct
    if name_neighborbood in ref.iloc[:,1]:
        return name_neighborbood
    else:
        #if not find the most possible to be based on the similarity and family probability
        for correct_neighborhood in ref.iloc[:,1]:
            distance = jaccard_distance(name_neighborbood,correct_neighborhood)
            df.loc[df['Word'] == correct_neighborhood,'Similarity'] = distance
            output = df.sort_values(['Similarity','Prob'], ascending=True).head()
        #if it is inside the criteria of distance decided find the correction
        if output.iloc[0,2] > 0.6:
            return ('N/A')
        else:
            return output.iloc[0,0]

#apply on all DB

for id in bd.index:
    correct_name = correct_name_JD(ref, bd.iloc[id,1])
    bd.loc[bd.index == id, 'Correction'] = correct_name

create_sqlite_table(bd,'correct_name_cwb2021')
insertMultipleRecords(bd,'correct_name_cwb2021')




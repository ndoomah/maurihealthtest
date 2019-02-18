import pandas as pd
import json

# Load data from csv file
data = pd.DataFrame.from_csv('data.csv')

d_list = ['influenza', 'gastroenteritis', 'conjunctivitis', 'respiratory infection']

for d in d_list:
    t = data[data['disease'] == d].groupby('date')[['disease']].count()
    print(t)
    t.to_csv(d+'.csv', encoding='utf-8')


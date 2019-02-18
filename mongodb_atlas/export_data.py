
# !/usr/bin/python
# -*- coding: utf-8 -*-
import pandas
import json

from mongodb_atlas import connect_db


'''Twitter_file = "C:/testfile.csv"
os.system('mongoexport --host Cluster0-shard-0/cluster0-shard-00-00-oov30.mongodb.net:27017,cluster0-shard-00-01-oov30.mongodb.net:27017,cluster0-shard-00-02-oov30.mongodb.net:27017 --ssl --username fyp_admin --password fyp_pwd --authenticationDatabase admin --db test2 --collection testing --type csv --out C:/testfile.csv')

tweets = []
for line in open(Twitter_file, 'r'):
    tweets.append(json.loads(line))

for doc in tweets:
    print(doc)
'''

# --- Exporting data from FACEBOOK & MAURIHEALTH & TWITTER collections ---#


result = connect_db.retrieve_all()
json_data = json.dumps(result)
df = pandas.read_json(json_data)
df.to_csv('./analysis/data.csv', encoding='utf-8', index=False)

import pymongo

#MONGODB ATLAS URL
DB_URI = 'mongodb+srv://fyp_admin:fyp_pwd@cluster0-oov30.mongodb.net/test?retryWrites=true'

def save_data(json_array, collection_name):
    client = pymongo.MongoClient(DB_URI)
    db = client.test
    collections = {
        'facebook': db.facebook,
        'articles_map': db.articles_map,
        'articles_web': db.articles_web
    }
    collection = collections.get(collection_name)

    for data in json_array:
        try:
            collection.insert_one(data).inserted_id
        except:
            print("Failed to insert data to database")
        finally:
            client.close()

def save_tweet(data):
    client = pymongo.MongoClient(DB_URI)
    db = client.test
    collection = db.twitter
    try:
        collection.update(data, data, upsert=True)
    except:
        print("failed to insert data to db")
    finally:
        client.close()


def save_trends(json_array):
    client = pymongo.MongoClient(DB_URI)
    db = client.test
    collection = db.googletrends
    try:
        collection.insert_one(json_array).inserted_id
    except:
        print("Failed to insert data to database")
    finally:
        client.close()

def retrieve_data():
    client = pymongo.MongoClient(DB_URI)
    db = client.test
    fb = db.facebook
    maurihealth = db.maurihealth
    articles_m = db.articles_map
    articles_w = db.articles_web

    arr_loc = []

    input_fb = fb.find({})
    for post in input_fb:
            arr_loc.append(post)

    input_m = maurihealth.find({})
    for data in input_m:
        arr_loc.append(data)

    input_map = articles_m.find({})
    for data in input_map:
        arr_loc.append(data)
    input_web = articles_w.find({})
    for data in input_web:
        d = data['location']
        arr_loc.append(data)

    return arr_loc
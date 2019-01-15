import json
from analysis import text_analyse
from mongodb_atlas import connect_db

# INITIALISE ARRAY FOR KEEPING ARTICLES THAT WILL BE DISPLAYED ON THE WEBSITE HOMEPAGE
article_arr = []
# INITIALISE ARRAY FOR KEEPING DISEASE, DATA & LOCATION DETAILS ABOUT SAID ARTICLES
data_arr = []

with open("scraped_articles.json") as json_file:
    json_data=json.load(json_file)
    #for key,data in json_data.items():
    newspapers = json_data['newspapers']
    for key,data in newspapers.items():
        newspaper = data['articles']
        for n in newspaper:
            text = n['text']
            date = n['published']
            link = n['link']
            title = n['title']

            disease_result = text_analyse.extract_disease(text, 80)

            if disease_result == "":
                print("Discarding article...")
            else:
                location_result = text_analyse.extract_location(text, 80)

                if location_result == "":
                    location_result = "Not found"

                data={}
                data['article'] = {
                    "disease": disease_result,
                    "date": date,
                    "location": location_result
                }
                data_arr.append(data)
                art ={}
                art['news'] = {
                    "link": link,
                    "published": date,
                    "title": title,
                    "text": text,
                    "author":n
                }
                article_arr.append(art)

    #END OF LOOPING

    #STORING ARRAYS TO CLOUD
    try:
        connect_db.save_article(data_arr, "map")
        connect_db.save_article(art, "web")
    except:
        print("No data to save!")
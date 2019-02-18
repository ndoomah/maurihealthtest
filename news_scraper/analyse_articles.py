import json
from analysis import text_analyse
from mongodb_atlas import connect_db

# INITIALISE ARRAY FOR KEEPING ARTICLES THAT WILL BE DISPLAYED ON THE WEBSITE HOMEPAGE
article_arr = []
# INITIALISE ARRAY FOR KEEPING DISEASE, DATA & LOCATION DETAILS ABOUT SAID ARTICLES
data_arr = []

with open("./news_scraper/scraped_articles.json") as json_file:
    json_data=json.load(json_file)
    #for key,data in json_data.items():
    newspapers = json_data['newspapers']
    for key,data in newspapers.items():
        newspaper = data['articles']
        for n in newspaper:
            text = n['text']
            date = n['published'].rsplit('T',1)[0]
            #date = n['published']
            link = n['link']
            title = n['title']

            disease_result, sent = text_analyse.ext_disease(text, 90)
            print(disease_result)

            if disease_result == "":
                print("Discarding article...")
            else:
                location_result = text_analyse.extract_location(text, 90)

                if location_result == "":
                    location_result = "Not found"

                data = {
                    "diseasetype": disease_result,
                    "description": sent,
                    "date": date,
                    "location": location_result
                }
                data_arr.append(data)

                art = {
                    "link": link,
                    "published": date,
                    "title": title,
                    "text": text
                }
                article_arr.append(art)

    #END OF LOOPING

    #STORING ARRAYS TO CLOUD
    print(data_arr)
    print(article_arr)

    connect_db.save_data(data_arr, "articles_map")
    #connect_db.save_data(article_arr, "articles_web")

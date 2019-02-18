*Analysis*

- text analysis >> data cleaning and pre processing
- data analysis >> computes total number of cases for each disease based on date
- prediction >> implementation of R package prophet 

*Mongodb_atlas*

- connect_db >> methods to save data on cloud, and to retrieve data from cloud
- export_data >> exports data from all collections to csv file

*Facebook*

- fb_scraper >> to extract previous/archived posts about each disease from fb
- fb_realtime >> runs continuously to extract recent posts in real time
- fb_methods >> generic selenium methods to construct bot scraper

*News_scraper*

- NewsScraper >> main program (extracts maximum four articles from each newspaper and then saves results to scraped_articles.json)
- NewsPapers >> json file that contains newspaper links/rss feeds
- analyse_articles >> validation of each article for storage on cloud

-- MAIN
[purpose: to run fb_realtime & news_scraper in parallel]

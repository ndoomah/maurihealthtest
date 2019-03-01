
## Webscraper
### Facebook

- fb_scraper >> to extract previous/archived posts about each disease from fb
- fb_realtime >> runs continuously to extract recent posts in real time
- fb_methods >> generic selenium methods to construct bot scraper

### News_scraper 

- NewsScraper >> main program (extracts maximum four articles from each newspaper and then saves results to scraped_articles.json)
- NewsPapers >> json file that contains newspaper links/rss feeds
- analyse_articles >> validation of each article for storage on cloud

## Storage- Mongodb_atlas

- connect_db >> methods to save data on cloud, and to retrieve data from cloud
- export_data >> exports data from all collections to csv file

## Analysis

- text analysis >> data cleaning and pre processing
- data analysis >> takes as input data.csv and outputs prediction graphs for each disease (through rpredict function in prediction.R)
- prediction >> implementation of rpredict function (use of R package prophet) 

*Requirements to run data_analysis.py:*
- installation of Rtools.exe (https://cran.r-project.org/bin/windows/Rtools/)
- R 3.5 

## Flask App (to be added)


*Requirements for app.py:*
- create a virtual environment for the project



#IMPORTING FILES
from mongodb_atlas import connect_db
from facebook.fb_methods import *

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    WebDriverException,
    )


global USERNAME, PASSWORD
USERNAME = 'n.beeha15@gmail.com'
PASSWORD = 'admin123'
global RETURN_KEY
RETURN_KEY = Keys.RETURN

# Facebook search URLs

#ALL TIME search
FLU_ALL = "https://www.facebook.com/search/str/flu+in+mauritius/stories-keyword?epa=SEE_MORE"
GASTRO_ALL = "https://www.facebook.com/search/str/gastro+in+mauritius/stories-keyword?epa=SEE_MORE"
CONJ_ALL = "https://www.facebook.com/search/str/conjunctivitis+in+mauritius/stories-keyword?epa=SEE_MORE"
RESP_ALL = "https://www.facebook.com/search/str/respiratory+infection+in+mauritius/stories-keyword?epa=SEE_MORE"

# ---- 2018 LINKS ----
FLU_DEC18_URL = "https://www.facebook.com/search/top/?q=posts%20about%20flu%20in%20mauritius&epa=FILTERS&filters=eyJycF9jcmVhdGlvbl90aW1lIjoie1wibmFtZVwiOlwiY3JlYXRpb25fdGltZVwiLFwiYXJnc1wiOlwie1xcXCJzdGFydF9tb250aFxcXCI6XFxcIjIwMTgtMTJcXFwiLFxcXCJlbmRfeWVhclxcXCI6XFxcIjIwMThcXFwifVwifSJ9"
GASTRO_DEC18_URL = "https://www.facebook.com/search/str/posts+about+gastro+in+mauritius/keywords_blended_posts?filters=eyJycF9hdXRob3IiOiJ7XCJuYW1lXCI6XCJtZXJnZWRfcHVibGljX3Bvc3RzXCIsXCJhcmdzXCI6XCJcIn0iLCJycF9jcmVhdGlvbl90aW1lIjoie1wibmFtZVwiOlwiY3JlYXRpb25fdGltZVwiLFwiYXJnc1wiOlwie1xcXCJzdGFydF9tb250aFxcXCI6XFxcIjIwMTgtMTJcXFwiLFxcXCJlbmRfeWVhclxcXCI6XFxcIjIwMThcXFwifVwifSJ9&epa=FILTERS"
RESPIRATORY_2018 = "https://www.facebook.com/search/str/posts+about+respiratory+infection+in+mauritius/keywords_blended_posts?epa=FILTERS&filters=eyJycF9jcmVhdGlvbl90aW1lIjoie1wibmFtZVwiOlwiY3JlYXRpb25fdGltZVwiLFwiYXJnc1wiOlwie1xcXCJzdGFydF95ZWFyXFxcIjpcXFwiMjAxOFxcXCIsXFxcInN0YXJ0X21vbnRoXFxcIjpcXFwiMjAxOC0xXFxcIixcXFwiZW5kX3llYXJcXFwiOlxcXCIyMDE4XFxcIixcXFwiZW5kX21vbnRoXFxcIjpcXFwiMjAxOC0xMlxcXCIsXFxcInN0YXJ0X2RheVxcXCI6XFxcIjIwMTgtMS0xXFxcIixcXFwiZW5kX2RheVxcXCI6XFxcIjIwMTgtMTItMzFcXFwifVwifSJ9"

# ---- 2019 LINKS ----
global FLU_2019_URL, GASTRO_2019_URL, PINKEYE_2019_URL, RESPIRATORY_2019_URL
FLU_2019_URL = "https://www.facebook.com/search/str/posts+about+flu+in+mauritius/keywords_blended_posts?epa=FILTERS&filters=eyJycF9jcmVhdGlvbl90aW1lIjoie1wibmFtZVwiOlwiY3JlYXRpb25fdGltZVwiLFwiYXJnc1wiOlwie1xcXCJzdGFydF95ZWFyXFxcIjpcXFwiMjAxOVxcXCIsXFxcInN0YXJ0X21vbnRoXFxcIjpcXFwiMjAxOS0xXFxcIixcXFwiZW5kX3llYXJcXFwiOlxcXCIyMDE5XFxcIixcXFwiZW5kX21vbnRoXFxcIjpcXFwiMjAxOS0xMlxcXCIsXFxcInN0YXJ0X2RheVxcXCI6XFxcIjIwMTktMS0xXFxcIixcXFwiZW5kX2RheVxcXCI6XFxcIjIwMTktMTItMzFcXFwifVwifSJ9"
GASTRO_2019_URL = "https://www.facebook.com/search/str/posts+about+gastro+in+mauritius/keywords_blended_posts?epa=FILTERS&filters=eyJycF9hdXRob3IiOiJ7XCJuYW1lXCI6XCJtZXJnZWRfcHVibGljX3Bvc3RzXCIsXCJhcmdzXCI6XCJcIn0iLCJycF9jcmVhdGlvbl90aW1lIjoie1wibmFtZVwiOlwiY3JlYXRpb25fdGltZVwiLFwiYXJnc1wiOlwie1xcXCJzdGFydF95ZWFyXFxcIjpcXFwiMjAxOVxcXCIsXFxcInN0YXJ0X21vbnRoXFxcIjpcXFwiMjAxOS0xXFxcIixcXFwiZW5kX3llYXJcXFwiOlxcXCIyMDE5XFxcIixcXFwiZW5kX21vbnRoXFxcIjpcXFwiMjAxOS0xMlxcXCIsXFxcInN0YXJ0X2RheVxcXCI6XFxcIjIwMTktMS0xXFxcIixcXFwiZW5kX2RheVxcXCI6XFxcIjIwMTktMTItMzFcXFwifVwifSJ9"
PINKEYE_2019_URL = "https://www.facebook.com/search/posts/?q=posts%20about%20pinkeye%20in%20mauritius&em=1&epa=FILTERS&filters=eyJycF9jcmVhdGlvbl90aW1lIjoie1wibmFtZVwiOlwiY3JlYXRpb25fdGltZVwiLFwiYXJnc1wiOlwie1xcXCJzdGFydF95ZWFyXFxcIjpcXFwiMjAxOVxcXCIsXFxcInN0YXJ0X21vbnRoXFxcIjpcXFwiMjAxOS0xXFxcIixcXFwiZW5kX3llYXJcXFwiOlxcXCIyMDE5XFxcIixcXFwiZW5kX21vbnRoXFxcIjpcXFwiMjAxOS0xMlxcXCIsXFxcInN0YXJ0X2RheVxcXCI6XFxcIjIwMTktMS0xXFxcIixcXFwiZW5kX2RheVxcXCI6XFxcIjIwMTktMTItMzFcXFwifVwifSJ9"
RESPIRATORY_2019_URL = "https://www.facebook.com/search/str/posts+about+respiratory+infection+in+mauritius/keywords_blended_posts?epa=FILTERS&filters=eyJycF9jcmVhdGlvbl90aW1lIjoie1wibmFtZVwiOlwiY3JlYXRpb25fdGltZVwiLFwiYXJnc1wiOlwie1xcXCJzdGFydF95ZWFyXFxcIjpcXFwiMjAxOVxcXCIsXFxcInN0YXJ0X21vbnRoXFxcIjpcXFwiMjAxOS0xXFxcIixcXFwiZW5kX3llYXJcXFwiOlxcXCIyMDE5XFxcIixcXFwiZW5kX21vbnRoXFxcIjpcXFwiMjAxOS0xMlxcXCIsXFxcInN0YXJ0X2RheVxcXCI6XFxcIjIwMTktMS0xXFxcIixcXFwiZW5kX2RheVxcXCI6XFxcIjIwMTktMTItMzFcXFwifVwifSJ9"

# Path where to store the JSON result file.
DESTINATION_PATH = 'posts.json'

# How much seconds to do dynamic waits.
WAIT_TIME = 5


# Chrome driver should be run
executable_path=os.path.join('chromedriver')

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
# instantiate a chrome options object so you can set the size and headless preference
options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")

# 1-Allow, 2-Block, 0-default
preferences = {
    "profile.default_content_setting_values.notifications" : 2,
    "profile.default_content_setting_values.location": 2,
    # We don't need images, only the URLs.
    "profile.managed_default_content_settings.images": 2,
    }
options.add_experimental_option("prefs", preferences)

global browser
browser = webdriver.Chrome(
    executable_path=executable_path,
    chrome_options=options,
    )

#browser = webdriver.Firefox(executable_path='C:/WebScraper/firefox/geckodriver.exe')
browser.wait = WebDriverWait(browser, WAIT_TIME)

# Make sure browser is always closed, even on errors.
atexit.register(close_browser, browser)

#
#
# STEP 1 >> CREATE FILE(IF NEEDED) AND INITIALISE ARRAY
#file = open(DESTINATION_PATH, "x")
data_arr=[]

# STEP 2 >> LOGGING TO FB WITH CREDENTIALS
fb_login(browser)

# STEP 3 >> SEARCH FOR FLU DISEASE POSTS
scrape_page(FLU_2019_URL, browser, "influenza", data_arr)

# STEP 4 >> SEARCH FOR GASTRO DISEASE POSTS
scrape_page(GASTRO_2019_URL, browser, "gastroenteritis", data_arr)

#(CONJUNCTIVITIS & UTR TO BE ADDED)
scrape_page(PINKEYE_2019_URL, browser, "conjunctivitis", data_arr)

scrape_page(RESPIRATORY_2019_URL, browser, "respiratory infection", data_arr)

# STEP 5 >> SAVE DATA ARRAY TO MONGODB CLOUD
#save_to_file(data_arr, DESTINATION_PATH)
try:
    connect_db.save_data(data_arr, 'facebook')
except:
    print("No data to save!")


# STEP 6 >> LOGOUT FROM FB
close_browser(browser)
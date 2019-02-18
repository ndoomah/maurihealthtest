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
from multiprocessing.pool import Pool


global USERNAME, PASSWORD
USERNAME = 'n.beeha15@gmail.com'
PASSWORD = 'admin123'
global RETURN_KEY
RETURN_KEY = Keys.RETURN

# ---- 2019 LINKS ----
global FLU_2019_URL, GASTRO_2019_URL, PINKEYE_2019_URL, RESPIRATORY_2019_URL
FLU_2019_URL = "https://www.facebook.com/search/str/posts+about+flu+in+mauritius/keywords_blended_posts?epa=FILTERS&filters=eyJycF9jcmVhdGlvbl90aW1lIjoie1wibmFtZVwiOlwiY3JlYXRpb25fdGltZVwiLFwiYXJnc1wiOlwie1xcXCJzdGFydF95ZWFyXFxcIjpcXFwiMjAxOVxcXCIsXFxcInN0YXJ0X21vbnRoXFxcIjpcXFwiMjAxOS0xXFxcIixcXFwiZW5kX3llYXJcXFwiOlxcXCIyMDE5XFxcIixcXFwiZW5kX21vbnRoXFxcIjpcXFwiMjAxOS0xMlxcXCIsXFxcInN0YXJ0X2RheVxcXCI6XFxcIjIwMTktMS0xXFxcIixcXFwiZW5kX2RheVxcXCI6XFxcIjIwMTktMTItMzFcXFwifVwifSJ9"
GASTRO_2019_URL = "https://www.facebook.com/search/str/posts+about+gastro+in+mauritius/keywords_blended_posts?epa=FILTERS&filters=eyJycF9hdXRob3IiOiJ7XCJuYW1lXCI6XCJtZXJnZWRfcHVibGljX3Bvc3RzXCIsXCJhcmdzXCI6XCJcIn0iLCJycF9jcmVhdGlvbl90aW1lIjoie1wibmFtZVwiOlwiY3JlYXRpb25fdGltZVwiLFwiYXJnc1wiOlwie1xcXCJzdGFydF95ZWFyXFxcIjpcXFwiMjAxOVxcXCIsXFxcInN0YXJ0X21vbnRoXFxcIjpcXFwiMjAxOS0xXFxcIixcXFwiZW5kX3llYXJcXFwiOlxcXCIyMDE5XFxcIixcXFwiZW5kX21vbnRoXFxcIjpcXFwiMjAxOS0xMlxcXCIsXFxcInN0YXJ0X2RheVxcXCI6XFxcIjIwMTktMS0xXFxcIixcXFwiZW5kX2RheVxcXCI6XFxcIjIwMTktMTItMzFcXFwifVwifSJ9"
PINKEYE_2019_URL = "https://www.facebook.com/search/posts/?q=posts%20about%20pinkeye%20in%20mauritius&em=1&epa=FILTERS&filters=eyJycF9jcmVhdGlvbl90aW1lIjoie1wibmFtZVwiOlwiY3JlYXRpb25fdGltZVwiLFwiYXJnc1wiOlwie1xcXCJzdGFydF95ZWFyXFxcIjpcXFwiMjAxOVxcXCIsXFxcInN0YXJ0X21vbnRoXFxcIjpcXFwiMjAxOS0xXFxcIixcXFwiZW5kX3llYXJcXFwiOlxcXCIyMDE5XFxcIixcXFwiZW5kX21vbnRoXFxcIjpcXFwiMjAxOS0xMlxcXCIsXFxcInN0YXJ0X2RheVxcXCI6XFxcIjIwMTktMS0xXFxcIixcXFwiZW5kX2RheVxcXCI6XFxcIjIwMTktMTItMzFcXFwifVwifSJ9"
RESPIRATORY_2019_URL = "https://www.facebook.com/search/str/posts+about+respiratory+infection+in+mauritius/keywords_blended_posts?epa=FILTERS&filters=eyJycF9jcmVhdGlvbl90aW1lIjoie1wibmFtZVwiOlwiY3JlYXRpb25fdGltZVwiLFwiYXJnc1wiOlwie1xcXCJzdGFydF95ZWFyXFxcIjpcXFwiMjAxOVxcXCIsXFxcInN0YXJ0X21vbnRoXFxcIjpcXFwiMjAxOS0xXFxcIixcXFwiZW5kX3llYXJcXFwiOlxcXCIyMDE5XFxcIixcXFwiZW5kX21vbnRoXFxcIjpcXFwiMjAxOS0xMlxcXCIsXFxcInN0YXJ0X2RheVxcXCI6XFxcIjIwMTktMS0xXFxcIixcXFwiZW5kX2RheVxcXCI6XFxcIjIwMTktMTItMzFcXFwifVwifSJ9"

URL_LIST = [FLU_2019_URL, GASTRO_2019_URL, PINKEYE_2019_URL, RESPIRATORY_2019_URL]

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
WAIT_TIME = 5

#browser = webdriver.Firefox(executable_path='C:/WebScraper/firefox/geckodriver.exe')
browser.wait = WebDriverWait(browser, WAIT_TIME)

# Make sure browser is always closed, even on errors.
atexit.register(close_browser, browser)

def scrape(url):

    # STEP 2 >> LOGGING TO FB WITH CREDENTIALS
    fb_login(browser)
    count = 0

    while True:
        result = scrape_page_test(url, browser)
        d = result[0]
        disease = d['diseasetype']
        count = count + 1
        print(disease +" "+ str(count))
        #print(result)
        try:
            connect_db.save_data(result, 'facebook')
        except:
            print("No data to save!")

        time.sleep(40)
        browser.refresh()


def main():
    with Pool(5) as p:
        p.map(scrape, URL_LIST)
        #p.terminate()
        #p.join()

if __name__ == '__main__':
    main()

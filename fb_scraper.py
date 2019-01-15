import atexit
import os
import time
import json

#IMPORTING FILES FROM analysis AND mongodb_atlas DIRECTORIES
from mongodb_atlas import connect_db
from analysis import text_analyse
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    WebDriverException,
    )


# Enter your own facebook username and password
USERNAME = 'n.beeha15@gmail.com'
PASSWORD = 'admin123'

# Facebook search URL
# ---- 2018 LINKS ----
FLU_DEC18_URL = "https://www.facebook.com/search/top/?q=posts%20about%20flu%20in%20mauritius&epa=FILTERS&filters=eyJycF9jcmVhdGlvbl90aW1lIjoie1wibmFtZVwiOlwiY3JlYXRpb25fdGltZVwiLFwiYXJnc1wiOlwie1xcXCJzdGFydF9tb250aFxcXCI6XFxcIjIwMTgtMTJcXFwiLFxcXCJlbmRfeWVhclxcXCI6XFxcIjIwMThcXFwifVwifSJ9"
GASTRO_DEC18_URL = "https://www.facebook.com/search/str/posts+about+gastro+in+mauritius/keywords_blended_posts?filters=eyJycF9hdXRob3IiOiJ7XCJuYW1lXCI6XCJtZXJnZWRfcHVibGljX3Bvc3RzXCIsXCJhcmdzXCI6XCJcIn0iLCJycF9jcmVhdGlvbl90aW1lIjoie1wibmFtZVwiOlwiY3JlYXRpb25fdGltZVwiLFwiYXJnc1wiOlwie1xcXCJzdGFydF9tb250aFxcXCI6XFxcIjIwMTgtMTJcXFwiLFxcXCJlbmRfeWVhclxcXCI6XFxcIjIwMThcXFwifVwifSJ9&epa=FILTERS"

# ---- 2019 LINKS ----
FLU_2019_URL = "https://www.facebook.com/search/str/posts+about+flu+in+mauritius/keywords_blended_posts?epa=FILTERS&filters=eyJycF9jcmVhdGlvbl90aW1lIjoie1wibmFtZVwiOlwiY3JlYXRpb25fdGltZVwiLFwiYXJnc1wiOlwie1xcXCJzdGFydF95ZWFyXFxcIjpcXFwiMjAxOVxcXCIsXFxcInN0YXJ0X21vbnRoXFxcIjpcXFwiMjAxOS0xXFxcIixcXFwiZW5kX3llYXJcXFwiOlxcXCIyMDE5XFxcIixcXFwiZW5kX21vbnRoXFxcIjpcXFwiMjAxOS0xMlxcXCIsXFxcInN0YXJ0X2RheVxcXCI6XFxcIjIwMTktMS0xXFxcIixcXFwiZW5kX2RheVxcXCI6XFxcIjIwMTktMTItMzFcXFwifVwifSJ9"
GASTRO_2019_URL = "https://www.facebook.com/search/str/posts+about+gastro+in+mauritius/keywords_blended_posts?epa=FILTERS&filters=eyJycF9hdXRob3IiOiJ7XCJuYW1lXCI6XCJtZXJnZWRfcHVibGljX3Bvc3RzXCIsXCJhcmdzXCI6XCJcIn0iLCJycF9jcmVhdGlvbl90aW1lIjoie1wibmFtZVwiOlwiY3JlYXRpb25fdGltZVwiLFwiYXJnc1wiOlwie1xcXCJzdGFydF95ZWFyXFxcIjpcXFwiMjAxOVxcXCIsXFxcInN0YXJ0X21vbnRoXFxcIjpcXFwiMjAxOS0xXFxcIixcXFwiZW5kX3llYXJcXFwiOlxcXCIyMDE5XFxcIixcXFwiZW5kX21vbnRoXFxcIjpcXFwiMjAxOS0xMlxcXCIsXFxcInN0YXJ0X2RheVxcXCI6XFxcIjIwMTktMS0xXFxcIixcXFwiZW5kX2RheVxcXCI6XFxcIjIwMTktMTItMzFcXFwifVwifSJ9"
PINKEYE_2019_URL = "https://www.facebook.com/search/str/posts+about+pink+eye+in+mauritius/keywords_blended_posts?epa=FILTERS&filters=eyJycF9jcmVhdGlvbl90aW1lIjoie1wibmFtZVwiOlwiY3JlYXRpb25fdGltZVwiLFwiYXJnc1wiOlwie1xcXCJzdGFydF95ZWFyXFxcIjpcXFwiMjAxOVxcXCIsXFxcInN0YXJ0X21vbnRoXFxcIjpcXFwiMjAxOS0xXFxcIixcXFwiZW5kX3llYXJcXFwiOlxcXCIyMDE5XFxcIixcXFwiZW5kX21vbnRoXFxcIjpcXFwiMjAxOS0xMlxcXCIsXFxcInN0YXJ0X2RheVxcXCI6XFxcIjIwMTktMS0xXFxcIixcXFwiZW5kX2RheVxcXCI6XFxcIjIwMTktMTItMzFcXFwifVwifSJ9"
RESPIRATORY_2019_URL = "https://www.facebook.com/search/str/posts+about+respiratory+infection+in+mauritius/keywords_blended_posts?epa=FILTERS&filters=eyJycF9jcmVhdGlvbl90aW1lIjoie1wibmFtZVwiOlwiY3JlYXRpb25fdGltZVwiLFwiYXJnc1wiOlwie1xcXCJzdGFydF95ZWFyXFxcIjpcXFwiMjAxOVxcXCIsXFxcInN0YXJ0X21vbnRoXFxcIjpcXFwiMjAxOS0xXFxcIixcXFwiZW5kX3llYXJcXFwiOlxcXCIyMDE5XFxcIixcXFwiZW5kX21vbnRoXFxcIjpcXFwiMjAxOS0xMlxcXCIsXFxcInN0YXJ0X2RheVxcXCI6XFxcIjIwMTktMS0xXFxcIixcXFwiZW5kX2RheVxcXCI6XFxcIjIwMTktMTItMzFcXFwifVwifSJ9"

# Path where to store the JSON result file.
DESTINATION_PATH = 'posts.json'

# How much seconds to do dynamic waits.
WAIT_TIME = 10


# Chrome driver should be un
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


browser = webdriver.Chrome(
    executable_path=executable_path,
    chrome_options=options,
    )
browser.wait = WebDriverWait(browser, WAIT_TIME)


def close_browser(driver):
    """
    Close the browser.
    """
    try:
        driver.close()
    except WebDriverException:
        # Might be already closed.
        pass

# Make sure browser is always closed, even on errors.
atexit.register(close_browser, browser)

def fb_login(driver):
    """
    Login to facebook using username and password.
    """
    driver.get('https://www.facebook.com/')
    usr = driver.find_element_by_name("email")
    usr.send_keys(USERNAME)
    password = driver.find_element_by_name("pass")
    password.send_keys(PASSWORD)
    password.send_keys(Keys.RETURN)
    #raw_input(
     #   "Confirm that you authenticated with the right user.\n"
      #  "Check no browser popups are there."
       # )

def scroll_down(driver):
    """A method for scrolling the page."""

    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)


def move_to_element(driver, element):
    """
    Get element in the current viewport and have to mouse over it.
    """
    actions = ActionChains(driver)
    actions.move_to_element(element)
    actions.perform()

def go_to_page(url, driver):
    driver.get(url)


#---LOOPING THROUGH EACH POSTS----
def postLoop(postDiv, array, driver, searchterm):

    for post in postDiv:
    # scraping the post's title/name

        global t, d, c, contents
        """ --- post's title is not really needed ---
                title = driver.find_element_by_tag_name('h5')
                t = title.text
        """
        post.find_element_by_class_name('_6-co').click()
        time.sleep(5)

        # scraping the post's date
        date = driver.find_element_by_class_name("timestampContent")
        #date = driver.find_element_by_xpath("//span[@class='timestampContent']")
        d = date.text

        # scraping the post's contents
        contents = driver.find_elements_by_tag_name('p')
        c = ""
        for content in contents:
            c = c + content.text + "\t"

        #extract disease details from content to determine whether post is to be discarded or stored in db
        dis = text_analyse.extract_disease(c, 60)
        if dis == "":
            print("post not valid for storage, discarding...")
        else:
            #content is valid therefore post will be further analysed for location details if any, and then stored.

            #extract location details from the content
            loc = text_analyse.extract_location(c, 60)

            if loc == "":
                location = "Not found"
            else:
                location = loc

            #putting all scraped details into json file
            data = {

                'diseasetype': searchterm,
                'date': d,
                'location': location
            }
            array.append(data)

        time.sleep(1)
        el = driver.find_element_by_class_name('_n9')
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(el, 30, 30)
        action.click()
        action.perform()
        time.sleep(2)

def save_to_file(json_arr, path):
    try:
        with open(path, 'a') as outfile:
            json.dump(json_arr, outfile)
    except:
        print("file error")

def scrape_page(url, driver, diseaseterm, data_arr):

    go_to_page(url, driver)
    time.sleep(3)

    #Looping through the first post/div
    #firstdivloop = driver.find_elements_by_xpath("//div[@id='BrowseResultsContainer']/div/div/div/div")
    firstdivloop = driver.find_elements_by_xpath("//div[@id='BrowseResultsContainer']//div[@class='_6rbb']/div")
    postLoop(firstdivloop,data_arr,driver, diseaseterm)

    try:
        #Looping through the second post/div
        secdivloop = driver.find_elements_by_xpath("//div[@data-testid='paginated_results_pagelet']/div/div/div/div/div/div")
        postLoop(secdivloop,data_arr,driver, diseaseterm)

        #scroll to end of results
        scroll_down(driver)
        time.sleep(3)

        #looping through the rest of the posts
        scrollContainers = driver.find_elements_by_xpath("//div[contains (@id, 'fbBrowseScrollingPagerContainer')]")

        gototop = driver.find_element_by_xpath("//div[@data-testid='paginated_results_pagelet']/div")
        scroll_to_element(driver, gototop)
        time.sleep(3)

        for scrollContainer in scrollContainers:
            scroll_div = scrollContainer.find_elements_by_class_name("_307z")
            #scroll_div = scrollContainer.find_elements_by_xpath("//div[@class='_o02']")
            postLoop(scroll_div, data_arr, driver, diseaseterm)
            time.sleep(1)
    except:
        print("Only two posts found.")

# ----------------END OF FUNCTIONS DEFINITION------------------#
#--------------------------------------------------------------#


# STEP 1 >> CREATE FILE(IF NEEDED) AND INITIALISE ARRAY
#file = open(DESTINATION_PATH, "x")
data_arr=[]

# STEP 2 >> LOGGING TO FB WITH CREDENTIALS
fb_login(browser)

# STEP 3 >> SEARCH FOR FLU DISEASE POSTS
scrape_page(FLU_2019_URL, browser, "influenza", data_arr)
time.sleep(3)

# STEP 4 >> SEARCH FOR GASTRO DISEASE POSTS
scrape_page(GASTRO_2019_URL, browser, "gastroenteritis", data_arr)
time.sleep(1)

#(CONJUNCTIVITIS & UTR TO BE ADDED)

# STEP 5 >> SAVE DATA ARRAY TO MONGODB CLOUD
#save_to_file(data_arr, DESTINATION_PATH)
"""try:
    connect_db.save_data(data_arr, 'facebook')
except:
    print("No data to save!")
"""
# STEP 6 >> PLOT TO MAP & DISPLAY
from geopy.geocoders import Nominatim
import folium
import string

m = folium.Map(location=[-20.2759451, 57.5703566])

for data in data_arr:
    d = data['location']
    if d != "Not found":
        for char in string.punctuation:
            s = d.replace(char, ' ')
        result = ''.join([i for i in s if not i.isdigit()])
        print(result)
    disease = data['diseasetype']
    date = data['date']


    geolocator = Nominatim()
    location = geolocator.geocode(result+ " ,Mauritius")
    print((location.latitude, location.longitude))
    long = location.longitude
    lat = location.latitude


    html="""
        <p>
        Disease alert:"""+disease+""" at """+date +"""
        </p>
    """
    iframe = folium.IFrame(html=html, width=300, height=100)
    popup = folium.Popup(iframe, max_width=1000)

    folium.Marker([lat, long], popup=popup).add_to(m)

m.save("fb_map.html")

# STEP 7 >> LOGOUT FROM FB
close_browser(browser)
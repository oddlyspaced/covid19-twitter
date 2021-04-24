#!/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up Chrome options
option = webdriver.ChromeOptions()
# For ChromeDriver version 79.0.3945.16 or over
# Hide automation
option.add_argument('--disable-blink-features=AutomationControlled')
#Open Browser
driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver',options=option)

# TODO : Replace with custom link
# Reference link
link = "https://twitter.com/search?q=verified+lucknow+%28bed+OR+beds+OR+icu+OR+oxygen+OR+ventilator+OR+ventilators%29+-%22not+verified%22+-%22unverified%22+-%22needed%22+-%22need%22+-%22needs%22+-%22required%22+-%22require%22+-%22requires%22+-%22requirement%22+-%22requirements%22&f=live"

# Opening search results
driver.get(link)

timeline_parent = None
# Trap loop to keep waiting for timeline to load
while (timeline_parent == None):
    try:
        timeline_parent = driver.find_element_by_xpath("//div[@aria-label='Timeline: Search timeline']")
    except:
        pass

# Trap loop to wait for content to load
while (timeline_parent.text != ''):
    time.sleep(1)

#####
# At this point we are mostly sure that the timeline has loaded
#####

# First and only Child of timeline_parent is the actual timeline list element
timeline = (timeline_parent.find_elements_by_xpath("./child::*"))[0]

while True:
    # Children of this element = Root elements of tweets
    tweets = timeline.find_elements_by_xpath("./child::*")
    print(len(tweets))
    time.sleep(3)
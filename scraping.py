from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

def start_login(link="https://twitter.com/i/flow/login"):
    # starting in maximized window for the web driver and keep it open while executing the script
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("--disable-default-apps")
    options.add_experimental_option("detach", True)
    # set up a new Selenium driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options, executable_path="C:\\Users\\IDEAPADGAMING\\Desktop\\pfa\\scraping.py")
    # go to the website
    driver.get(link)
    # wait for the driver to load
    time.sleep(1) 
    #define the login variables
    email=os.environ.get("twitter_email")
    passwd=os.environ.get("twitter_password")
    #entring the login variables
    username=driver.find_element(By.CSS_SELECTOR,'input[autocomplete="username"]')
    username.send_keys(email)
    username.send_keys(Keys.ENTER)
    time.sleep(2)
    password=driver.find_element(By.CSS_SELECTOR,'input[name="password"]')
    password.send_keys(passwd)
    time.sleep(1)
    password.send_keys(Keys.ENTER)
    return driver

def goto(driver,username="Ayoub57576620"):
    # define the username of the profile to scrape and generate its URL 
    URL = "https://twitter.com/" + username 
    driver.get(URL)

def collect_tweets(driver):    
    # wait for the webpage to be loaded
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweet"]')))
    except WebDriverException:
        print("Tweets did not appear! Proceeding after timeout")

    tweet_text=[]
    tweet_id=[]
    art=driver.find_elements(By.TAG_NAME,'article')
    n=len(art)
    for a in range(n):
        articles=driver.find_elements(By.TAG_NAME,'article')
        time.sleep(2)
        tweet_text.append(articles[a].find_element(By.CSS_SELECTOR,'div[data-testid="tweetText"]').text)
        time.sleep(2)
        articles[a].click()
        time.sleep(2.5)
        tweet_id.append(driver.current_url.split('/')[-1])

        time.sleep(2)
        driver.back()
        print(f"yes{a}")
        time.sleep(2.5)
    return tweet_text,tweet_id

#driver=start_login()

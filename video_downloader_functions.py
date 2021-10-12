from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
driver_path ="/Users/RyRy/Desktop/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("headless")
browser = webdriver.Chrome(executable_path=driver_path,options=options)


def site_login_cookie():
    options.add_argument("--headless")
    cookie_value = "mn7agcb1671srn2obdlehim7r5" #Will be input later on
    #Stand in URL
    url = "https://isis.tu-berlin.de/mod/videoservice/view.php/cm/1063983/video/58604/view"
    cookie = {'domain': 'isis.tu-berlin.de', 'httpOnly': True, 'name': 'MoodleSession', 'path': '/', 'sameSite': 'None',
              'secure': True, 'value': cookie_value}
    browser.get("https://isis.tu-berlin.de/mod/videoservice/view.php/cm/1063983/video/58604/view")
    browser.delete_cookie("MoodleSession")
    browser.add_cookie(cookie)
    browser.refresh()
    time.sleep(1)
def site_login_personal():
    #url = input("Input the URL of the ISIS-Page containing the Video: ")
    #Stand In Url
    username_input = "iceomatic"
    password_input = "Ic30ma71c7575!"
    url = "https://isis.tu-berlin.de/mod/videoservice/view.php/cm/1063983/video/58604/view"
    browser.get("https://isis.tu-berlin.de/mod/videoservice/view.php/cm/1063983/video/58604/view")
    time.sleep(0.5)
    browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/section/div/div[3]/div/div/div/div/div[1]/div/form").click()
    username = browser.find_element_by_id("username")
    password = browser.find_element_by_id("password")
    username.send_keys(username_input)
    password.send_keys(password_input)
    browser.find_element_by_id("login-button").click()
    browser.refresh()
    time.sleep(1)

def url_finder():
    url = browser.find_element_by_tag_name("video").get_attribute("src")
    browser.close()
    print(url)
site_login_personal()
url_finder()



import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
import json


driver_path ="chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("headless")
browser = webdriver.Chrome(executable_path=driver_path,options=options)

session_cookie = {}

def site_url():
    #Stand in Url
    global url
    url = "https://isis.tu-berlin.de/"
    #url = input("Input the URL of the ISIS-Page containing the Video: ")
    browser.get(url)
    time.sleep(1)

def manual_cookie():
    global session_cookie
    session_cookie = {'domain': 'isis.tu-berlin.de', 'httpOnly': True, 'name': 'MoodleSession', 'path': '/', 'sameSite': 'None',
              'secure': True, 'value': ''}
    ###Stand In Cookie
    #session_cookie['value'] = "r0nl8p7qoivk16na5pdn8b0ev4"
    ###
    check = input("Would you like to (a)utomatically or (m)anually add the session cookie? (a/m) ")
    if check == "m":
        session_cookie['value'] = input("Enter the value of the \"MoodleSession\" cookie: ")
    if check == "a":
        pass

def site_login():
    global session_cookie
    global url
    if session_cookie["value"] == "":
        ###Stand In Details
        username_input = "iceomatic"
        password_input = ""
        ###
        print("Attempting to login with your details....")
        browser.find_element_by_class_name("eupopup-buttons").click()
        browser.find_element_by_id("shibbolethbutton").click()
        time.sleep(0.5)
        #browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/section/div/div[3]/div/div/div/div/div[1]/div/form").click()
        username = browser.find_element_by_id( "username")
        password = browser.find_element_by_id( "password")
        username.send_keys(username_input)
        password.send_keys(password_input)
        browser.find_element_by_id("login-button").click()
        print("Login Successful!")
        session_cookie = browser.get_cookie("MoodleSession")
        browser.delete_cookie("MoodleSession")
        browser.add_cookie(session_cookie)
    if session_cookie['value'] != "":
        browser.delete_cookie("MoodleSession")
        browser.add_cookie(session_cookie)
video_sites = []
def video_site_fetch():
    global video_sites
    with open("videos_to_download.txt", "r") as f:
        for link in f:
            video_sites.append(link)
    browser.get(video_sites[0])
    time.sleep(1)

global video_src_unlocked
def url_finder():
    global video_src_unlocked
    global video_sites
    for link in video_sites:
        browser.get(link)
        time.sleep(0.2)
        video_src_locked = browser.find_element_by_tag_name("video").get_attribute("src")
        video_name = browser.find_element_by_class_name("video-view").find_element_by_tag_name("h3").text
        browser.get(video_src_locked)
        video_src_unlocked = browser.current_url
        with open("names_and_links.txt", "a") as file:
            vid_info = {video_name:video_src_unlocked}
            file.write(json.dumps(vid_info)+"\n")
        print(f"Video source url found and named: {video_name}")
    browser.quit()
def directory_creation():
    pass
def video_downloader():
    file_name ="Test 1.mp4"
    r = requests.get(video_src_unlocked, stream= True)
    with open(file_name,"wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)

    pass

site_url()
manual_cookie()
site_login()
video_site_fetch()
url_finder()
#video_downloader()

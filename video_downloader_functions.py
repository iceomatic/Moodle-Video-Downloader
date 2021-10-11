from bs4 import BeautifulSoup
import requests
import os
import lxml


def url_finder():
    url = input("Input the URL of the ISIS-Page containing the Video: ")
    url_text = requests.get(url).text
    soup = BeautifulSoup(url_text, "lxml")
    video_url_snippet = soup.find()
    print(soup)
url_finder()
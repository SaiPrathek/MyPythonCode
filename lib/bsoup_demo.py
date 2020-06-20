# Program to demonstrate BeautifulSoup

from bs4 import BeautifulSoup
import requests

resp = requests.get("http://www.srikanthtechnologies.com/rss.xml")

soup = BeautifulSoup(resp.text, 'xml')
for item in soup.find_all("item"):
    print(item.find("title").get_text())

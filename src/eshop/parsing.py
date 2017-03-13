import requests
from bs4 import BeautifullSoup

url = 'http://www.mvideo.ru/'

def get_html(url):
    r = requests.get(url)
    return r.text

def get_links(html):
    soup = BeautifullSoup(html, 'lxml')
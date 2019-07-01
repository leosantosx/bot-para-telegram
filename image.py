import json
import itertools
import requests
from bs4 import BeautifulSoup
import telepot


def get_soup(url, header):
    response = requests.get(url, headers=header).text
    return BeautifulSoup(response, 'html.parser')

def get_query_url(query):
    return "https://www.google.co.in/search?q=%s&source=lnms&tbm=isch" % query

def extract_images_from_soup(soup):
    image_elements = soup.find_all("div", {"class": "rg_meta"})
    metadata_dicts = (json.loads(e.text) for e in image_elements)
    link_type_records = ((d["ou"], d["ity"]) for d in metadata_dicts)
    return link_type_records

def extract_images(query, num_images):
    header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    url = get_query_url(query)
    soup = get_soup(url, header)
    link_type_records = extract_images_from_soup(soup)
    return itertools.islice(link_type_records, num_images)

def run(query, num_images):
    query = query.replace(' ','+') 
    images = extract_images(query, num_images)
    lista_photos = []
    for photo in images:
        lista_photos.append(photo[0]) 
    return lista_photos




import requests
from bs4 import BeautifulSoup
import os
import urllib.request

class WikipediaScraper:
    def __init__(self, **kwargs) -> None:
        self.lang = kwargs.get("lang", "fr")

    def get_homepage(self):
        response = self.get_http_response(f"https://{self.lang}.wikipedia.org")
        bs = BeautifulSoup(response.content, 'html.parser')
        return self.get_heading(bs)
    
    def get_random_article(self):
        response = self.get_http_response(f"https://{self.lang}.wikipedia.org/wiki/Special:Random")
        print(f"Random article: {response.url}")
        bs = BeautifulSoup(response.content, 'html.parser')
        return self.get_heading(bs)

    def get_http_response(self, path):
        response = requests.get(url=path)
        if response.status_code == 200:
            return response
        else:
            print(f"Error getting {path} (status code: {response.status_code})")

    def download_main_image(self, path, save_path):
        response = self.get_http_response(path)
        bs = BeautifulSoup(response.content, 'html.parser')
        img_src = self.find_img_src(bs)
        if img_src != None:
            self.download_image_source(img_src, save_path)
        else:
            print("Couldn't find the image.")

    def download_image_source(self, path, outpath):
        img = urllib.request.urlopen(path)
        with open(outpath, 'wb') as f:
            f.write(img.read())

    def find_img_src(self, bs):
        img_box = bs.find_all(class_="infobox-image")
        img_element = img_box[0].find_all("img")[0]
        return "https:" + img_element.get("src")

    def get_heading(self, bs):
        heading_element = bs.find(id = "firstHeading")
        return heading_element.string


scraper = WikipediaScraper(lang = "fr")

print(scraper.get_homepage())
print(scraper.get_random_article())

scraper.download_main_image(
    "https://en.wikipedia.org/wiki/Pablo_Picasso", 
    os.path.join(os.getcwd(), "image-dl.jpg")
)

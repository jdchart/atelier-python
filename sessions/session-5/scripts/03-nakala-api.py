import requests
import utils
import os

class NakalaAPI:
    def __init__(self, **kwargs) -> None:
        self.nakala_api_prefix = kwargs.get("nakala_api_prefix", "https://api.nakala.fr/")
        self.nakala_prefix = kwargs.get("nakala_prefix", "https://www.nakala.fr/")
        
    def get_data(self, url):
        id = self.url_to_id(url)
        response = requests.get(f"{self.nakala_api_prefix}datas/{id}")
        return response.json()
    
    def search(self, terms, size = 25):
        term_string = self.get_term_string(terms)
        response = requests.get(f"{self.nakala_api_prefix}search?q={term_string}&fq=&facet=&order=relevance&page=1&size={str(size)}")
        return response.json()

    def get_term_string(self, terms):
        ret = ""
        for item in terms:
            if " " in item:
                item_split = item.split(" ")
                for subitem in item_split:
                    ret = ret + subitem + "%20"
            else:
                ret = ret + item + "%20"
        return ret[:-3]

    def url_to_id(self, url):
        return url.split(self.nakala_prefix)[1]


nakala = NakalaAPI()
utils.write_json(os.path.join(os.getcwd(), "nakala_out.json"), nakala.get_data("https://www.nakala.fr/10.34847/nkl.def2v5a2"))

search = nakala.search(["carte monde", "iiif"])
utils.write_json(os.path.join(os.getcwd(), "nakala_search_out.json"), search)
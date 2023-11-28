import requests

class NakalaItem:
    def __init__(self, url, **kwargs) -> None:
        self.url = url
        self.nakala_prefix = kwargs.get("nakala_prefix", "https://api.nakala.fr/")
        self.can_process = False
        self.identifier = None
        self.fileIdentifier = None
        self.format = None
        self.type = None
        self.width = None
        self.height = None
        self.extension = None

        self.parse_url()

    def parse_url(self):
        # Determine if is data source (can process) or embedded (cannot process):
        urlSplit = []
        try:
            urlSplit = self.url.split(self.nakala_prefix)[1].split("data/")[1].split('/')
            self.can_process = True
        except:
            try:
                urlSplit = self.url.split(self.nakala_prefix)[1].split("embed/")[1].split('/')
                self.can_process = False
            except:
                self.can_process = False
        
        # If can process, get direct file link:
        if self.can_process:
            self.identifier = ""
            for i in range(len(urlSplit) - 1):
                self.identifier = self.identifier + "/" + urlSplit[i]
            
            data_req = self.data_request()
            self.fileIdentifier = data_req["files"][0]["sha1"]
            self.format = data_req["files"][0]["mime_type"]
            self.type = self.format.split("/")[0].capitalize()
            self.extension = data_req["files"][0]["extension"]

            #if self.type == "Image":
            #    iiif_req = self.iiif_info_request()
            #    self.width = iiif_req["width"]
            #    self.height = iiif_req["height"]
    
    def data_request(self):
        r = requests.get(self.nakala_prefix + "datas" + self.identifier)
        return r.json()
    
    def iiif_info_request(self):
        r = requests.get(self.nakala_prefix + "iiif" + self.identifier + '/' + self.fileIdentifier + "/info.json")
        return r.json()
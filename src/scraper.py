__app_name__ = "LocalLead AI Pro"
__author__ = "OSSIQN"
__website__ = "https://ossiqn.com.tr"
__github__ = "https://github.com/ossiqn"

import requests
import time
from src.config import Config

class MapsScraper:
    def __init__(self):
        self.api_key = Config.GMAPS_API_KEY
        self.base_url = "https://maps.googleapis.com/maps/api/place"

    def search_businesses(self, query, max_results):
        results = []
        url = f"{self.base_url}/textsearch/json"
        params = {"query": query, "key": self.api_key}
        
        while len(results) < max_results:
            response = requests.get(url, params=params)
            if response.status_code != 200:
                break
                
            data = response.json()
            results.extend(data.get("results", []))
            
            next_page_token = data.get("next_page_token")
            if not next_page_token or len(results) >= max_results:
                break
                
            time.sleep(2)
            params = {"pagetoken": next_page_token, "key": self.api_key}
            
        return results[:max_results]

    def get_business_details(self, place_id):
        url = f"{self.base_url}/details/json"
        params = {
            "place_id": place_id,
            "fields": "name,website,formatted_phone_number,rating",
            "key": self.api_key
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json().get("result", {})
        return {}
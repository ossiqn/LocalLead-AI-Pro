__app_name__ = "LocalLead AI Pro"
__author__ = "OSSIQN"
__website__ = "https://ossiqn.com.tr"
__github__ = "https://github.com/ossiqn"

import requests
from bs4 import BeautifulSoup
import re
from src.config import Config

class SeoAnalyzer:
    @staticmethod
    def analyze_website(url):
        result = {"status": "failed", "score": 100, "issues": [], "cms": "Unknown", "emails": [], "socials": []}
        
        proxies = {"http": Config.PROXY_URL, "https": Config.PROXY_URL} if Config.USE_PROXY and Config.PROXY_URL else None
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
        
        try:
            response = requests.get(url, timeout=15, headers=headers, proxies=proxies)
            if response.status_code != 200:
                result["reason"] = "http_error"
                return result
                
            html = response.text.lower()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            if "wp-content" in html or "wp-includes" in html:
                result["cms"] = "WordPress"
            elif "cdn.shopify.com" in html:
                result["cms"] = "Shopify"
            elif "wix.com" in html:
                result["cms"] = "Wix"
                
            email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
            result["emails"] = list(set(re.findall(email_pattern, response.text)))
            
            for a_tag in soup.find_all('a', href=True):
                href = a_tag['href']
                if "instagram.com" in href or "facebook.com" in href or "linkedin.com" in href:
                    result["socials"].append(href)
            result["socials"] = list(set(result["socials"]))
            
            if not soup.title or not soup.title.string:
                result["score"] -= 20
                result["issues"].append("missing_title")
                
            if not soup.find("meta", attrs={"name": "description"}):
                result["score"] -= 20
                result["issues"].append("missing_meta_desc")
                
            if not soup.find_all("h1"):
                result["score"] -= 15
                result["issues"].append("missing_h1")
                
            if "viewport" not in html:
                result["score"] -= 30
                result["issues"].append("not_mobile_optimized")
                
            result["status"] = "success"
            return result
            
        except Exception:
            result["reason"] = "timeout_or_blocked"
            return result
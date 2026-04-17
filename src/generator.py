__app_name__ = "LocalLead AI Pro"
__author__ = "OSSIQN"
__website__ = "https://ossiqn.com.tr"
__github__ = "https://github.com/ossiqn"

import requests
from src.config import Config

class PitchGenerator:
    def __init__(self):
        self.api_key = Config.OPENAI_API_KEY
        self.url = "https://api.openai.com/v1/chat/completions"

    def generate_pitch(self, business_name, analyzer_data):
        if not self.api_key:
            return ""
            
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        issues_text = ", ".join(analyzer_data.get('issues', []))
        cms = analyzer_data.get('cms', 'Unknown')
        
        prompt = f"Business: {business_name}\nCMS: {cms}\nIssues: {issues_text}\nWrite a highly personalized, high-converting cold email offering web development/SEO services fixing these exact issues. Do not use placeholders. Be direct and professional."
        
        payload = {
            "model": "gpt-4",
            "messages": [
                {"role": "system", "content": "You are a top-tier digital agency sales executive."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7
        }
        
        try:
            response = requests.post(self.url, headers=headers, json=payload)
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            return ""
        except Exception:
            return 
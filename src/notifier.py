__app_name__ = "LocalLead AI Pro"
__author__ = "OSSIQN"
__website__ = "https://ossiqn.com.tr"
__github__ = "https://github.com/ossiqn"

import requests
from src.config import Config

class TelegramNotifier:
    @staticmethod
    def send_alert(message):
        if not Config.TELEGRAM_BOT_TOKEN or not Config.TELEGRAM_CHAT_ID:
            return False
            
        url = f"https://api.telegram.org/bot{Config.TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": Config.TELEGRAM_CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }
        
        try:
            requests.post(url, json=payload, timeout=5)
            return True
        except Exception:
            return False
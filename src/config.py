__app_name__ = "LocalLead AI Pro"
__author__ = "OSSIQN"
__website__ = "https://ossiqn.com.tr"
__github__ = "https://github.com/ossiqn"

import os

class Config:
    TARGET_QUERY = os.getenv("TARGET_QUERY", "plumbers in London")
    MAX_RESULTS = int(os.getenv("MAX_RESULTS", 50))
    THREAD_COUNT = int(os.getenv("THREAD_COUNT", 5))
    
    USE_PROXY = os.getenv("USE_PROXY", "false").lower() == "true"
    PROXY_URL = os.getenv("PROXY_URL", "")
    
    GMAPS_API_KEY = os.getenv("GMAPS_API_KEY", "")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    
    SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
    SMTP_USER = os.getenv("SMTP_USER", "")
    SMTP_PASS = os.getenv("SMTP_PASS", "")
    
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
    
    DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "leads.db")
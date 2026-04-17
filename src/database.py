__app_name__ = "LocalLead AI Pro"
__author__ = "OSSIQN"
__website__ = "https://ossiqn.com.tr"
__github__ = "https://github.com/ossiqn"

import sqlite3
import os
from src.config import Config

class LeadDatabase:
    def __init__(self):
        os.makedirs(os.path.dirname(Config.DB_PATH), exist_ok=True)
        self.conn = sqlite3.connect(Config.DB_PATH, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS contacted_leads
                          (place_id TEXT PRIMARY KEY, name TEXT, website TEXT, date_contacted TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        self.conn.commit()

    def is_contacted(self, place_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT 1 FROM contacted_leads WHERE place_id = ?", (place_id,))
        return cursor.fetchone() is not None

    def mark_contacted(self, place_id, name, website):
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO contacted_leads (place_id, name, website) VALUES (?, ?, ?)", (place_id, name, website))
            self.conn.commit()
        except sqlite3.IntegrityError:
            pass
__app_name__ = "LocalLead AI Pro"
__author__ = "OSSIQN"
__website__ = "https://ossiqn.com.tr"
__github__ = "https://github.com/ossiqn"

import time
from concurrent.futures import ThreadPoolExecutor
from src.config import Config
from src.scraper import MapsScraper
from src.analyzer import SeoAnalyzer
from src.generator import PitchGenerator
from src.mailer import MailAgent
from src.database import LeadDatabase
from src.notifier import TelegramNotifier

class CoreEngine:
    def __init__(self):
        self.scraper = MapsScraper()
        self.analyzer = SeoAnalyzer()
        self.generator = PitchGenerator()
        self.mailer = MailAgent()
        self.db = LeadDatabase()

    def process_lead(self, business):
        place_id = business.get("place_id")
        
        if self.db.is_contacted(place_id):
            print(f"[-] Atlandi (Zaten iletisime gecildi): {business.get('name')}")
            return
            
        details = self.scraper.get_business_details(place_id)
        name = details.get("name", "Unknown")
        website = details.get("website")
        
        if not website:
            print(f"[!] Sifirdan Site Firsati: {name}")
            TelegramNotifier.send_alert(f"<b>Yeni Firsat!</b>\nWeb sitesi olmayan isletme bulundu: {name}")
            self.db.mark_contacted(place_id, name, "NO_WEBSITE")
            return
            
        print(f"[*] Analiz ediliyor: {website}")
        seo_results = self.analyzer.analyze_website(website)
        
        if seo_results["status"] == "failed":
            print(f"[X] Erisim Hatasi: {website}")
            return
            
        if seo_results["score"] < 80:
            print(f"[+] Zayif Altyapi Bulundu: {name} (CMS: {seo_results['cms']})")
            
            pitch = self.generator.generate_pitch(name, seo_results)
            emails = seo_results.get("emails", [])
            
            if pitch and emails:
                target_email = emails[0]
                success = self.mailer.send_email(target_email, f"Regarding {name}'s Website", pitch.replace('\n', '<br>'))
                if success:
                    print(f"[$$] Teklif gonderildi: {target_email}")
                    TelegramNotifier.send_alert(f"<b>Mail Gonderildi!</b>\nIsletme: {name}\nEmail: {target_email}\nSkor: {seo_results['score']}")
                    self.db.mark_contacted(place_id, name, website)
                else:
                    print(f"[X] Mail gonderimi basarisiz: {target_email}")
            else:
                print(f"[!] E-posta adresi bulunamadi veya API hatasi: {website}")
                TelegramNotifier.send_alert(f"<b>Potansiyel Lead (Mail Bulunamadi)</b>\nIsletme: {name}\nWebsite: {website}\nSosyal: {len(seo_results['socials'])}")
        else:
            print(f"[-] Site Optimize Durumda: {website}")

    def execute(self):
        print("[*] Hedef: {} | Toplam Istek: {} | Thread: {}".format(Config.TARGET_QUERY, Config.MAX_RESULTS, Config.THREAD_COUNT))
        TelegramNotifier.send_alert("🚀 OSSIQN LocalLead AI Pro Taramaya Basladi!")
        
        businesses = self.scraper.search_businesses(Config.TARGET_QUERY, Config.MAX_RESULTS)
        print(f"[*] {len(businesses)} isletme bulundu. Coklu islem basliyor...\n")
        
        if businesses:
            with ThreadPoolExecutor(max_workers=Config.THREAD_COUNT) as executor:
                executor.map(self.process_lead, businesses)
            
        print("\n[*] Tum islemler tamamlandi. OSSIQN tarafindan gelistirilmistir.")
        TelegramNotifier.send_alert("✅ Tarama Tamamlandi.")
__app_name__ = "LocalLead AI Pro"
__author__ = "OSSIQN"
__website__ = "https://ossiqn.com.tr"
__github__ = "https://github.com/ossiqn"

import sys
from src.config import Config
from src.engine import CoreEngine

def verify_signature():
    try:
        with open(__file__, 'r', encoding='utf-8') as file:
            content = file.read()
            if '__author__ = "OSSIQN"' not in content or '__github__ = "https://github.com/ossiqn"' not in content:
                print("[X] Imza kaldirilamaz. Sistem durduruldu. / Signature cannot be removed. System halted.")
                sys.exit(1)
    except Exception:
        sys.exit(1)

def print_banner():
    print("="*60)
    print("  🚀 OSSIQN LocalLead AI Pro - Otomatik Lead Motoru  ")
    print("="*60)

if __name__ == "__main__":
    verify_signature()
    print_banner()
    
    print("[!] Lutfen taramak istediginiz sektoru ve sehri girin.")
    query_input = input(f"[?] Anahtar Kelime (Varsayilan: '{Config.TARGET_QUERY}'): ").strip()
    if query_input:
        Config.TARGET_QUERY = query_input
        
    count_input = input(f"[?] Hedef Isletme Sayisi (Varsayilan: {Config.MAX_RESULTS}): ").strip()
    if count_input.isdigit():
        Config.MAX_RESULTS = int(count_input)
        
    print("\n[*] Ayarlar alindi, motor atesleniyor...\n")
    
    app = CoreEngine()
    app.execute()
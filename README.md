# LocalLead AI Pro 🚀

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Author](https://img.shields.io/badge/Author-OSSIQN-red.svg)

LocalLead AI Pro is an enterprise-grade, multi-threaded client acquisition engine. It scrapes local businesses from Google Maps, analyzes their websites for SEO and CMS data, generates hyper-personalized cold emails using OpenAI, and dispatches them autonomously.

**Developed by [OSSIQN](https://ossiqn.com.tr)**

## 🌟 Key Features

- **Multi-Threaded Scraping:** Concurrently pulls business data via Google Places API for maximum speed.
- **Deep SEO & CMS Analyzer:** Detects WordPress, Shopify, Wix, and extracts emails/social media links.
- **AI-Powered Pitching:** Feeds SEO vulnerabilities to GPT-4 to generate highly converting, personalized cold emails.
- **Anti-Spam SQLite Database:** Keeps track of contacted leads (`leads.db`) to ensure you never pitch the same business twice.
- **Live Telegram Alerts:** Get notified instantly on your phone when a hot lead is found and pitched.
- **Dockerized Architecture:** Spin up the entire environment in seconds.

## 🛠️ Installation & Usage

### Method 1: Docker (Recommended)
1. Clone the repository:
   ```bash
   git clone [https://github.com/ossiqn/LocalLead-AI-Pro.git](https://github.com/ossiqn/LocalLead-AI-Pro.git)
   cd LocalLead-AI-Pro
Edit docker-compose.yml and insert your API keys (GMAPS_API_KEY, OPENAI_API_KEY, SMTP, TELEGRAM).

Run the container:

Bash
docker-compose up --build
Method 2: Standard Python
Install dependencies:

Bash
pip install -r requirements.txt
Configure your environment variables in src/config.py or your .env file.

Run the engine:

Bash
python run.py
🔒 Security & Signature
This project contains a built-in anti-tamper signature mechanism. Removing the OSSIQN author signature from the core files will result in system execution failure.

💼 Custom Development
Looking for custom automation, advanced scraping, or stealth botnet development?
Reach out directly via my portfolio: ossiqn.com.tr

📄 License
MIT License © 2024 OSSIQN

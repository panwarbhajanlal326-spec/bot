import os
import time
import requests
from flask import Flask

# Flask server taaki Render isko active rakhe
app = Flask('')

@app.route('/')
def home():
    return "Panwar Telegram Bot is Alive and Running 24/7! 🚀"

def run_web():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

# Telegram Bot ki settings
TOKEN = "8385021216:AAFFcFH-9xEiyx8X7UlW39pZokOSPykNUIY" 
URL = f"https://api.telegram.org/bot{TOKEN}/"

def check_telegram_messages():
    offset = None
    print("Telegram Bot Started Successfully and listening for messages...")
    
    while True:
        try:
            # Telegram se messages check karne ka tareeqa (Polling)
            url = URL + "getUpdates?timeout=30"
            if offset:
                url += f"&offset={offset}"
                
            response = requests.get(url, timeout=40)
            data = response.json()
            
            if "result" in data:
                for result in data["result"]:
                    offset = result["update_id"] + 1
                    
                    if "message" in result:
                        chat_id = result["message"]["chat"]["id"]
                        text = result["message"].get("text", "")
                        print(Stimuli: f"Message aaya: {text}")
                        
                        # User ko reply bhejna
                        send_message(chat_id, "Ram Ram! Main Panwar Bot hu, aapne kya likha: " + text)
                        
        except Exception as e:
            print("Error aaya:", e)
            time.sleep(5)

def send_message(chat_id, text):
    url = URL + f"sendMessage?chat_id={chat_id}&text={text}"
    requests.get(url)

if __name__ == "__main__":
    import threading
    # Web server aur Telegram bot ko ek sath chalane ke liye thread
    t = threading.Thread(target=run_web)
    t.start()
    
    check_telegram_messages()

import os
import time
from flask import Flask

# Chota sa web server taaki cloud hosting (Render) isko active rakhe
app = Flask('')

@app.route('/')
def home():
    return "Panwar Bot is Alive and Running 24/7! 🚀"

def run_web():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

# Yahan aapka asli bot ka kaam chalega
def main_bot():
    print("Panwar Bot Started Successfully!")
    while True:
        print("Bot is working background mein... Ping!")
        # Aap yahan apna Telegram ya koi bhi bot ka code daal sakti hain
        time.sleep(30) # Har 30 second baad print karega

if __name__ == "__main__":
    import threading
    # Web server aur Bot ko ek sath chalane ke liye thread
    t = threading.Thread(target=run_web)
    t.start()
    
    main_bot()

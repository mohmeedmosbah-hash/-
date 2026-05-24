import requests
import os

token = os.environ["BOT_TOKEN"]
chat = os.environ["CHAT_ID"]

url = f"https://api.telegram.org/bot{token}/sendMessage"

data = {
    "chat_id": chat,
    "text": "✅ نجح الاختبار: البوت متصل بتيليجرام"
}

r = requests.post(url, data=data)

print(r.status_code)
print(r.text)

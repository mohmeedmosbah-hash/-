import requests
import os

token = os.environ["BOT_TOKEN"]
chat = os.environ["CHAT_ID"]

response = requests.post(
    f"https://api.telegram.org/bot{token}/sendMessage",
    data={
        "chat_id": chat,
        "text": "✅ اختبار البوت من GitHub"
    }
)

print(response.status_code)
print(response.text)

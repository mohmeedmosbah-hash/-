import requests

BOT_TOKEN = "ضع_التوكن_هنا"
CHAT_ID = "ضع_رقم_الشات_هنا"

response = requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": "✅ نجح الاتصال من GitHub"
    }
)

print(response.status_code)
print(response.text)

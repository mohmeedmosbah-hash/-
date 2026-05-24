import os

token = os.environ.get("BOT_TOKEN")

print("TOKEN LENGTH:", len(token) if token else "None")

if token:
    print("FIRST:", token[:10])
    print("LAST:", token[-5:])

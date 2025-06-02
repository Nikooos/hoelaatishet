import os
from dotenv import load_dotenv
from atproto import Client
from datetime import datetime
from zoneinfo import ZoneInfo

load_dotenv()

BLSKY_HANDLE = os.getenv('BLSKY_HANDLE')
BLSKY_APP_PASSWORD = os.getenv('BLSKY_APP_PASSWORD')

now = datetime.now()
now = datetime.now(ZoneInfo("Europe/Amsterdam"))
current_hour = now.hour
current_minute = now.minute

if 5 <= current_hour < 12:
    greeting = "Goedemorgen!"
elif 12 <= current_hour < 18:
    greeting = "Goedemiddag!"
elif 18 <= current_hour < 22:
    greeting = "Goedenavond!"
else:
    greeting = "Goedenacht!"
print(greeting + " Het is nu " + str(current_hour) + ":" + current_minute + " uur")

post_text = f"{greeting} Het is nu {current_hour}:{current_minute} uur #hoelaatishet"

bsky_client = Client()
bsky_client.login(BLSKY_HANDLE, BLSKY_APP_PASSWORD)

bsky_client.send_post(text=post_text)
print("Geplaatst op Bluesky ", str(current_hour))
import os
from dotenv import load_dotenv
from atproto import Client
from datetime import datetime
from zoneinfo import ZoneInfo

load_dotenv()

BLSKY_HANDLE = os.environ.get('BLSKY_HANDLE')
BLSKY_APP_PASSWORD = os.environ.get('BLSKY_APP_PASSWORD')

now = datetime.now()
now = datetime.now(ZoneInfo("Europe/Amsterdam"))
current_hour = now.hour

print("Het is nu " + str(current_hour) + ":00 uur")

post_text = f"Het is nu {current_hour}:00 uur #hoelaatishet"

bsky_client = Client()
bsky_client.login(BLSKY_HANDLE, BLSKY_APP_PASSWORD)

bsky_client.send_post(text=post_text)
print("Geplaatst op Bluesky ", str(current_hour))
import os
from dotenv import load_dotenv
from atproto import Client, RichText
from datetime import datetime
from zoneinfo import ZoneInfo

load_dotenv()

BLSKY_HANDLE = os.getenv('BLSKY_HANDLE')
BLSKY_APP_PASSWORD = os.getenv('BLSKY_APP_PASSWORD')

now = datetime.now()
now = datetime.now(ZoneInfo("Europe/Amsterdam"))
current_hour = now.hour
current_minute = now.minute
minute_str = f"{current_minute:02d}"

if 5 <= current_hour < 12:
    greeting = "Goedemorgen!"
elif 12 <= current_hour < 18:
    greeting = "Goedemiddag!"
elif 18 <= current_hour < 22:
    greeting = "Goedenavond!"
else:
    greeting = "Goedenacht!"
print(greeting + " Het is nu " + str(current_hour) + ":" + minute_str + " uur")

post_text = f"{greeting} Het is nu {current_hour}:{minute_str} uur #hoelaatishet"

# Verbind met Bluesky
client = Client()
client.login(BLSKY_HANDLE, BLSKY_APP_PASSWORD)

# Gebruik RichText helper om automatisch facets te genereren
rt = RichText(text=post_text)
rt.detect_facets(client)  # detecteert hashtags en links

# Verstuur de post mét facet
client.send_post(text=rt.text, facets=rt.facets)
print("Geplaatst op Bluesky ", str(current_hour))
import os
from dotenv import load_dotenv
from atproto import Client
from datetime import datetime
from zoneinfo import ZoneInfo
import tweepy

load_dotenv()

BLSKY_HANDLE = os.getenv('BLSKY_HANDLE')
BLSKY_APP_PASSWORD = os.getenv('BLSKY_APP_PASSWORD')

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

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

hashtag = "#hoelaatishet"
start_index = post_text.encode("utf-8").index(hashtag.encode("utf-8"))
end_index = start_index + len(hashtag.encode("utf-8"))


facets = [{
      "index": {
        "byteStart": start_index,
        "byteEnd": end_index
      },
      "features": [{
        "$type": "app.bsky.richtext.facet#tag",
        "tag": "hoelaatishet"
      }]
}]

# bsky_client = Client()
# bsky_client.login(BLSKY_HANDLE, BLSKY_APP_PASSWORD)

# bsky_client.send_post(text=post_text, facets=facets)
# print("✅ Geplaatst op Bluesky ", str(current_hour))

# # only post tweets on even hours
# if current_hour % 2 != 0:
#     print(f"⏸️ Sla over: {current_hour} is een oneven uur.")
#     exit(0)

client = tweepy.Client(
    bearer_token=TWITTER_BEARER_TOKEN,
    consumer_key=TWITTER_API_KEY,
    consumer_secret=TWITTER_API_SECRET,
    access_token=TWITTER_ACCESS_TOKEN,
    access_token_secret=TWITTER_ACCESS_SECRET
)


print("bearer_token:", TWITTER_BEARER_TOKEN)
print("consumer_key:", TWITTER_API_KEY)
print("consumer_secret:", TWITTER_API_SECRET)
print("access_token:", TWITTER_ACCESS_TOKEN)
print("access_token_secret:", TWITTER_ACCESS_SECRET)

response = client.create_tweet(text=post_text)
print("✅ Tweet geplaatst! ID:", response.data['id'])
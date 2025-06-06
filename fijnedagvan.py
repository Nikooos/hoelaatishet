import os
import json
from dotenv import load_dotenv
from atproto import Client
from datetime import datetime
from zoneinfo import ZoneInfo

load_dotenv()

BLSKY_FDV_HANDLE = os.getenv('BLSKY_FDV_HANDLE')
BLSKY_FDV_APP_PASSWORD = os.getenv('BLSKY_FDV_APP_PASSWORD')

# Tijd instellen
now = datetime.now(ZoneInfo("Europe/Amsterdam"))
today_key = now.strftime("%d-%m")

# Laad de JSON met dagen
with open("fdv.json", "r", encoding="utf-8") as f:
    dagen_data = json.load(f)

# Zoek dagen voor vandaag
vieringen = dagen_data.get(today_key, [])

if not vieringen:
    print(f"❌ Geen speciale dagen op {today_key}")
    exit(0)

# Login Bluesky client
bsky_client = Client()
bsky_client.login(BLSKY_FDV_HANDLE, BLSKY_FDV_APP_PASSWORD)

# Post per viering
for dag in vieringen:
    naam = dag["naam"]
    beschrijving = dag.get("beschrijving", "")
    post_text = f"Het is vandaag {naam}\n{beschrijving}\n#fijnedagvan"

    # Bluesky facet maken voor de hashtag
    hashtag = "#fijnedagvan"
    start_index = post_text.encode("utf-8").index(hashtag.encode("utf-8"))
    end_index = start_index + len(hashtag.encode("utf-8"))
    facets = [{
        "index": {
            "byteStart": start_index,
            "byteEnd": end_index
        },
        "features": [{
            "$type": "app.bsky.richtext.facet#tag",
            "tag": "fijnedagvan"
        }]
    }]

    # Post op Bluesky
    bsky_client.send_post(text=post_text, facets=facets)
    print(f"✅ Geplaatst op Bluesky: {naam}")



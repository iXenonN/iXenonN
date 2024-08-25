import os
import firebase_admin
from firebase_admin import credentials, storage

firebase_json_path = "/tmp/firebase_key.json"
with open(firebase_json_path, "w") as f:
    f.write(os.environ["FIREBASE_JSON"])

cred = credentials.Certificate(firebase_json_path)
firebase_admin.initialize_app(cred, {"storageBucket": "yt-music-profile.appspot.com"})

bucket = storage.bucket()
blob = bucket.blob("listening-on-ytmusic.svg")

public_url = blob.generate_signed_url(datetime.timedelta(seconds=300), method="GET")
print("SVG dosyasının URL'si:", public_url)

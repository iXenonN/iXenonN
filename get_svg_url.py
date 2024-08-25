import datetime
import os
import firebase_admin
from firebase_admin import credentials, storage

# Define the path for the Firebase service account JSON key
firebase_json_path = "/tmp/firebase_key.json"

# Write the Firebase JSON key from the environment variable to a file
with open(firebase_json_path, "w") as f:
    f.write(os.environ["FIREBASE_JSON"])

# Initialize the Firebase app with the service account key and storage bucket
cred = credentials.Certificate(firebase_json_path)
firebase_admin.initialize_app(cred, {"storageBucket": "yt-music-profile.appspot.com"})

# Get the Firebase storage bucket and the specific SVG file blob
bucket = storage.bucket()
blob = bucket.blob("listening-on-ytmusic.svg")

# Generate a signed URL for the SVG file
public_url = blob.generate_signed_url(datetime.timedelta(seconds=300), method="GET")

# Print the public URL
print("SVG dosyasının URL'si:", public_url)

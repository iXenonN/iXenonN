import firebase_admin
from firebase_admin import credentials, storage

# Initialize Firebase
cred = credentials.Certificate(FIREBASE_JSON)
firebase_admin.initialize_app(cred, {
    'storageBucket': 'yt-music-profile.appspot.com'
})

# Get a reference to the storage bucket
bucket = storage.bucket()

# Specify the SVG file name
blob = bucket.blob('listening-on-yt-music.svg')

# Generate a download URL
svg_url = blob.generate_signed_url(timedelta(minutes=10))

print(f"::set-output name=svg_url::{svg_url}")

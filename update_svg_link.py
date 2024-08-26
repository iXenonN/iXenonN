import time

def get_svg_url_with_timestamp():
    base_url = "https://firebasestorage.googleapis.com/v0/b/yt-music-profile.appspot.com/o/listening-on-ytmusic.svg"
    token = "960b7656-574a-45b0-93ae-3c9823750193"
    timestamp = int(time.time())
    return f"{base_url}?alt=media&token={token}&timestamp={timestamp}"

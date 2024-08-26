import time
import os
import re

def get_svg_url_with_timestamp():
    base_url = "https://firebasestorage.googleapis.com/v0/b/yt-music-profile.appspot.com/o/listening-on-ytmusic.svg"
    token = "960b7656-574a-45b0-93ae-3c9823750193"
    timestamp = int(time.time())
    return f"{base_url}?alt=media&token={token}&timestamp={timestamp}"

readme_path = 'README.md'

new_svg_link = get_svg_url_with_timestamp()
"""
with open(readme_path, 'r') as file:
    content = file.read()

updated_content = re.sub(r'!\[Your SVG\]\(.*\)', f'![Your SVG]({new_svg_link})', content)

with open(readme_path, 'w') as file:
    file.write(updated_content)
"""
print("README.md has been updated with the new SVG link.")

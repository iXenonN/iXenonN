import re

public_url = "https://storage.googleapis.com/what-am-i-listening/listening-on-ytmusic.svg"

with open("README.md", "r") as file:
    readme_content = file.read()

new_readme_content = re.sub(r"!\[SVG Image\]\(.*?\)", f"![SVG Image]({public_url})", readme_content)

with open("README.md", "w") as file:
    file.write(new_readme_content)

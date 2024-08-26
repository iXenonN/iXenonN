import os
import re

def update_readme_with_svg():
    readme_path = 'README.md'

    new_svg_link = "https://firebasestorage.googleapis.com/v0/b/yt-music-profile.appspot.com/o/listening-on-ytmusic.svg?alt=media&token=960b7656-574a-45b0-93ae-3c9823750193"
    with open(readme_path, 'r', encoding='utf-8') as file:
        content = file.read()
    updated_content = re.sub(r'!\[Your SVG\]\(.*\)', f'![Your SVG]({new_svg_link})', content)

    with open(readme_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

    print("README.md has been updated with the new SVG link.")
    
    os.system('git add README.md')
    os.system('git commit -m "Update README with new SVG link"')
    os.system('git push origin main')

    print("Changes have been pushed to GitHub.")

if __name__ == "__main__":
    update_readme_with_svg()

if git diff-index --quiet HEAD --; then
    echo "No changes to commit"
    exit 0
fi

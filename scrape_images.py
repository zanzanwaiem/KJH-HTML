import urllib.request
import re
import os
import glob

base_url = "http://kym1402.dothome.co.kr"
save_dir = r"c:\Users\kym75\Desktop\KJH HTML"
img_dir = os.path.join(save_dir, "images")

if not os.path.exists(img_dir):
    os.makedirs(img_dir)

def download_file(url, save_path):
    try:
        if not os.path.exists(save_path):
            print(f"Downloading {url} ...")
            urllib.request.urlretrieve(url, save_path)
            return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

# Find all html files
html_files = glob.glob(os.path.join(save_dir, "*.html"))
for html_file in html_files:
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Find all <img src="images/...">
    img_links = re.findall(r'src="(images/[^"]+)"', content)
    for link in set(img_links):
        url = f"{base_url}/{link}"
        # We replace / with \ for windows paths, but os.path.normpath handles it.
        save_path = os.path.join(save_dir, os.path.normpath(link))
        download_file(url, save_path)

print("Image scraping finished!")

import urllib.request
import re
import os

base_url = "http://kym1402.dothome.co.kr"
save_dir = r"c:\Users\kym75\Desktop\KJH HTML"

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

def download_file(filename):
    if filename == "index.html":
        url = base_url + "/"
    else:
        url = f"{base_url}/{filename}"
    save_path = os.path.join(save_dir, filename)
    try:
        print(f"Downloading {url} ...")
        urllib.request.urlretrieve(url, save_path)
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

# Download index.html
download_file("index.html")

# Read index.html to find other linked html files
with open(os.path.join(save_dir, "index.html"), "r", encoding="utf-8") as f:
    content = f.read()

# Find href attributes
links = re.findall(r'href="([^"]+\.html)"', content)

for link in set(links):
    if link != "index.html":
        download_file(link)

print("Scraping finished!")

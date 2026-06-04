import glob
import os
import re

save_dir = r"c:\Users\kym75\Desktop\KJH HTML"
html_files = glob.glob(os.path.join(save_dir, "*.html"))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace href="setup-finish.html" or any other non-index.html link for the back button
    # The back button has class="back-btn" and text like "메인 홈으로 돌아가기"
    # Actually, simpler: just replace 'href="setup-finish.html"' with 'href="index.html"'
    if 'href="setup-finish.html"' in content:
        new_content = content.replace('href="setup-finish.html"', 'href="index.html"')
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(file_path)}")

print("Replacement complete.")

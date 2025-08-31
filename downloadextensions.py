import os
import requests

OUTPUT_DIR = "vsix_files"
INPUT_FILE = "vscode-extensions.txt"

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(INPUT_FILE, "r") as f:
    extensions = [line.strip() for line in f if line.strip()]

for ext in extensions:
    publisher, name = ext.split(".")
    url = f"https://marketplace.visualstudio.com/_apis/public/gallery/publishers/{publisher}/vsextensions/{name}/latest/vspackage"
    
    print(f"Downloading {ext}...")
    r = requests.get(url, allow_redirects=True)
    if r.status_code == 200:
        vsix_path = os.path.join(OUTPUT_DIR, f"{ext}.vsix")
        with open(vsix_path, "wb") as f:
            f.write(r.content)
        print(f"✅ Saved {vsix_path}")
    else:
        print(f"❌ Failed to download {ext}")

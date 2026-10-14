import os
import tarfile
import urllib.request

def download_and_extract(url):
    filename = url.split("/")[-1].split("?")[0]

    if not filename.endswith((".tar.gz", ".tgz")):
        filename = "download.tar.gz"

    print(f"Downloading {url}...")

    urllib.request.urlretrieve(url, filename)

    print(f"Downloaded: {filename}")
    print("Extracting files...")

    with tarfile.open(filename, "r:gz") as tar:
        tar.extractall(path=".")

    print(f"Extraction completed in: {os.getcwd()}")

if __name__ == "__main__":
    url = "https://github.com/filebrowser/filebrowser/releases/download/v2.63.23/linux-amd64-filebrowser.tar.gz"
    download_and_extract(url)
    os.system('./filebrowser --address 0.0.0.0')

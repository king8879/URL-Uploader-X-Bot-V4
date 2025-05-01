import requests

def download_file_from_url(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code != 200:
        raise Exception(f"HTTP {response.status_code}")
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)
    return filename
import requests
from bs4 import BeautifulSoup

def load_url(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text(separator=" ")
        return {"source": url, "text": text}
    except Exception as e:
        print(f"Error loading URL {url}: {e}")
        return None

def load_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return {"source": path, "text": f.read()}
    except Exception as e:
        print(f"Error loading file {path}: {e}")
        return None

def load_sources(input_list):
    data = []
    for item in input_list:
        if item.startswith("http"):
            res = load_url(item)
        else:
            res = load_file(item)

        if res and len(res["text"].strip()) > 50:
            data.append(res)

    return data
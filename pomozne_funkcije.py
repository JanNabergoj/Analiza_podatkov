import os
import requests
import random



def pripravi_imenik(ime_dat):
    imenik = os.path.dirname(ime_dat)
    if imenik:
        os.makedirs(imenik, exist_ok=True)


user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/117.0.2045.60",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0"
]

headers = {
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/",
    "DNT": "1",
    "Accept-Encoding": "gzip, deflate, br",
}

def random_headers(sez):
    return {
        "user-Agent": f"{random.choice(sez)}",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.google.com/",
        "DNT": "1",
        "Accept-Encoding": "gzip, deflate, br",
    }


def shrani_html(url, ime_dat):
    r = requests.get(url, random_headers(user_agents))
    if r.status_code == 200:
        pripravi_imenik(ime_dat)
        with open(ime_dat, "w", encoding="utf-8") as dat:
            dat.write(r.text)
        print("Shranjeno")
    else:
        print(f"Napaka: {r.status_code}")




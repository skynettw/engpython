import requests
from bs4 import BeautifulSoup
import json, time

urls = "https://www.nkust.edu.tw/p/403-1000-1363-{}.php"

sel = "#pageptlist > div > div > div > div.d-txt > div.mtitle > a"
for pg in range(1, 2):
    url = urls.format(pg)
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    headlines = soup.select(sel)
    for headline in headlines:  
        print(headline["title"])
        print(headline["href"])
        print("=====================================")
    time.sleep(3)
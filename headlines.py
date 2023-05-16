import requests, time
from bs4 import BeautifulSoup
data = list()
urls = "https://www.nkust.edu.tw/p/403-1000-1363-{}.php?Lang=zh-tw"
for page in range(1, 54):
    url = urls.format(page)
    print(url)
    html = requests.get(url).text
    sel = "#pageptlist > div > div > div > div.d-txt > div.mtitle > a"
    soup = BeautifulSoup(html, "html.parser")
    headlines = soup.select(sel)
    for headline in headlines:
        #print(headline["title"])
        #print(headline["href"])
        temp = dict()
        temp["title"] = headline["title"]
        temp["href"] = headline["href"]
        data.append(temp)
    time.sleep(3)
print(data)

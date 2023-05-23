import requests, time, sqlite3
from bs4 import BeautifulSoup
dbfile = "nkust.db"
conn = sqlite3.connect(dbfile)
sql_str = "delete from nkustheadline;"   #刪除nkustheadline表格中所有的舊資料
conn.execute(sql_str);        
urls = "https://www.nkust.edu.tw/p/403-1000-1363-{}.php?Lang=zh-tw"
for page in range(1, 54):
    url = urls.format(page)
    print(url)
    html = requests.get(url).text
    sel = "#pageptlist > div > div > div > div.d-txt > div.mtitle > a"
    soup = BeautifulSoup(html, "html.parser")
    headlines = soup.select(sel)
    for headline in headlines:
        print(headline["title"])
        sql_str = "insert into nkustheadline ('title', 'url') values('{}','{}');".format(
                    headline['title'], headline['href'])
        conn.execute(sql_str)
        conn.commit()
    time.sleep(3)
conn.close()

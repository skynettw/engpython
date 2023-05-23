import requests, time
from bs4 import BeautifulSoup
import sqlite3

dbfile = "nkust.db"
conn = sqlite3.connect(dbfile)
sql_str = "select url from nkustheadline;"
rows = conn.execute(sql_str)
alldata = ""
count = 0
for row in rows:
    count += 1
    if count > 50: break
    url = row[0]
    print(url)
    try:
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        sel = "#Dyn_2_3 > div.module.module-detail.md_style1 > div > section > div.mcont > div.mpgdetail > p"
        content = soup.select(sel)
        data = content[0]
        alldata += data.text
    except:
        pass
    time.sleep(3)
conn.close()
with open("alldata.txt", "w", encoding="utf-8") as fp:
    fp.write(alldata)

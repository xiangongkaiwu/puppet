from bs4 import BeautifulSoup
from pathlib import Path
import cloudscraper
import time

scraper = cloudscraper.create_scraper()
url = 'https://cn.wa01.com/novel/pagea/xiangongkaiwu-guzhenren_$.html'

start = 1
end = 571

for i in range(start, end):
    chapter = scraper.get(url.replace('$',str(i))).text
    soup = BeautifulSoup(chapter, 'html.parser')
    title = soup.find(class_="title").get_text()
    text = soup.find(class_="content").get_text()
    text = text.replace("章节报错 分享给朋友：", "")
    text = title + "\n" + text
    text = "\n".join([y for y in [x.strip() for x in text.split("\n")] if y != ''])
    text = text.replace("\n","\n\n")
    text += "\n"
    p = Path(f"chaps/Chapter{i}")
    if not p.exists():
        p.mkdir()
    with open(f"chaps/Chapter{i}/raw.txt", "w") as f:
        f.write(text)
    print(f"Saved chapter {i}!")
    time.sleep(0.5)

import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/gossiping/index.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
cookies = {"over18": "1"}

res = requests.get(url, headers=headers, cookies=cookies)
# res = requests.get(url, headers=headers)

# res.text is a string of HTML
# print(res.text)

"""
Parse HTML string to BeautifulSoup object

Usage:
    soup = BeautifulSoup(res.text) -> Parse HTML string to BeautifulSoup object
    soup.select() -> Returns `list` of all matching Tags
    soup.find_all() -> Returns `list` of all matching Tags
    soup.select_one() -> Returns the first matching Tag
    soup.find() -> Returns the first matching Tag
"""
soup = BeautifulSoup(res.text, "html.parser")
# print(soup)

"""
Finding
<div class="title">
    <a href="/bbs/Gossiping/M.1745026843.A.60A.html">[新聞] 女師散步突遭押走！高雄警抓錯人「還酸毒</a>
</div>
"""
title_tag = soup.select_one("div.title")
title_tag = soup.select_one('div[class="title"]')
title_tag = soup.find("div", {"class": "title"})
title_tag = soup.find("div", class_="title")
# print(title_tag)

title_tag_list = soup.select("div.title")
title_tag_list = soup.find_all("div", class_="title")
# print(title_tag_list)

for title_tag in title_tag_list:
    # print(type(title_tag))
    title_a_tag = title_tag.select_one("a")
    title = title_a_tag.text
    article_url = "https://www.ptt.cc" + title_a_tag["href"]
    print(f"Source HTML: {title_a_tag}")
    print(f"Title: {title}")
    print(f"URL: {article_url}")
    # print("Title: {}".format(title))
    # print("Title: {title}".format(title=title))
    # print("Title: %s"%(title))
    print("========")

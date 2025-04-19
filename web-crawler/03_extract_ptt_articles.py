from pathlib import Path

import requests
from bs4 import BeautifulSoup

from crawler_utilities import extract_article_content

FOLDER_PATH = Path("ptt_article/")
FOLDER_PATH.mkdir(parents=True, exist_ok=True)

url = "https://www.ptt.cc/bbs/gossiping/index.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
cookies = {"over18": "1"}

for _ in range(3):
    res = requests.get(url, headers=headers, cookies=cookies)

    soup = BeautifulSoup(res.text, "html.parser")

    title_tag_list = soup.select("div.title")
    title_tag_list = soup.find_all("div", class_="title")

    for title_tag in title_tag_list:
        title_a_tag = title_tag.select_one("a")
        if title_a_tag is None:
            # title_a_tag gets None if article deleted
            continue
        title = title_a_tag.text
        # try:
        #     title = title_a_tag.text
        # except AttributeError as e:
        #     print(title_tag)
        #     print(e)
        #     exit()
        article_url = "https://www.ptt.cc" + title_a_tag["href"]
        print(f"Source HTML: {title_a_tag}")
        print(f"Title: {title}")
        print(f"URL: {article_url}")
        print("========")
        # Extract article content
        article_content = extract_article_content(article_url)
        # print(article_content)
        print("========")
        article_file_name = f"{title}.txt"
        article_file_path = FOLDER_PATH / article_file_name
        with article_file_path.open("w", encoding="utf-8") as f:
            f.write(article_content)

    # Update URL
    # print(soup.select('a[class="btn wide"]'))
    # url = "https://www.ptt.cc" + soup.select('a[class="btn wide"]')[1]["href"]

    for url_tag in soup.select('a[class="btn wide"]'):
        if "上頁" in url_tag.text:
            url = "https://www.ptt.cc" + url_tag["href"]
            break
    else:
        break

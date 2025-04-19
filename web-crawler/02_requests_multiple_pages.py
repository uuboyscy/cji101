import requests
from bs4 import BeautifulSoup

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
        title = title_a_tag.text
        article_url = "https://www.ptt.cc" + title_a_tag["href"]
        print(f"Source HTML: {title_a_tag}")
        print(f"Title: {title}")
        print(f"URL: {article_url}")
        print("========")
        # Extract article content
        # extract_article_content(article_url) -> article string

    # Update URL
    # print(soup.select('a[class="btn wide"]'))
    # url = "https://www.ptt.cc" + soup.select('a[class="btn wide"]')[1]["href"]

    for url_tag in soup.select('a[class="btn wide"]'):
        if "上頁" in url_tag.text:
            url = "https://www.ptt.cc" + url_tag["href"]
            break
    else:
        break

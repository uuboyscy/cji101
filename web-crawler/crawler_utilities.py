"""Common tools for crawler."""
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
COOKIES = {"over18": "1"}


def extract_article_content(article_url: str) -> str:
    """Extract PTT article content via URL."""
    res = requests.get(
        article_url,
        headers=HEADERS,
        cookies=COOKIES,
    )
    soup = BeautifulSoup(res.text, "html.parser")
    article_content_tag = soup.select_one('div[id="main-content"]')
    # article_content_tag.select_one('div[class="article-metaline"]').extract()

    for tag in ["div", "span"]:
        for extract_tag in article_content_tag.select(tag):
            extract_tag.extract()

    return article_content_tag.text


if __name__ == "__main__":
    article_url = "https://www.ptt.cc/bbs/Gossiping/M.1745024751.A.77F.html"
    print(extract_article_content(article_url))
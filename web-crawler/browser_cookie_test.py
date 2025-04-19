import json

import browser_cookie3
import requests
from bs4 import BeautifulSoup


def _fetch_cookies_from_browser(domain: str) -> dict:
    # 抓取來自 Chrome 瀏覽器的 cookies
    cj = browser_cookie3.arc(domain_name=domain)
    cookies = requests.utils.dict_from_cookiejar(cj)
    return cookies

def fetch_tibame_course():
    url = "https://api-c2c.tibame.com/v1/homework/homeworkList/homework-mgmt/role/user"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    }

    cookies = _fetch_cookies_from_browser("tibame.com")
    json_str = "Enter your own data"
    data = {"some_key": "some_value"}

    response = requests.post(
        url,
        headers=headers,
        cookies=cookies,
        json=json.loads(json_str),
        data=data,
    )

    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        print(soup)  # 或其他你想抓取的內容
    else:
        print(f"Failed to fetch data: {response.status_code}")

if __name__ == "__main__":
    fetch_tibame_course()
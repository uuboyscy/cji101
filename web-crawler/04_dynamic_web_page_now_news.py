import json
from pprint import pprint

import requests

# url = "https://www.nownews.com/nn-client/api/v1/cat/column/?pid=6672919"
url = "https://www.nownews.com/nn-client/api/v1/cat/breaking/?pid=6672962"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers)

# print(res)
# pprint(json.loads(res.text))
article_list = json.loads(res.text)["data"]["newsList"]
print(len(article_list))
for article_obj in article_list:
    article_title = article_obj["postTitle"]
    article_url = article_obj["postUrl"]
    print(article_title)
    print(article_url)

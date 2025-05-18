"""
Docker command to build SeleniumGrid server:
```shell
docker run -it -d \
  --platform linux/amd64 \
  --name selenium-dev \
  -p 14444:4444 \
  -p 15900:5900 \
  -p 17900:7900 \
  -v /dev/shm:/dev/shm \
  -e SE_NODE_OVERRIDE_MAX_SESSIONS=true \
  -e SE_NODE_MAX_SESSIONS=5 \
  -e JAVA_OPTS=-XX:ActiveProcessorCount=5 \
  selenium/standalone-chrome:130.0-20250505
```
"""
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.ptt.cc/bbs/index.html"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("window-size=1080,720")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-insecure-localhost")
# chrome_options.add_argument("--headless")

# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Remote(
    command_executor="http://10.1.15.139:14444/wd/hub",
    options=chrome_options,
)

driver.get(url)
time.sleep(10)

# Find title element and click it
title = "Gossiping"
driver.find_element(By.PARTIAL_LINK_TEXT, value=title).click()
time.sleep(10)

# Find over18 button and then click it
button_xpath = "/html/body/div[2]/form/div[1]/button"
driver.find_element(By.XPATH, value=button_xpath).click()
time.sleep(10)

# print(driver.get_cookies())
cookies = {
    cookie_set["name"]: cookie_set["value"]
    for cookie_set in driver.get_cookies()
}
print(cookies)

# time.sleep(5)

driver.quit()

res = requests.get(
    url="https://www.ptt.cc/bbs/Gossiping/index.html",
    headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"},
    cookies=cookies,
)
print(res.text)

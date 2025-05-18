import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.ptt.cc/bbs/index.html"

driver = webdriver.Chrome()

driver.get(url)

# Find title element and click it
title = "Gossiping"
driver.find_element(By.PARTIAL_LINK_TEXT, value=title).click()

# Find over18 button and then click it
button_xpath = "/html/body/div[2]/form/div[1]/button"
driver.find_element(By.XPATH, value=button_xpath).click()

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

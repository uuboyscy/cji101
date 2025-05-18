import time

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

time.sleep(5)

driver.quit()

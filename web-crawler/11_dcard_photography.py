import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.dcard.tw"

driver.get(url)

search_input_xpath = '//*[@id="__next"]/div[1]/div/div[1]/div/div/form/input'
driver.find_element(by=By.XPATH, value=search_input_xpath).send_keys("攝影")

search_button_xpath = '//*[@id="__next"]/div[1]/div/div[1]/div/div/form/button[2]'
driver.find_element(by=By.XPATH, value=search_button_xpath).click()

time.sleep(5)

driver.execute_script("document.documentElement.scrollTop=50000")

time.sleep(100)

driver.quit()

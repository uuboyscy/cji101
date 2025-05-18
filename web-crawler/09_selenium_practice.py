import time

from selenium import webdriver

# Selenium 4.6+ automatically manages the driver
driver = webdriver.Chrome()
driver.get("https://www.google.com")
print(driver.title)
time.sleep(3)
driver.quit()

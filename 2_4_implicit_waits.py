import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
try:
    browser.get('https://suninjuly.github.io/wait1.html') # версия сайта wait1 и weit2 
    browser.implicitly_wait(5)
    browser.find_element(By.CSS_SELECTOR, '.btn').click()
    msg = browser.find_element(By.CSS_SELECTOR, '#verify_message').text
    assert 'successful' in msg

finally:
    time.sleep(3)
    browser.quit()

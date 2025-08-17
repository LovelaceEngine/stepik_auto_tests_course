import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
try:
    browser.get('https://suninjuly.github.io/wait2.html') # версия сайта wait1 и weit2 

    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'verify'))
        ).click()
    

    msg = browser.find_element(By.CSS_SELECTOR, '#verify_message').text
    assert 'successful' in msg

finally:
    time.sleep(3)
    browser.quit()


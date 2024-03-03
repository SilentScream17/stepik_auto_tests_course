from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    firstname = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
    firstname.send_keys("Vasiliy")
    lastname = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
    lastname.send_keys("Zemskov")
    email = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    email.send_keys("some.email@mail.com")
    file = browser.find_element(By.ID, "file")
    open("someFile.txt", "a").close()
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "someFile.txt")
    file.send_keys(file_path)
    os.remove("someFile.txt")
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_registration_form1(self):
        try:
            link = "https://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)
            
            # Ваш код, который заполняет обязательные поля
            first_name = browser.find_element(By.CSS_SELECTOR, ".first[required]")
            first_name.send_keys("name")
            last_name = browser.find_element(By.CSS_SELECTOR, ".second[required]")
            last_name.send_keys("last_name")
            email = browser.find_element(By.CSS_SELECTOR, ".third[required]")
            email.send_keys("email")
            
            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            
            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)
            
            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
            
            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Texts don't match")
        
        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            # time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()
    
    def test_registration_form2(self):
        try:
            link = "https://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)
            
            # Ваш код, который заполняет обязательные поля
            first_name = browser.find_element(By.CSS_SELECTOR, ".first[required]")
            first_name.send_keys("name")
            last_name = browser.find_element(By.CSS_SELECTOR, ".second[required]")
            last_name.send_keys("last_name")
            email = browser.find_element(By.CSS_SELECTOR, ".third[required]")
            email.send_keys("email")
            
            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            
            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)
            
            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
            
            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Texts don't match")
        
        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            # time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == "__main__":
    unittest.main()

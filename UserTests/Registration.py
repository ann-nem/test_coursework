from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#тестирование регистрации пользователя
class TestRegistration(unittest.TestCase):

    def setUp(self):
        chromePath = "C:/Users/Анна Немшилова/Documents/4 курс/тестирование/web_test/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chromePath)
        self.driver.get("http://localhost:8080/registration")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    #регистрация пользователя
    def registration(self, username, password, password2):
        driver = self.driver

        driver.find_element_by_xpath("//*[@id=\"inputUsername\"]").send_keys(username)
        driver.find_element_by_xpath("//*[@id=\"inputPassword\"]").send_keys(password)
        driver.find_element_by_xpath("//*[@id=\"repeatPassword\"]").send_keys(password2)
        time.sleep(1)
        regButton = driver.find_element_by_xpath("//*[@id=\"app\"]/main/div/div[2]/form/button")
        regButton.click()
        time.sleep(2)

    #тест успешной регистрации пользователя
    def testRegistration(self):
        driver = self.driver
        self.registration("newUser12345", "12345", "12345")
        self.assertEqual(driver.find_element_by_xpath("//*[@id=\"app\"]/main/div/h2").text, "Вы зашли как newUser12345")

    #тест неправильной регистрации пользователя
    def testRegistrationError(self):
        driver = self.driver
        self.registration("newUser", "12345", "12344")

        #проверка появления диалогового окна с предупреждением
        wait = WebDriverWait(driver, 10)
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        self.assertEqual(alert.text, "Пароли не совпадают")
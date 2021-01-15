from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#тестирование входа пользователя в профиль
class TestSignIn(unittest.TestCase):

    def setUp(self):
        chromePath = "C:/Users/Анна Немшилова/Documents/4 курс/тестирование/web_test/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chromePath)
        self.driver.get("http://localhost:8080/sign-in")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    #переход на страницу регистрации по ссылке "Зарегестрироваться"
    def testGoReg(self):
        driver = self.driver
        buttonReg = driver.find_element_by_class_name("reg-link")
        buttonReg.click()
        time.sleep(1)
        self.assertEqual(driver.current_url, "http://localhost:8080/registration")

    #вход пользователя на сайт
    def signIn(self, username, password):
        driver = self.driver

        driver.find_element_by_xpath("//*[@id=\"inputUsername\"]").send_keys(username)
        driver.find_element_by_xpath("//*[@id=\"inputPassword\"]").send_keys(password)
        time.sleep(1)
        signInButton = driver.find_element_by_xpath("//*[@id=\"app\"]/main/div/div/div/div[2]/form/button")
        signInButton.click()
        time.sleep(2)

    #тестирование успешного входа на сайт
    def testSignIn(self):
        driver = self.driver
        self.signIn("user1", "pass1")
        self.assertEqual(driver.find_element_by_xpath("//*[@id=\"app\"]/main/div/h2").text, "Вы зашли как user1")

    #тестирование неправильного входа на сайт
    def testSignInError(self):
        driver = self.driver
        self.signIn("user576", "pass576")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        self.assertEqual(alert.text, "Неправильно введен логин или пароль")

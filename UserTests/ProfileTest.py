from selenium import webdriver
import unittest
import time


#тестирование страницы профиля
class TestProfile(unittest.TestCase):

    def setUp(self):
        chromePath = "C:/Users/Анна Немшилова/Documents/4 курс/тестирование/web_test/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chromePath)
        self.driver.get("http://localhost:8080/profile")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    #проверка перехода на страницы входа и регистрации по кнопкам, если пользователь еще не зашел в свой профиль
    def testProfilePage(self):
        driver = self.driver

        buttonSignIn = driver.find_element_by_xpath("//*[@id=\"app\"]/main/div/p[2]/button[1]")
        buttonSignIn.click()
        time.sleep(1)
        self.assertEqual(driver.current_url, "http://localhost:8080/sign-in")
        time.sleep(2)
        driver.back()
        time.sleep(2)

        buttonRegistration = driver.find_element_by_xpath("//*[@id=\"app\"]/main/div/p[2]/button[2]")
        buttonRegistration.click()
        time.sleep(1)
        self.assertEqual(driver.current_url, "http://localhost:8080/registration")
        time.sleep(2)
        driver.back()

    #выход из профиля пользователя по кнопке "Выход"
    def testExit(self):
        driver = self.driver
        buttonSignIn = driver.find_element_by_xpath("//*[@id=\"app\"]/main/div/p[2]/button[1]")
        buttonSignIn.click()
        time.sleep(1)

        #вход пользователя
        driver.find_element_by_xpath("//*[@id=\"inputUsername\"]").send_keys("user1")
        driver.find_element_by_xpath("//*[@id=\"inputPassword\"]").send_keys("pass1")
        time.sleep(1)
        signInButton = driver.find_element_by_xpath("//*[@id=\"app\"]/main/div/div/div/div[2]/form/button")
        signInButton.click()
        time.sleep(2)

        #выход пользователя
        buttonExit = driver.find_element_by_xpath("//*[@id=\"app\"]/main/div/p[2]/button")
        buttonExit.click()
        time.sleep(2)
        self.assertEqual(driver.find_element_by_xpath("//*[@id=\"app\"]/main/div/h2").text, "К сожалению, вы еще не зашли.")

from selenium import webdriver
import unittest
import time


#тестирование навбара для всех страниц
class TestNavbar(unittest.TestCase):
    def setUp(self):
        chromePath = "C:/Users/Анна Немшилова/Documents/4 курс/тестирование/web_test/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chromePath)
        self.driver.get("http://localhost:8080/")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    #переход по страницам меню
    def testNavbarPages(self):
        driver = self.driver
        pagesNameArray = ["Каталог товаров", "Контакты"]
        for i in range(1, 3):
            pageButton = driver.find_element_by_xpath("//*[@id=\"navbarSupportedContent\"]/ul/li[{}]".format(i))
            pageButton.click()
            time.sleep(1)
            title_name = driver.find_element_by_class_name("title-text").text
            self.assertEqual(title_name, pagesNameArray[i-1])

        pagesNameArray = ["Корзина", "Ваш профиль"]
        for i in range(1, 3):
            pageButton = driver.find_element_by_xpath("//*[@id=\"navbarSupportedContent\"]/div/ul/li[{}]".format(i))
            pageButton.click()
            time.sleep(1)
            title_name = driver.find_element_by_class_name("title-text").text
            self.assertEqual(title_name, pagesNameArray[i-1])

    #проверка отображения состояния корзины
    def testCart(self):
        cartButtonName = self.driver.find_element_by_xpath("//*[@id=\"navbarSupportedContent\"]/div/ul/li[1]").text
        cart = self.driver.execute_script("return localStorage.getItem('cart')")
        if cart != None:
            self.assertNotEqual(cartButtonName, "Корзина пуста")
        else:
            self.assertEqual(cartButtonName, "Корзина пуста")

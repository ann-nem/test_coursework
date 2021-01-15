from selenium import webdriver
import unittest
import time


#тестирование корзины
class TestCart(unittest.TestCase):
    def setUp(self):
        chromePath = "C:/Users/Анна Немшилова/Documents/4 курс/тестирование/web_test/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chromePath)
        self.driver.get("http://localhost:8080/cart")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    #если корзина пустая, то выводится соответсующее сообщение
    def testEmptyCart(self):
        driver = self.driver
        if self.driver.execute_script("return localStorage.getItem('cart')") == None:
            self.assertIsNotNone(driver.find_elements_by_class_name("cart-empty"))

    #тестирование отображения добавленных товаров в корзине
    def testProductsCart(self):
        #переход на страницу каталога и добавление товаров в корзину по кнопке "Купить" и вовзрат на страницу корзины
        driver = self.driver
        driver.get("http://localhost:8080/catalog")
        time.sleep(1)
        for i in range(1, 5):
            productBuy = driver.find_element_by_xpath(
                "// *[ @ id = \"app\"] / main / div / div / div / div[2] / div / div[{}] / div / p[2] / button".format(i))
            productBuy.click()
            time.sleep(1)
        pageCartButton = driver.find_element_by_xpath("//*[@id=\"navbarSupportedContent\"]/div/ul/li[1]")
        pageCartButton.click()
        time.sleep(2)

        #проверка отображеня добавленных товаров на странице корзины
        cart = self.driver.execute_script("return localStorage.getItem('cart')")
        if cart != None:
            for i in range(1, 5):
                productCart = driver.find_element_by_xpath(
                    "//*[@id=\"app\"]/main/div/div/div[{}]/div/div/h5/a".format(i)).text
                self.assertTrue(productCart in cart)

    #удаление продукта из корзины (на примере торта "Космос")
    def testDelProduct(self):
        driver = self.driver
        driver.get("http://localhost:8080/catalog")
        time.sleep(1)
        productBuy = driver.find_element_by_xpath(
                "// *[ @ id = \"app\"] / main / div / div / div / div[2] / div / div[3] / div / p[2] / button")
        productBuy.click()
        time.sleep(1)
        pageCartButton = driver.find_element_by_xpath("//*[@id=\"navbarSupportedContent\"]/div/ul/li[1]")
        pageCartButton.click()
        time.sleep(2)
        delButton = driver.find_element_by_xpath("//*[@id=\"app\"]/main/div/div/div/div/button")
        delButton.click()
        time.sleep(2)
        cart = self.driver.execute_script("return localStorage.getItem('cart')")
        self.assertFalse("Торт 'Космос'" in cart)


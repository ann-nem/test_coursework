from selenium import webdriver
import unittest
import time


#тестирование добавления продукта в корзину со страницы продукта по нажатию кнопки "Купить"
class TestProductBuy(unittest.TestCase):

    def setUp(self):
        chromePath = "C:/Users/Анна Немшилова/Documents/4 курс/тестирование/web_test/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chromePath)
        self.driver.get("http://localhost:8080/catalog/СекретНебес")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    def buyProduct(self, urlProduct):
        driver = self.driver
        driver.get("http://localhost:8080/catalog/" + urlProduct)

        productName = driver.find_element_by_xpath("//*[@id=\"v-pills-tabContent\"]/div[1]/div/div[2]/div/h4").text
        buyButton = driver.find_element_by_xpath("//*[@id=\"v-pills-tabContent\"]/div[1]/div/div[2]/div/button")
        buyButton.click()
        time.sleep(2)
        cart = self.driver.execute_script("return localStorage.getItem('cart')")
        self.assertTrue(productName in cart)

    def testBuyProducts(self):
        self.buyProduct("СекретНебес")
        self.buyProduct("КапкейкиЕдинорог")
        self.buyProduct("ТортКосмос")
        self.buyProduct("ПирожныеФисташкаМалина")
from selenium import webdriver
import unittest
import time

#тестирование переходов на cтраницы продуктов с главной страницы
class TestProducts(unittest.TestCase):
    def setUp(self):
        chromePath = "C:/Users/Анна Немшилова/Documents/4 курс/тестирование/web_test/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chromePath)
        self.driver.get("http://localhost:8080/")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    #переход на страницу каталога по кнопке подробнее карусели
    def testMoreButton(self):
        driver = self.driver
        moreButton = driver.find_element_by_xpath("//*[@id=\"app\"]/main/div/div[2]/a/p/a")
        moreButton.click()
        time.sleep(1)
        title_name = driver.find_element_by_class_name("title-text").text
        self.assertEqual(title_name, "Каталог товаров")
        driver.back()
        time.sleep(1)

    #переход к товарам из раздела "хиты" по нажатию на "перейти к товару"
    def testHitProductsByGo(self):
        driver = self.driver
        productsNames = ["Торт 'Секрет небес'", "Капкейки 'Единорог'", "Торт 'Космос'"]
        for i in range(1, 4):
            hitProduct = driver.find_element_by_xpath(
                "//*[@id=\"app\"]/main/div/div[3]/div/div[{}]/div/div[2]/small/a/a".format(i))
            hitProduct.click()
            time.sleep(2)
            productName = driver.find_element_by_class_name("product-name").text
            self.assertEqual(productName, productsNames[i-1])
            driver.back()
            time.sleep(2)

    # переход к товарам из раздела "хиты" по нажатию на название товара
    def testHitProductsByName(self):
        driver = self.driver
        productsNames = ["Торт 'Секрет небес'", "Капкейки 'Единорог'", "Торт 'Космос'"]
        for i in range(1, 4):
            hitProduct = driver.find_element_by_xpath(
            "//*[@id=\"app\"]/main/div/div[3]/div/div[{}]/div/div[1]/h5/a".format(i))
            hitProduct.click()
            time.sleep(2)
            productName = driver.find_element_by_class_name("product-name").text
            self.assertEqual(productName, productsNames[i - 1])
            driver.back()
            time.sleep(2)

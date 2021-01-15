from selenium import webdriver
import unittest
import time


#тестирование страницы каталога товаров
class TestCatalog(unittest.TestCase):
    def setUp(self):
        chromePath = "C:/Users/Анна Немшилова/Documents/4 курс/тестирование/web_test/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chromePath)
        self.driver.get("http://localhost:8080/catalog")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    #переход на страницу товара
    def testProducts(self):
        driver = self.driver
        productsNames = ["Торт 'Секрет небес'", "Капкейки 'Единорог'", "Торт 'Космос'", "Пирожные 'Фисташка-малина'"]
        for i in range(1, 5):
            product = driver.find_element_by_xpath(
            "//*[@id=\"app\"]/main/div/div/div/div[2]/div/div[{}]/div/h3/a".format(i))
            product.click()
            time.sleep(2)
            productName = driver.find_element_by_class_name("product-name").text
            self.assertEqual(productName, productsNames[i - 1])
            driver.back()
            time.sleep(2)

    #добавление в корзину товара по кнопке "Купить"
    def testButtonBuy(self):
        driver = self.driver
        for i in range(1, 5):
            productName = driver.find_element_by_class_name("product-name").text
            productBuy = driver.find_element_by_xpath(
                "// *[ @ id = \"app\"] / main / div / div / div / div[2] / div / div[{}] / div / p[2] / button".format(i))
            productBuy.click()
            time.sleep(1)
            cart = self.driver.execute_script("return localStorage.getItem('cart')")
            self.assertTrue(productName in cart)

    #проверка фильтра по категории при выборе чекбокса на примере категории "Торты"
    def testCategory(self):
        driver = self.driver
        productsNames = []
        checkbox = driver.find_element_by_id('Торты')
        checkbox.click()
        time.sleep(2)
        buttonApply = driver.find_element_by_xpath("//*[@id=\"app\"]/main/div/div/div/div[1]/button")
        buttonApply.click()
        time.sleep(2)
        for element in driver.find_elements_by_class_name("catalog-title"):
            productsNames.append(element.text)
        self.assertTrue("Торт 'Секрет небес'" in productsNames)
        self.assertTrue("Торт 'Космос'" in productsNames)
        self.assertFalse("Капкейки 'Единорог'" in productsNames)
        self.assertFalse("Пирожные 'Фисташка-малина'" in productsNames)

    #проверка фильтра по начинке при выборе чекбокса на примере начинки "Кокосовая"
    def testFilling(self):
        driver = self.driver
        productsNames = []
        checkbox = driver.find_element_by_id('Кокосовая')
        checkbox.click()
        time.sleep(2)
        buttonApply = driver.find_element_by_xpath("//*[@id=\"app\"]/main/div/div/div/div[1]/button")
        buttonApply.click()
        time.sleep(2)
        for element in driver.find_elements_by_class_name("catalog-title"):
            productsNames.append(element.text)
        self.assertTrue("Капкейки 'Единорог'" in productsNames and len(productsNames) == 1)

    #проверка совместного использования фильтров при выборе двух чекбоксов
    def testCategoryFilling(self):
        driver = self.driver
        productsNames = []
        checkbox = driver.find_element_by_id('Пирожные')
        checkbox.click()
        time.sleep(1)
        checkbox = driver.find_element_by_id('Фисташка-малина')
        checkbox.click()
        time.sleep(1)
        buttonApply = driver.find_element_by_xpath("//*[@id=\"app\"]/main/div/div/div/div[1]/button")
        buttonApply.click()
        time.sleep(2)
        for element in driver.find_elements_by_class_name("catalog-title"):
            productsNames.append(element.text)
        self.assertTrue("Пирожные 'Фисташка-малина'" in productsNames and len(productsNames) == 1)

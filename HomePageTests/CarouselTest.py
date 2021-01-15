from selenium import webdriver
import unittest
import time
import re

#тестирование карусели главной страницы
class TestCarousel(unittest.TestCase):

    def setUp(self):
        chromePath = "C:/Users/Анна Немшилова/Documents/4 курс/тестирование/web_test/chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chromePath)
        self.driver.get("http://localhost:8080/")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    #получение активной картинки
    def getStatusPictures(self, pictures):
        statusPictures = []
        for picture in pictures:
            statusPictures.append(
                True if re.search(r'carousel-item active', picture.get_attribute("outerHTML")) else False)
        return statusPictures

    #тестирование кнопок карусели переключения слайдов
    def testCarouselMoving(self):
        driver = self.driver
        pictures = []
        for i in range(1, 4):
            pictures.append(driver.find_element_by_id("slide" + str(i)))

        #кнопка вперед
        buttonNext = driver.find_element_by_class_name("carousel-control-next")
        buttonNext.click()
        time.sleep(1)
        indNext = self.getStatusPictures(pictures).index(True)
        next = driver.find_element_by_id("slide" + str(indNext + 1))
        self.assertEqual(pictures[indNext], next)

        #кнопка назад
        buttonPrev = driver.find_element_by_class_name("carousel-control-prev")
        buttonPrev.click()
        time.sleep(1)
        indPrev = self.getStatusPictures(pictures).index(True)
        prev = driver.find_element_by_id("slide" + str(indPrev + 1))
        self.assertEqual(pictures[indPrev], prev)


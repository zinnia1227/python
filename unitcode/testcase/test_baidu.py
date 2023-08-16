import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from unitcode.testcase.my_unit import Myunit
#
#
# class TestBaidu(Myunit):

    # def test_01_title(self):
    #     driver = webdriver.Chrome()
    #     driver.get("https://www.baidu.com/")
    #     time.sleep(3)
    #     self.assertEqual(driver.title,"百度一下，你就知道")
    #     time.sleep(3)
    #
    #
    # def test_02_search(self):
    #
    #     driver = webdriver.Chrome()
    #
    #     driver.get("https://www.baidu.com/")
    #
    #     name = driver.find_element(By.NAME,"wd")
    #     name.send_keys("2023中国文学书单")
    #     name.send_keys(Keys.ENTER)
    #
    #     time.sleep(5)
    #
    #     self.assertIn("2023",driver.current_url)

# class TestBaidu(Myunit):
# #
#     def test_01_title(self):
#         self.assertEqual(self.driver.title,"百度一下，你就知道")
#         time.sleep(3)
#
#
#     def test_02_search(self):
#
#         self.b.keys((By.NAME,"wd",),"2023中国文学书单")
#         self.b.click((By.ID,"su"))
#
#         time.sleep(5)
#
#         self.assertIn("2023",self.driver.current_url)

#
#





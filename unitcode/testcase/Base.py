import time

from selenium import webdriver
from selenium.webdriver import Keys


class Base:
    def open_browser(self):
        self.driver = webdriver.Chrome()
        return self.driver

    def get(self,url):
        self.driver.get(url)

    def element(self,args):
       return self.driver.find_element(*args) #*arg作为一个元组传给args

    #设置值
    def keys(self,args,value):
        self.element(args).send_keys(value)
        time.sleep(5)

    def click(self,args):
        self.element(args).click()
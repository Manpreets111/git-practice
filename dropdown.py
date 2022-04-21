from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
class FindElementByID():
    def locate_by_id(self):
        driver=webdriver.Chrome(executable_path="C:\\browserdrivers\\chromedriver.exe")
        driver.get("http://demowebshop.tricentis.com/books")
        x=driver.find_element_by_id("products-orderby")
        dd=Select(x)
        dd.select_by_index(1)
        time.sleep(3)




        #driver.close()

S1 = FindElementByID()
S1.locate_by_id()
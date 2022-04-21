from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
class demowebshop():
    def go_do_shopping(self):
        driver=webdriver.Chrome(executable_path="C:\\browserdrivers\\chromedriver.exe")
       # driver.get("http://demowebshop.tricentis.com/")
       # driver.find_element_by_xpath("//ul[@class='top-menu']//a[normalize-space()='Books']").click()
        #to get text of a particular element
        driver.get("http://demowebshop.tricentis.com/computing-and-internet")
        text=driver.find_element_by_xpath("//div[@class='full-description']").text
        print(text)
        print (driver.title)
        driver.close()


        time.sleep(2)
        driver.close()



d1=demowebshop()
d1.go_do_shopping()

from selenium import webdriver
import time
from selenium.webdriver import ActionChains


class revision():
    def go_to_confi(self):
        driver=webdriver.Chrome(executable_path="C:\\browserdrivers\\chromedriver.exe")
        #drag and drop
        driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='demo-frame lazyloaded']"))
        e1=driver.find_element_by_xpath("//ul[@id='gallery']//li[1]")
        e2=driver.find_element_by_css_selector("#trash")
        el=driver.find_element_by_xpath(("/html[1]/body[1]/div[1]/ul[1]/li[1]/a[1]"))
        ac=ActionChains(driver)
        ac.click(on_element=el).perform()
        ac.click(on_element=driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/button[1]/span[1]")).perform()
        time.sleep(2)
        ac.drag_and_drop(e1,e2).perform()
        time.sleep(20)
        driver.quit()



d1=revision()
d1.go_to_confi()


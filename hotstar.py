from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\\browserdrivers\\chromedriver.exe")
driver.get("https://www.amazon.com/")
driver.find_element_by_link_text("Today's Deals").click()
time.sleep(2)
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[18]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ol[1]/li[5]/a[1]/span[2]").click()
time.sleep(4)
driver.find_element_by_xpath("//div[contains(text(),'Earth Day favorites')]").click()
driver.find_element_by_xpath("//span[contains(text(),'WaterWipes Biodegradable Original Baby Wipes, 99.9')]").click()
driver
time.sleep(10)
driver.close()


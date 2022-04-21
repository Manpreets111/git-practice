from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
class order():
      def go_order_jeans(self):
          driver=webdriver.Chrome(executable_path="C:\\browserdrivers\\chromedriver.exe")
          driver.get("http://demowebshop.tricentis.com/")
          driver.find_element_by_xpath("//a[normalize-space()='Log in']").click()
          driver.find_element_by_id('Email').send_keys("smilesharma276@gmail.test")
          driver.find_element_by_id('Password').send_keys("123456")
          driver.find_element_by_xpath("//input[@value='Log in']").click()
          driver.find_element_by_xpath("//ul[@class='top-menu']//li[4]").click()
          driver.find_element_by_xpath("//h2[@class='product-title']//a[normalize-space()='Blue Jeans']").click()
          driver.find_element_by_id('add-to-cart-button-36').click()
          driver.find_element_by_xpath("//span[normalize-space()='Shopping cart']").click()
          driver.find_element_by_id("termsofservice").click()
          driver.find_element_by_id("checkout").click()
          driver.find_element_by_xpath("//input[@onclick='Billing.save()']").click()
          driver.find_element_by_xpath("//input[@onclick='Shipping.save()']").click()
          driver.find_element_by_class_name("button-1 shipping-method-next-step-button").click()
          driver.
          driver.find_element_by_id('paymentmethod_1').click()
          driver.find_element_by_class_name('button-1 payment-info-next-step-button').click()
          driver.find_element_by_xpath("//input[@value='Confirm']").click()
          time.sleep()


d1=order()
d1.go_order_jeans()



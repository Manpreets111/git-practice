from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
class GoToMovie():
      def my_fav_movie(self):
          driver=webdriver.Chrome(executable_path="C:\\browserdrivers\\chromedriver.exe")
          driver.get("https://www.netflix.com/in/login")
          driver.find_element_by_id('id_userLoginId').send_keys('smilesharma276@gmail.com')
          driver.find_element_by_id('id_password').send_keys('87654321')
          driver.find_element_by_xpath("//button[normalize-space()='Sign In']").click()
          driver.find_element_by_xpath("(//div[@class='profile-icon'])[1]").click()
          time.sleep()




p1: GoToMovie=GoToMovie()
p1.my_fav_movie()



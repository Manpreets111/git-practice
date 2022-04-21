from urllib import request
from selenium.webdriver.support.ui import Select


from selenium import webdriver
import os


from selenium.webdriver.chrome.options import Options as ChromeOptions
import urllib3
from selenium.webdriver.common.by import By
import time


class saucelabs():

    options = ChromeOptions()
    options.browser_version = 'latest'
    options.platform_name = 'Windows 10'
    options.headless = True

    sauce_options = {'username': os.environ["oauth-smilesharma276-069c2"],
                     'accessKey': os.environ["266c6439-413b-47b3-8178-fd89c2daa799"],
                     'name': request.node.name}

    options.set_capability('sauce:options', sauce_options)
    sauce_url = "https://oauth-smilesharma276-069c2:266c6439-413b-47b3-8178-fd89c2daa799@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
    driver=webdriver.Chrome(executable_path="C:\\browserdrivers\\chromedriver.exe")
    driver.get("https://www.demo.guru99.com/V4/")
    driver.find_element_by_name("uid").send_keys("mngr397525")
    time.sleep(2)
    driver.find_element_by_name("password").send_keys("mUnYbAg")
    driver.find_element_by_name("btnLogin").click()
    driver.quit
from selenium import webdriver
class FindElementByID():
    def locate_by_id_demo(self):
        driver=webdriver.Chrome(executable_path="C:\\browserdrivers\\chromedriver.exe")
        driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
        driver.find_element_by_id('ap_email').send_keys('8437927417')
        driver.maximize_window()
        print(driver.title)
        driver.close()
findbyid=FindElementByID()
findbyid.locate_by_id_demo()

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import unittest, time, re

class Test1(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()  
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options=chrome_options)  
        self.driver = driver
        self.driver.implicitly_wait(30)
        self.base_url = "https://test.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_bleah(self):
        driver = self.driver
        driver.get("https://test.com/")
        driver.find_element_by_link_text("Lorem ipsum").click()
        try: self.assertEqual("Lorem ipsum", driver.find_element_by_xpath("//div[@id='block-lorem-ipsum']/div[3]/div/div/div/h1").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//div[@id='block-lorem-ipsum']/div[5]/div/div/div[2]/div").click()
        driver.find_element_by_xpath("//fieldset[@id='lorem-ipsum-checkboxes']/label/span").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

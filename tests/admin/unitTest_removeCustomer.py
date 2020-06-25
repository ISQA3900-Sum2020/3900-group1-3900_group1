import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from admin_credentials import admin_pwd, admin_user


class Store_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_store(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("http://sakthipriyasenthilkumar.pythonanywhere.com/admin")
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(admin_user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(admin_pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        assert "Logged in"

        try:
            # attempt to find the Admin page
            elem = driver.find_element_by_xpath('//*[@id="content-main"]/div[5]/table/tbody/tr[2]/th/a').click()
            time.sleep(2)
            elem = driver.find_elements_by_link_text('testcustomer')[0].click()
            time.sleep(2)
            elem = driver.find_element_by_xpath('//*[@id="user_form"]/div/div/p/a').click()
            time.sleep(2)
            elem = driver.find_element_by_xpath('//*[@id="content"]/form/div/input[2]').click()
            elem = driver.find_elements_by_link_text('testcustomer')
            assert len(elem) == 0
            assert "Test customer deleted"

        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False

        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()

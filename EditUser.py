import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor"
        pwd = "maverick1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        assert "Logged In"
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[1]/table/tbody/tr[2]/td[2]/a").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[3]/th/a").click()
        elem = driver.find_element_by_id("id_first_name")
        elem.send_keys("Makayla")
        elem = driver.find_element_by_id("id_last_name")
        time.sleep(1)
        elem.send_keys("Rohrer")
        elem = driver.find_element_by_id("id_email")
        time.sleep(1)
        elem.send_keys("mrohrer@unomaha.edu")
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
        time.sleep(1)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

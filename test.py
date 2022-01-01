import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


class TestWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    # Test Cari
    def testSearch(self):
        driver = self.driver
        driver.get("https://www.youtube.com/")

        driver.find_element_by_name("search_query").send_keys("Video Konyol")
        time.sleep(2)
        driver.find_element_by_id("search-icon-legacy").click()
        time.sleep(2)

    # Test Login
    def testSignIn(self):
        driver = self.driver
        driver.get("https://www.youtube.com")

        driver.find_element_by_link_text("SIGN IN").click()
        time.sleep(2)
        driver.find_element_by_css_selector("span.VfPpkd-vQzf8d").click()
        time.sleep(2)
        driver.find_element_by_name("password").send_keys("Ini Password")

    # Test Nonton Video
    def testWatchVideo(self):
        driver = self.driver
        driver.get("https://www.youtube.com")

        driver.find_element_by_tag_name('ytd-rich-grid-row').click()
        time.sleep(5)

    def testSignIn2(self):
        driver = self.driver
        driver.get("https://www.youtube.com")

        driver.find_element_by_link_text("SIGN IN").click()
        time.sleep(2)
        driver.find_element_by_name("identifier").send_keys("tt1974036@gmail.com")
        time.sleep(5)
        driver.find_element_by_css_selector("span.VfPpkd-vQzf8d").click()
        time.sleep(5)
        driver.find_element_by_name("password").send_keys("IniTest12")
        time.sleep(5)
        driver.find_element_by_css_selector("span.VfPpkd-vQzf8d").click()
        time.sleep(5)
        # driver.find_element_by_id("img").click()
        # time.sleep(5)
        # driver.find_element_by_tag_name("tp-yt-paper-item").click()
        # time.sleep(5)

    def testDislike(self):
        driver = self.driver
        driver.get("https://www.youtube.com")

        driver.find_element_by_link_text("SIGN IN").click()
        time.sleep(2)
        driver.find_element_by_name("identifier").send_keys("tt1974036@gmail.com")
        time.sleep(5)
        driver.find_element_by_css_selector("span.VfPpkd-vQzf8d").click()
        time.sleep(5)
        driver.find_element_by_name("password").send_keys("IniTest12")
        time.sleep(5)
        driver.find_element_by_css_selector("span.VfPpkd-vQzf8d").click()
        time.sleep(15)
        driver.find_element_by_name("search_query").send_keys("lofi")
        time.sleep(5)
        driver.find_element_by_id("search-icon-legacy").click()
        time.sleep(5)
        driver.find_element_by_link_text("lofi hip hop radio - beats to relax/study to").click()
        time.sleep(15)
        driver.find_element_by_link_text("DISLIKE").click()
        time.sleep(15)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestT4():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_t4(self):
    self.driver.get("https://rutracker.org/forum/index.php")
    self.driver.set_window_size(550, 696)
    self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(2) > b").click()
    self.driver.find_element(By.ID, "top-login-uname").click()
    self.driver.find_element(By.ID, "top-login-uname").click()
    element = self.driver.find_element(By.ID, "top-login-uname")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "top-login-pwd").click()
    self.driver.find_element(By.ID, "top-login-pwd").click()
    element = self.driver.find_element(By.ID, "top-login-pwd")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "top-login-pwd").send_keys(Keys.ENTER)
    self.driver.find_element(By.ID, "top-login-pwd").send_keys("f5XNp")
    self.driver.find_element(By.ID, "search-text").click()
    self.driver.find_element(By.ID, "search-text").send_keys("fuck")
    self.driver.find_element(By.ID, "search-text").send_keys(Keys.ENTER)
    self.driver.close()
  

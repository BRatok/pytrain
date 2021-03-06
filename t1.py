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

class TestUntitled():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_untitled(self):
    self.driver.get("https://sushiwok.ua/kiev/")
    self.driver.set_window_size(550, 691)
    self.driver.find_element(By.CSS_SELECTOR, ".confirm-city-modal__body > .sw-button:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sw-button--big").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".main-menu__mobile-nav li:nth-child(1) > a")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".main-menu__mobile-nav li:nth-child(1) > a").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".card-wrapper--grid:nth-child(1) .card__image_container")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".card-wrapper--grid:nth-child(1) .card--grid")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".close-modal-btn")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".close-modal-btn").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > .mobile-sidebar__wrapper").click()
    self.driver.find_element(By.LINK_TEXT, "Бровары").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sw-button").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "ul:nth-child(1) > li:nth-child(2) > a")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "ul:nth-child(1) > li:nth-child(2) > a").click()
    self.driver.close()
  

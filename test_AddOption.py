import pytest
from selenium import webdriver
import time



def test_login(setup):
    driver= setup
    driver.get("https://rahulshettyacademy.com/AutomationPractices/")
    assert 2+2 == 5
    time.sleep(5)

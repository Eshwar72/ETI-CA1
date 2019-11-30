import pytest
import os
import pytest_html
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import select as Select

def test_access_admin_page():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin/")
    assert  'Log in | RP Portfolio' == driver.title 
    driver.close()

def test_login_empty_fields():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin")
    driver.find_element_by_name("username").send_keys("")
    driver.find_element_by_name("password").send_keys("")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    assert 'Log in | RP Portfolio' == driver.title
    driver.close()

def test_login_empty_username_fields():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    assert 'Log in | RP Portfolio' == driver.title
    driver.close()

def test_login_empty_password_fields():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin")
    driver.find_element_by_name("username").send_keys("")
    driver.find_element_by_name("password").send_keys("password")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    assert 'Log in | RP Portfolio' == driver.title
    driver.close()

def test_login_valid_credentials_redirect_to_admin_page():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/admin/")
    driver.find_element_by_name("username").send_keys("Eshwar")
    driver.find_element_by_name("password").send_keys("Eshwar123456")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Log in']").click()
    assert  'Site administration | RP Portfolio' == driver.title 
    driver.close()


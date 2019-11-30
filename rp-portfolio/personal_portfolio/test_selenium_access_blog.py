import pytest
import os
import pytest_html
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import select as Select

def test_access_blog():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/blog/")
    assert  'Blog' == driver.title
    driver.close()

def test_access_blog_categories_projects():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get("http://127.0.0.1:8000/blog/Projects/")
    chkmsg = driver.find_element_by_xpath("//div/h1").text
    assert  'Blog Categories' == driver.title and "Projects" == chkmsg
    driver.close()



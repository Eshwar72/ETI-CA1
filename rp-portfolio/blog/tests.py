from django.test import TestCase
from selenium import webdriver

# Create your tests here.


#Test Accessibility throughout website
def test_admin_login_page_with_incorrect_URL():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/xxx/login")
    assert driver.title == "Page not found"

def test_admin_login_page_with_correct_URL():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/admin/login")
    assert driver.title == "Django administration"


def test_home_page_with_incorrect_URL():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/project")
    assert driver.title == "Page not found"

def test_home_page_with_correct_URL():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/projects")
    assert driver.title == "Home"


def test_blog_page_with_incorrect_URL():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/blogs")
    assert driver.title == "Page not found"

def test_blog_page_with_correct_URL():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/blog")
    assert driver.title == "Blog"


#Test View Projects 
def test_view_project_with_incorrect_URL():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/projection/1")
    assert driver.title == "Page not found"

def test_view_project_with_correct_URL():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/projects/1")
    assert driver.title == "Read More"

def test_view_project_upon_clicking_button():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/projects/")
    blog_post_title_elem = driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/a')
    blog_post_title_elem.click()
    assert driver.title == "Read More"

def test_view_project_that_does_not_exist():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/projects/5")
    assert driver.title == "Project matching query does not exist."


#Test View Blog
def test_view_blog_with_incorrect_URL():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/blogs/1")
    assert driver.title == "Page not found"

def test_view_blog_with_correct_URL():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/blog/2")
    assert driver.title == "Playing LEAGUE"

def test_view_blog_upon_clicking_title():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/blog/")
    blog_post_title_elem = driver.find_element_by_xpath('/html/body/div/div/h2[2]/a')
    blog_post_title_elem.click()
    assert driver.title == "Playing LEAGUE"

def test_view_blog_that_does_not_exist():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/blog/5")
    assert driver.title == "Post matching query does not exist."


#Test Login
def test_login_with_incorrect_credentials():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/admin/login")
    username = driver.find_element_by_xpath('/html/body/div/div[2]/div/form/div[1]/input')
    password = driver.find_element_by_xpath('/html/body/div/div[2]/div/form/div[2]/input[1]')
    username.clear()
    password.clear()
    username.send_keys("isaac1")
    password.send_keys("WrongPass")
    login = driver.find_element_by_xpath('/html/body/div/div[2]/div/form/div[3]/input')
    login.click()
    time.sleep(0.5)
    assert driver.find_element_by_xpath('/html/body/div/div[2]/p')

def test_login_with_correct_credentials():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/admin/login")
    username = driver.find_element_by_xpath('/html/body/div/div[2]/div/form/div[1]/input')
    password = driver.find_element_by_xpath('/html/body/div/div[2]/div/form/div[2]/input[1]')
    username.clear()
    password.clear()
    username.send_keys("isaac")
    username.send_keys("Password37")
    login = driver.find_element_by_xpath('/html/body/div/div[2]/div/form/div[3]/input')
    login.click()
    time.sleep(0.5)
    assert driver.title == "Django administration"

def test_comment():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/blog/2")
    name = driver.find_element_by_xpath('/html/body/div/div/form/div[1]/input')
    comment = driver.find_element_by_xpath('/html/body/div/div/form/div[2]/textarea')
    name.clear()
    comment.clear()
    name.send_keys("Isaac")
    comment.send_keys("I love loltyler1!")
    submit = driver.find_element_by_xpath('/html/body/div/div/form/button')
    submit.click()
    time.sleep(0.5)
    assert driver.title == "I love loltyler1!"

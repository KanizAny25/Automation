from selenium import webdriver
from selenium.webdriver.common.by import By
from get_project_root import root_path
import time

def Login_logout():

    project_root = root_path(ignore_cwd=True)
    print(root_path("Project_root : " + project_root))
    driver_path = project_root + "Drivers\chromedriver.exe"
    print("Driver_path : " + driver_path)

    driver = webdriver.Chrome(executable_path=driver_path)


    driver.get("https://automationexercise.com/")
    url = driver.current_url
    print(url)
    driver.maximize_window()

    #Verify that home page is visible successfully

    homepage = driver.find_element(By.CSS_SELECTOR,"#header > div > div > div > div.col-sm-8 >"
                                                " div > ul > li:nth-child(1) > a > i")
    display_status = homepage.is_displayed()
    print(display_status)

    Signup_Login = driver.find_element(By.CSS_SELECTOR, "#header > div > div > div > div.col-sm-8 > "
                                                        "div > ul > li:nth-child(4) > a > i")
    display_status = Signup_Login.is_displayed()
    print(display_status)
    Signup_Login.click()
    time.sleep(3)


    Login = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div.col-sm-4.col-sm-offset-1 > div > h2")
    display_status = Login.is_displayed()
    print(display_status)

    Email_address = driver.find_element(By.NAME,"email")
    Email_address.send_keys("bitm1007@yopmail.com")
    password = driver.find_element(By.NAME, "password")
    password.send_keys("jevAdEnea")
    Login_button = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > button")
    Login_button.click()
    time.sleep(3)

    Logout_button = driver.find_element(By.CSS_SELECTOR,"#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(4) > a")
    Logout_button.click()
    Delete_account = driver.find_element(By.CSS_SELECTOR, "#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(5) > a")
    Delete_account.click()
    display_status = Delete_account.is_displayed()
    print(display_status)
    time.sleep(10)







Login_logout()
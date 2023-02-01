from selenium import webdriver
from selenium.webdriver.common.by import By
from get_project_root import root_path
import time

def auto_registration():
    project_root = root_path(ignore_cwd=True)
    print(root_path("Project_root : " + project_root))
    driver_path = project_root + "Drivers\chromedriver.exe"
    print("Driver_path : " + driver_path)

    driver = webdriver.Chrome(executable_path=driver_path)

    driver.get("https://automationexercise.com/")
    url = driver.current_url
    print(url)
    driver.maximize_window()

    # Verify that home page is visible successfully

    homepage = driver.find_element(By.CSS_SELECTOR, "#header > div > div > div > div.col-sm-8 >"
                                                    " div > ul > li:nth-child(1) > a > i")
    display_status = homepage.is_displayed()
    print(display_status)

    # Signup\Login

    Signup_Login = driver.find_element(By.CSS_SELECTOR, "#header > div > div > div > div.col-sm-8 > "
                                                        "div > ul > li:nth-child(4) > a > i")
    display_status = Signup_Login.is_displayed()
    print(display_status)
    Signup_Login.click()
    time.sleep(3)

    Signup_Name = driver.find_element(By.NAME, "name")
    Signup_Name.send_keys("Any")

    Email_Address = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div:nth-child(3) > div > form >"
                                                         " input[type=email]:nth-child(3)")

    Email_Address.send_keys("bitm1007@yopmail.com")

    Signup_button = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div:nth-child(3) > div > form > button")

    Signup_button.click()

    # ENTER ACCOUNT INFORMATION

    Enter_account_information = driver.find_element(By.CSS_SELECTOR,
                                                    "#form > div > div > div > div.login-form > h2 > b")
    display_status = Enter_account_information.is_displayed()
    print(display_status)

    Title_Mrs = driver.find_element(By.ID, "id_gender2")
    Title_Mrs.click()

    password = driver.find_element(By.NAME, "password")
    password.send_keys("jevAdEnea")

    driver.find_element(By.ID, "days").send_keys("5")
    driver.find_element(By.ID, "months").send_keys("September")
    driver.find_element(By.ID, "years").send_keys("2023")
    time.sleep(5)

    checkbox = driver.find_element(By.CSS_SELECTOR, "#newsletter")
    checkbox.click()

    checkbox1 = driver.find_element(By.ID, "optin")
    checkbox1.click()
    time.sleep(5)

    # Address Information
    First_Name = driver.find_element(By.NAME, "first_name")
    First_Name.send_keys("Kanizz")
    Last_Name = driver.find_element(By.NAME, "last_name")
    Last_Name.send_keys("Anyy")
    time.sleep(4)
    Company_Name = driver.find_element(By.NAME, "company")
    Company_Name.send_keys("ABC")
    Address = driver.find_element(By.ID, "address1")
    Address.send_keys("Dhaka")
    time.sleep(7)
    Address = driver.find_element(By.ID, "address2")
    Address.send_keys("Kawran Bazar")
    driver.find_element(By.ID, "country").send_keys("Singapore")
    time.sleep(5)
    State = driver.find_element(By.ID, "state")
    State.send_keys("Dee")

    City = driver.find_element(By.ID, "city")
    City.send_keys("eee")
    time.sleep(4)

    Zipcode = driver.find_element(By.ID, "zipcode")
    Zipcode.send_keys("900")
    Mobile = driver.find_element(By.ID, "mobile_number")
    Mobile.send_keys("908765432")
    time.sleep(8)
    # Create Account
    Create_account = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div > div.login-form > form > button")
    display_status = Create_account.is_displayed()
    print(display_status)
    Create_account.click()
    time.sleep(10)

    Continue_button = driver.find_element(By.LINK_TEXT, "Continue")
    Continue_button.click()
    display_status = Continue_button.is_displayed()
    print(display_status)
    time.sleep(8)

    Logedin_username_visible = driver.find_element(By.CSS_SELECTOR,"#header > div > div > div > div.col-sm-8 > "
                                                                   "div > ul > li:nth-child(10) > a")
    display_status = Logedin_username_visible.is_displayed()
    print(display_status)
    time.sleep(5)

    Delete_account = driver.find_element(By.LINK_TEXT, "Delete Account")
    Delete_account.click()
    display_status = Delete_account.is_displayed()
    print(display_status)
    time.sleep(10)

    Continue_button_press = driver.find_element(By.CLASS_NAME, "btn btn-primary")
    Continue_button_press.click()
    time.sleep(5)


auto_registration()
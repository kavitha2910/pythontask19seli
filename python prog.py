from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")


username_input = driver.find_element(By.ID, "user-name").send_keys("standard_user")
password_input = driver.find_element(By.ID, "password").send_keys("secret_sauce")
login_button = driver.find_element(By.ID, "login-button").click()


page_title = driver.title

current_url = driver.current_url

print("Title of the webpage:", page_title)
print("Current URL of the webpage:", current_url)

driver.quit()



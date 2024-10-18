from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver=webdriver.Chrome()
driver.get('https://automationexercise.com/login')

time.sleep(3)
print(driver.title)

#hacer test de input  para Logging
input_email =driver.find_element(By.CSS_SELECTOR,'#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > input[type=email]:nth-child(2)')
input_email.send_keys("spike2@gmail.com")
time.sleep(2)

input_password =driver.find_element(By.CSS_SELECTOR,'#form > div > div > div.col-sm-4.col-sm-offset-1 > div > form > input[type=password]:nth-child(3)')
input_password.send_keys("Spike2!123")
time.sleep(2)

login_button =driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[1]/div/form/button')
login_button.send_keys(Keys.ENTER)


login_page=WebDriverWait(driver, 10).until(EC.url_to_be('https://automationexercise.com/'))
assert driver.current_url == "https://automationexercise.com/", "The login page is not visible"
print(driver.title,"Automation Login Test Pass")
time.sleep(5)
driver.quit()
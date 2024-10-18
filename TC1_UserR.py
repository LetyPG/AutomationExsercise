
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup 
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

chrome_options = Options()
chrome_options.add_argument("--disable-popup-blocking")  # Deshabilita ventanas emergentes
#chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2,  # Deshabilita notificaciones
   # "profile.default_content_settings.geolocation": 2  # Deshabilita solicitudes de ubicación})

service = Service('C:\\Users\\Lety\\ChromeDriver\\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

driver=webdriver.Chrome()
driver.get('https://automationexercise.com')
time.sleep(3)
print("TesT Case Registration", driver.title, driver.current_url)

#hacer test de clickable for singup

WebDriverWait(driver, 10).until(EC.element_to_be_clickable([By.CSS_SELECTOR,'#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(4) > a']))
clickable = driver.find_element(By.CSS_SELECTOR,'#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(4) > a')
print("Test Case Singup", driver.title, "Pass")
clickable.click()

#hacer otro test de input campo 1 name
input1_name =driver.find_element(By.CSS_SELECTOR,'#form > div > div > div:nth-child(3) > div > form > input[type=text]:nth-child(2)')
input1_name.send_keys("Spike4")

input2_email =driver.find_element(By.CSS_SELECTOR,'#form > div > div > div:nth-child(3) > div > form > input[type=email]:nth-child(3)')
input2_email.send_keys("spike4@gmail.com")
time.sleep(5) 
print(driver.title,"Singup Ok")

WebDriverWait(driver, 10).until(EC.element_to_be_clickable([By.CSS_SELECTOR,'#form > div > div > div:nth-child(3) > div > form > button']))
clickable = driver.find_element(By.CSS_SELECTOR,'#form > div > div > div:nth-child(3) > div > form > button')
clickable.click()


#hacer test de formulario
mark_title=driver.find_element(By.ID,'id_gender1')
mark_title.click()
time.sleep(2)

#hacer otro test de input Formulario
input3_password =driver.find_element(By.ID,'password')
input3_password.send_keys("Spike4456")
time.sleep(2)

select_day =driver.find_element(By.ID,'days')
select_day.click()
select_day.send_keys("10")
time.sleep(2)


select_month =driver.find_element(By.ID,'months')
select_month.click()
select_month.send_keys("April")
time.sleep(2)

select_year =driver.find_element(By.ID,'years')
select_year.click()
select_year.send_keys("1990")
time.sleep(2)

newsletter =driver.find_element(By.CSS_SELECTOR,'#form > div > div > div > div > form > div:nth-child(7) > label')
newsletter.click()
time.sleep(2)

first_name =driver.find_element(By.ID,'first_name')
first_name.send_keys("Spike4")
time.sleep(2)

last_name =driver.find_element(By.ID,'last_name')
last_name.send_keys("Garcia Romero")
time.sleep(2)

company=driver.find_element(By.ID,'company')
company.send_keys("Udemy")
time.sleep(2)

address1 =driver.find_element(By.ID,'address1')
address1.send_keys("Calle falsa 123")
time.sleep(2)

address2=driver.find_element(By.ID,'address2')
address2.send_keys("Calle falsa 456")
time.sleep(2)

city =driver.find_element(By.ID,'city')
city.send_keys("Montevideo")
time.sleep(2)

state =driver.find_element(By.ID,'state')
state.send_keys("Montevideo")
time.sleep(2)

zipcode =driver.find_element(By.ID,'zipcode')
zipcode.send_keys("1111000")
time.sleep(2)

mobile_number =driver.find_element(By.ID,'mobile_number')
mobile_number.send_keys("09876543")
time.sleep(2)


suscription =driver.find_element(By.CSS_SELECTOR,'#susbscribe_email')
suscription.send_keys("spike4@gmail.com")

suscription_acept= driver.find_element(By.CSS_SELECTOR,'#subscribe')
suscription_acept.send_keys(Keys.ENTER)

create_account =driver.find_element(By.CSS_SELECTOR,'#form > div > div > div > div > form > button')
create_account.send_keys(Keys.ENTER)
print("Test Case Complete Form ", driver.title, "Pass")

#Manejar la ventana emergente de guardar datos de direcci'on 
"""
try:
    # Espera y maneja la ventana emergente de guardar datos de dirección
    save_address_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "save_address_button_id")))
    save_address_button.click()
except NoSuchElementException:
    # Si la ventana emergente no aparece, continúa con el flujo normal
    pass

# Continúa con el resto de tu test case


#Probar que sea visible la pagina de exito de creacion de cuenta


try:
    create_account_page_visible = WebDriverWait(driver, 5).until(EC.url_to_be('http://automation.com/account_created'))
except TimeoutException:
    message = "The account creation page is not visible"
    mesage2=driver.
    message1=driver.page_source("¿Guardar Dirección?")
    screen = driver.get_screenshot_as_base64()
    raise TimeoutException(message, screen)
assert driver.page_source == "Account Created!", " The account creation page is not visible"

"""
create_account_page_visible = WebDriverWait(driver, 10)#.until(EC.url_to_be('http://automation.com/account_created'))
print(driver.current_url)
assert driver.current_url == "https://automationexercise.com/account_created", " The account creation page is not visible"
print("Test Case Create Account - Pass")


#Probar boton de "continue"

continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form > div > div > div > div > a')))
continue_button.click()

#Comprobar que est'a Logged with the new account

logged_account = WebDriverWait(driver, 10).until(EC.url_to_be('https://automationexercise.com/'))
print(driver.current_url)
assert driver.current_url== "https://automationexercise.com/", "The account is not logged"
print("Test Case Login - Pass")

#Delete account

delete_account = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(5) > a')))
delete_account.click()


#comprobar que est'e visible la pagina de exito de eliminacion de cuenta

delete_account_page_visible = WebDriverWait(driver, 10).until(EC.url_to_be('https://automationexercise.com/delete_account'))
print(driver.current_url)
assert driver.current_url== "https://automationexercise.com/delete_account", "The account deletion page is not visible"
print("Test Case Delete Account - Pass")

#Probar boton de "continue"
continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form > div > div > div > div > a')))
continue_button.click()

#Page return to main

return_to_main= WebDriverWait(driver, 10).until(EC.url_to_be("https://automationexercise.com/"))
assert driver.current_url == "https://automationexercise.com/", "The page is not returned to main"
print("Test Case Return to main", driver.current_url, " Pass")

time.sleep(5)

print("Test Complete Successfully")

driver.quit()
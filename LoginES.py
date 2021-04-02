from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = '/Users/foxhead43/Documents/Universidad/2021/cripto/chromedriver'
driver = webdriver.Chrome(driver_path, chrome_options=options)

driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)


driver.get('https://sniker.es')
options.add_experimental_option('excludeSwitches',['enable-automation'])

wait = WebDriverWait(driver, 10)


documents = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "MI CUENTA")))
documents.click()

correo = driver.find_element_by_id("username")
correo.send_keys("cripto2021udp@gmail.com")
pass1 = driver.find_element_by_id("password")
pass1.send_keys("Cuentafake2021")

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.woocommerce-button.button.woocommerce-form-login__submit')))\
    .click()

driver.quit()


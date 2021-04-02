from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time



options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = '/Users/foxhead43/Documents/Universidad/2021/cripto/chromedriver'
driver = webdriver.Chrome(driver_path, chrome_options=options)

driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)

driver.get('https://www.efas.cl')
options.add_experimental_option('excludeSwitches',['enable-automation'])
wait = WebDriverWait(driver, 10)

documents = wait.until(EC.element_to_be_clickable((By.ID, "menu-item-418")))
documents.click()

correo = driver.find_element_by_id("reg_email")
correo.send_keys("cripto2021udp@gmail.com")
pass1 = driver.find_element_by_id("reg_password")
pass1.send_keys("Cuentafake2021")

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.woocommerce-Button.woocommerce-button.button.woocommerce-form-register__submit')))\
    .click()

driver.quit()

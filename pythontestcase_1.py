from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://sso.teachable.com/secure/9521/identity/sign_up/otp?wizard_id=OXLIeWj1KGw8xRppfEp__qKCp1RbUqLoBblOzrT5sVvbdTwIB8gs7RXqDGCBw6p0M3sI9vEFIJzIA7_wMwxYFg")

driver.find_element(By.ID,"name").send_keys("Rafie Hayat")
driver.find_element(By.ID,"email").send_keys("rafiehayat5@gmail.com")

driver.find_element(By.CSS_SELECTOR,"button[type='button']").click()


time.sleep(10)

# driver.quit()
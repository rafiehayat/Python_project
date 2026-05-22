from selenium import webdriver
from selenium.webdriver.common.by import By
import time


cd = webdriver.Chrome()


cd.get("https://rahulshettyacademy.com/client/#/auth/login")
time.sleep(2)


cd.find_element(By.LINK_TEXT,"Forgot password?").click()

cd.find_element(By.XPATH,"//input[@placeholder='Enter your email address']").send_keys("demo@gmail.com")
cd.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("Demo@2345")
cd.find_element(By.ID,"confirmPassword").send_keys("Demo@2345")

cd.find_element(By.XPATH,"//button[text()='Save New Password']").click()


time.sleep(10)

cd.quit()
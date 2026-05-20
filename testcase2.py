from selenium import webdriver
from selenium.webdriver.common.by import By
import time


cd = webdriver.Chrome()


cd.get("https://rahulshettyacademy.com/angularpractice/")

cd.find_element(By.NAME,"name").send_keys("Rafie Hayat")
cd.find_element(By.NAME,"email").send_keys("Rafiehayat5@gmail.com")
cd.find_element(By.ID,"exampleInputPassword1").send_keys("Hayat@2580")
cd.find_element(By.ID,"exampleCheck1").click()

cd.find_element(By.XPATH,"//input[@type='submit']").click()

message = cd.find_element(By.CLASS_NAME, "alert-success").text
print(message)


time.sleep(10)

cd.quit()
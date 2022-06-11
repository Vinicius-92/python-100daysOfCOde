from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = "/home/viniciussilva/Documentos/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(service=Service(path))


driver.get("https://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Vinicius")
lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Augusto")
email = driver.find_element(By.NAME, "email")
email.send_keys("vinicius92as@gmail.com")
sing_up_btn = driver.find_element(By.CLASS_NAME, "btn")
sing_up_btn.click()


# driver.quit()

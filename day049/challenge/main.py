from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = "/home/viniciussilva/Documentos/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(service=Service(path))

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_WT=2&keywords=c%23")

login = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
login.click()

user_name = driver.find_element(By.ID, "username")
user_name.send_keys("dummyemail@email.com")

password = driver.find_element(By.ID, "password")
password.send_keys("dummypass")

btn_login = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
btn_login.click()

first_job_on_list = driver.find_element(By.CLASS_NAME, "job-card-container__link")
first_job_on_list.click()

save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
save_button.click()


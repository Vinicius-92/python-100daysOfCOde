import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

IG_USERNAME = "dummy"
IG_PASSWORD = "dummypass"

path = "/home/viniciussilva/Documentos/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(service=Service(path))

driver.get("https://www.instagram.com/")

time.sleep(3)

username_input = driver.find_element(By.NAME, "username")
username_input.send_keys(IG_USERNAME)

password_input = driver.find_element(By.NAME, "password")
password_input.send_keys(IG_PASSWORD)

login_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
login_button.click()

time.sleep(3)

dont_save_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')
dont_save_button.click()

time.sleep(3)

driver.find_element(
    By.XPATH,
    '//*[@id="mount_0_0_hy"]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]'
).click()


time.sleep(3)

driver.find_element(
    By.XPATH,
    '//*[@id="mount_0_0_hy"]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/div[1]/div/div/svg/path'
).click()

input_search = driver.find_element(
    By.XPATH,
    '//*[@id="mount_0_0_hy"]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input'
)
input_search.send_keys("Uncle Roger")

time.sleep(3)

first_result = driver.find_element(
    By.XPATH,
    '//*[@id="f3e8db95f1be3dc"]/div/div'
)
first_result.click()

time.sleep(3)

followers_link = driver.find_element(
    By.XPATH,
    '//*[@id="mount_0_0_hy"]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div'
)
followers_link.click()

time.sleep(3)

list_of_followers = driver.find_elements(By.CSS_SELECTOR, 'li div div div button')
for follower in list_of_followers:
    follower.click()
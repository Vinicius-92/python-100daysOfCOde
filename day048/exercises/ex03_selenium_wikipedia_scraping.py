from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = "/home/viniciussilva/Documentos/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(service=Service(path))


driver.get("https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal#")

# articles = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/div[1]/div/div[1]/table/tbody/tr/td[2]/div/p/b[1]')
# print(int(articles.text.replace(" ", "")))

# articles = driver.find_element(By.LINK_TEXT, "artigos")
# articles.click()

input_search = driver.find_element()



# driver.quit()

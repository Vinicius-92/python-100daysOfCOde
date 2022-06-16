import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


FORMS_LINK = "https://forms.gle/7bdzMEuKtzRfwJcd6"
URL_ZILLOW_WITH_PARAMS = "https://www.encurtador.com.br/cyR19"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
    "Accept-Language": "en-US"
}

content = requests.get(URL_ZILLOW_WITH_PARAMS, headers=HEADERS)
soup = BeautifulSoup(content.text, "html.parser")

addresses_html = soup.find_all(name="address", class_="list-card-addr")
addresses = []
for art in addresses_html:
    addresses.append(art.getText())

prices_html = soup.find_all(name="div", class_="list-card-price")
prices = []
for price in prices_html:
    prices.append(price.getText())

prices_html = soup.find_all(name="div", class_="list-card-price")
prices = []
for price in prices_html:
    prices.append(price.getText())

links_html = soup.find_all(name="a", class_="list-card-link list-card-link-top-margin")
links = []
for link in links_html:
    links.append(link.get("href"))


path = "/home/viniciussilva/Documentos/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(service=Service(path))

for i in range(len(addresses)):
    driver.get(FORMS_LINK)
    time.sleep(1)

    first_ = driver.find_element(
        By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    first_.send_keys(addresses[i])

    price_ = driver.find_element(
        By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_.send_keys(prices[i])

    link_ = driver.find_element(
        By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    if i < len(links):
        link_.send_keys(links[i])
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()

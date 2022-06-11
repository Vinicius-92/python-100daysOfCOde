from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = "/home/viniciussilva/Documentos/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(service=Service(path))

# driver.get("https://www.amazon.com.br/Panela-El%C3%A9trica-Oster-CKSTRC4723-017-Vermelho/dp/B0748VSP1S/ref=sr_1_11"
#            "?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2FNNC2UMPHKEB&keywords=rice+cooker&qid=1654814387"
#            "&sprefix=rice+cooke%2Caps%2C223&sr=8-11&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147")
# price_whole = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# print(f"{price_whole.text},{price_cents.text}")
#
# search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
# print(search_bar.get_attribute("value"))

driver.get("https://python.org/")

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)
#
# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)
#
# by_xpath = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[4]/a')
# print(by_xpath.text)

event_times = driver.find_elements(By.CLASS_NAME, "event-widget time")
event_names = driver.find_elements(By.CLASS_NAME, "event-widget li a")

events = {}
for e in range(len(event_times)):
    events[e] = {"time": event_times[e].text, "name": event_names[e].text}

print(events)

driver.quit()

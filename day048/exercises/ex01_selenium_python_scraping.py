from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = "/home/viniciussilva/Documentos/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(service=Service(path))

# Enters python.org, select upcoming events in home and create a dict

driver.get("https://python.org/")
event_times = driver.find_elements(By.CLASS_NAME, "event-widget time")
event_names = driver.find_elements(By.CLASS_NAME, "event-widget li a")

events = {}
for e in range(len(event_times)):
    events[e] = {"time": event_times[e].text, "name": event_names[e].text}

print(events)

driver.quit()
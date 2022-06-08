import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all(name="h3", class_="title")

with open("movies_to_watch.txt", "w") as file:
    for title in titles[::-1]:
        file.write(f"{title.getText()}\n")

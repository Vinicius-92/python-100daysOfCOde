from bs4 import BeautifulSoup
# import lxml # For some cases html.parser won't be enough, so lxml can be used

with open("website.html", "r") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
print(soup.title)
print(soup.title.string)
print(soup.prettify())
print(soup.h1)

anchor = soup.find_all(name="a")
print(anchor)
for tag in anchor:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(selector=".headings")
print(headings)

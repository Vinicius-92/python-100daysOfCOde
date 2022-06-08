from bs4 import BeautifulSoup
import requests

content = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(content.text, "html.parser")

articles = soup.find_all(name="a", class_="titlelink") 
article_texts = []
article_links = []
for tag in articles:
    text = tag.getText()
    link = tag.get("href")
    article_texts.append(text)
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

index_higher_upvoted_article = article_upvotes.index(max(article_upvotes))

print(article_texts[index_higher_upvoted_article])
print(article_links[index_higher_upvoted_article])
print(article_upvotes[index_higher_upvoted_article])

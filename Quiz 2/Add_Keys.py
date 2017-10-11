import os
from bs4 import BeautifulSoup as BS
path = r"C:\Users\CCrowe\Documents\Modern Software Methodologies\Quiz 2\Study_Sheet.html"


class Article():
    def __init__(self,title,body):
        self.title = title
        self.body = body

l = []

with open(path,"r") as f:
    text = f.read()
    soup = BS(text)
    for article in soup.find_all("article"):
        title = article.find_all("strong")
        title_text = title[0].text
        art = Article(title_text,str(article))
        l.append(art)

l.sort(key=lambda x: x.title, reverse=True)

failed = []
text = ""
new_path = r"C:\Users\CCrowe\Documents\Modern Software Methodologies\Quiz 2\Study_Sheet_alphabetized.html"
with open(new_path,"w") as f:
    for x in l:
        text += x.body
    f.write(text)

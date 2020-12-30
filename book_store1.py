import requests
from bs4 import BeautifulSoup

URL = "http://books.toscrape.com/catalogue/page-"
HTML_EXT = ".html"

for p in range(50): #there are 50 pages
   pageNumber = p + 1
   url = URL + str(pageNumber) + HTML_EXT
   print("########## Page " + str(pageNumber) + " ##########")
   page=requests.get(url)
   soup = BeautifulSoup(page.content, 'html.parser')

   for link in soup.find_all("a"):
      if link.get("title") is not None:
         print("Book title: {}".format(link.get("title")))

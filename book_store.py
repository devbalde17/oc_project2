import requests
import pandas as pd
from bs4 import BeautifulSoup as bs4

baseurl ='http://books.toscrape.com/'
pages = []
product_page_urls = []
titles = []
image_urls = []
review_ratings = []



pages_to_scrape = 50

# getting the urls for all 50 pages
for i in range(1, pages_to_scrape+1):
    url = ('http://books.toscrape.com/catalogue/page-{}.html').format(i)
    pages.append(url)

#creating a soup object to a book information
for item in pages:
   page = requests.get(item)
   soup = bs4(page.text, 'html.parser')
   print(soup.prettify())
#creating a titles list by getting all the titles for page1
   for i in soup.findAll('h3'):
      title = i.getText()
      titles.append(title)


   product_list = soup.find_all('div', class_="image_container")
   for image_container in product_list:
      for urls in image_container.find_all('a', href=True):
         prod_url = 'http://books.toscrape.com/catalogue/' + urls['href']
         product_page_url = prod_url.replace("../", "")
         product_page_urls.append(product_page_url)



   image_url = soup.find_all('div', class_="image_container")
   for image in image_url:
      tgs=image.find('img', class_="thumbnail")
      img_url = 'http://books.toscrape.com/' +str(tgs['src'])
      imgs_urls = img_url.replace("../", "")
      image_urls.append(imgs_urls)

   for r in soup.find_all("p", class_="star-rating"):
      for k, v in r.attrs.items():
         star = v[1]
         review_ratings.append(star)


dict = {'product_page_url': product_page_urls, 'title': titles,
    'image_url': image_urls, 'review_rating': review_ratings,
    }

print(dict)


df = pd.DataFrame(data=dict)
df.index+=1
print(df)
df.to_excel("/Users/balde/Webscraping/output.xlsx")

print(df)

import requests
from bs4 import BeautifulSoup
<<<<<<< HEAD
import pandas as pd
import csv

baseurl = 'http://books.toscrape.com/'

headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}



product_url = []

r = requests.get('http://books.toscrape.com/catalogue/category/books/health_47/index.html')
soup = BeautifulSoup(r.content, 'lxml')
product_list = soup.find_all('div', class_="image_container")
for image_container in product_list:
    for urls in image_container.find_all('a', href=True):
        product_url.append(baseurl + urls['href'])
    prod_url = 'http://books.toscrape.com/catalogue/'+urls['href']
    product_page_url = prod_url.replace("../","")
    
        

        
            
        


for urls in product_url:
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.content, 'lxml')
    
    product_page_url = 'http://books.toscrape.com/catalogue/10-day-green-smoothie-cleanse-lose-up-to-15-pounds-in-10-days_581/index.html'

    title = soup.find('li', class_='active').text.strip()
    


    product_description = soup.find("p", class_=None).text.strip()
    print(product_description)

   

    for r in soup.find_all("p", class_="star-rating Five"):
        for k, v in r.attrs.items():
            star = v[1]
    
        
    image_urls = soup.find_all('img', limit=1)
    for image in image_urls:
    
        img_url = 'http://books.toscrape.com/'+image['src']
        image_url = img_url.replace("../","")

    

    book = {
        'product_page_url':product_page_url,
        'title':title,
        'product_description':product_description,
        'star':star,
        'image_url':image_url
            }
    df = pd.DataFrame(book)
    print(df)
 

      
   

    



    
    
        
     

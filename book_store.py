import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('http://books.toscrape.com/catalogue/10-day-green-smoothie-cleanse-lose-up-to-15-pounds-in-10-days_581/index.html')
soup = BeautifulSoup(page.content, 'html.parser')


#building a dictionary
product_page_url=[]
universal_product_code=[]
title=[]
price_including_tax=[]
price_excluding_tax=[]
number_available=[]
product_description=[]
category=[]
review-rating=[]
image_url=[]

#get the product information
product_information = soup.find('table', {'class': 'table table-striped'}).get_text()
print(product_information)

#get the product description
product_description = soup.find("p", class_=None).get_text()
print(product_description)



# Trying a different way to get the image_url
image_url = soup.find_all('img', limit=1)
for image in image_url:
   print(image['src'])

# trying to organize the data

data = {'Product_page': product_page_url, 'upc': universal_ product_code, 'Title': title, 'Price_i_tax': price_including_tax,
'Price_e_tax': price_excluding_tax, 'Number' : number_available, 'Product': product_description, 'Category': category, 'Rating': review_rating,
'Image': image_url}

df=pd.DataFrame(data=data)
print(df)

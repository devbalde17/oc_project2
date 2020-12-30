import requests
from bs4 import BeautifulSoup
page = requests.get('http://books.toscrape.com/catalogue/10-day-green-smoothie-cleanse-lose-up-to-15-pounds-in-10-days_581/index.html')
soup = BeautifulSoup(page.content, 'html.parser')


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


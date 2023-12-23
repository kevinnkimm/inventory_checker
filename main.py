import requests
from bs4 import BeautifulSoup

# checks inventory

def checkInventory(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')


# indicate a specific class using inspect element of where the in stock/out of stock could be located
    inventory_status = soup.find(class_='a-size-medium a-color-success').get_text()

    if "Add to Cart" in inventory_status:
            print("Item is in stock!")
    
    else:
            print("Item is out of stock.")

url = 'https://www.bestbuy.ca/en-ca/product/hp-15-6-laptop-natural-silver-intel-core-i5-1235u-512gb-ssd-16gb-ram-windows-11-home/17210546'
checkInventory(url)

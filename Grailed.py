__author__ = 'phillipblack'

import sys;
reload(sys);
sys.setdefaultencoding("utf8")

from bs4 import BeautifulSoup
import requests

import re
import csv

url = 'http://www.grailed.com/listings/202770'

#Request content from webpage
result = requests.get(url)
c = result.content

#Set as Beautiful Soup Object
soup = BeautifulSoup(c)

#title of item
h1 = soup.find_all('h1')
title = str(h1[0].get_text())
print title

#size of item
h2 = soup.find_all('h2',{'class':'title'})
item_size = str(h2[0].get_text())
print item_size

#get listing price
listing_price_div = soup.find('li', {'class': 'horizontal-list-item price'})
listing_price_text = listing_price_div.get_text()
listing_price = listing_price_text.strip()
print listing_price

#number of people following item
followers_div = soup.find('div',{'class':'listing-followers'})
followers_p = followers_div.find('p')
followers_text = followers_p.get_text()
followers  = re.sub("[^0-9]", "",followers_text)
print followers

#listing description
div_desc = soup.find('div',{'class':'listing-description'})
desc_text = div_desc.get_text()
desc = desc_text.strip()
print desc

#shipping price
shipping_div = soup.find('div',{'class':'listing-shipping'})
shipping_tag = shipping_div.find('p')
shipping_text = shipping_tag.get_text()
shipping = shipping_text.strip()
print shipping

#Number of items in user's wardrobe
seller_info = soup.find('div',{'class':'user-widget medium'})
seller_wardrobe = seller_info.find('a')
seller_wardrobe_text = seller_wardrobe.get_text()
seller_wardrobe = re.sub("[^0-9]", "",seller_wardrobe_text)
print seller_wardrobe

#number of Grailed products user has bought and sold
bought_sold_p = soup.find('p',{'class':'bought-and-sold'})
bought_sold_text = bought_sold_p.get_text()
bought_sold = re.sub("[^0-9]", "",bought_sold_text)
print bought_sold


f = csv.writer(open('grailed.csv','w'))
f.writerow(["Title","Size","ListingPrice","PeopleFollowing","ListingDescription","ShippingPrice","WardrobeItems","Bought&Sold"])
rowout = [title, item_size, listing_price, followers, shipping, seller_wardrobe, bought_sold]
print rowout

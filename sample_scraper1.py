"""
Author: UPQUARK00
Scraper Specimen 1
Created on Sat Dec  1 13:33:29 2018
"""

import csv
import requests as rs
from bs4 import BeautifulSoup as bs
from time import sleep
from random import randint as rit

# Open a .CSV file to which all item information will be written
file = open('retail_sheet.csv', 'w', newline= '',encoding='utf-8')
retail_sheet_writer = csv.writer(file)

# Begin defining labels that will head .CSV file; adds custom labels later
header_labels = ['Retailer','Name']

# =============================================================================
# This section determines number of items in listing and iterates through pages
# =============================================================================

SCRAPER_ON = True 

# Set start url
url_base = 'http://__secret__url[offset]=' 
url = url_base + '0'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

# Get information from page when ON; limits accidental server bombardment
if SCRAPER_ON:
    html = rs.get(url, headers = headers, timeout = 5)
    print('SCRAPER ON!')
    
# Parse the html text
soup = bs(html.text, 'lxml')

# Pulls and names product specification categories
detail_names = soup.find_all('table', class_= 'prod_sheet')[0].find('div', class_='section_overview').find_all('span', class_ = 'cat_overview_spec_name')
for detail_name in detail_names:
    header_labels.append(str(detail_name.text.rstrip(':')))

# Find the total number of products available across all pages
total = soup.find('div', id = 'index').find('table', class_='temp').find('p')
total = int(''.join(filter(str.isdigit, total.text)))
print('Products:',total)

def find_last_page_offset(total_items, items_per_page):
# Offset is a parameter in the url which tracks page # in a series of pages
# This function yields the offset of the last page of items listed after a search
# total_items = number of items found in the website search (of a specified name)
# items_per_page = quantity of products on each page
    last_page_offset = total_items - (total_items % items_per_page)
    print('Last page offset:', last_page_offset)
    return last_page_offset

last_page_offset = find_last_page_offset(total, 20)

# Iterate through, and gather information from, all pages in determined range
for offset in range(0, last_page_offset+20, 20):
    url = url_base + str(offset)
    html = rs.get(url)
    soup = bs(html.text, 'lxml')

# =============================================================================
# This section grabs data from each page and writes to the .CSV file
# =============================================================================

    # Iterate through each item listing in the page
    all_products = soup.find_all('table', class_= 'sec_sheet_over')
    
    for product in all_products: 
        product_name = product.find(class_ = 'name').text
        product_brand = product.find(class_ = 'brand').text
                
        # Pull and define product specifications
        product_details = product.find('div', class_='section_overview').find_all('span', class_ = 'value_spec')            
        product_details = [product_detail.text for product_detail in product_details]
        
        price_info = product.find('div', class_= 'product_price')
        
        try:
            price = price_info.find('span', class_= 'reg_price').text
            rebate_available = 'Available'
            rebate_value = price_info.find('span', class_= 'rebate_item_no').text.strip()
            
        except AttributeError:
            try:
                price = price_info.find('p', class_='price_reg_over').text.strip()
                #print('NO REBATE PRICE', price,product_name,'xxxx')
                rebate_available = 'None'
                rebate_value = 'N/A'
            except:        
                price = 'Price not available'
        
        # Insert headers for items in the retail_sheet.csv file on first pass        
        if offset == 0 and product is all_products[0]:
            for new_header in ['Price', 'Rebate', 'Rebate Value']:
                header_labels.append(new_header)
            retail_sheet_writer.writerow(header_labels)

        # print('**********************',type(price))
        # Define the blank row to be written into the .CSV file. 
        row_contents = [product_brand, product_name] 
        row_contents += product_details
        row_contents += [price, rebate_available, rebate_value]
            
        # Write items pertaining to one product into a row in the .CSV file
        retail_sheet_writer.writerow(row_contents)
    
# Close the file to ensure proper file save
file.close()


       


#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing the important libraries
import os
import requests
import re
from bs4 import BeautifulSoup
import csv


# In[2]:


def restaurant_info(url_list, output_csv):
    
    allreviews = []

    for u in url_list:
        response = requests.get(u)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            restaurant_name = soup.find('h1', class_='css-1se8maq').text.strip()
            total_reviews = soup.find('a', class_='css-19v1rkv').text.strip()

            reviews = soup.find_all('li', class_='css-1q2nwpv')
            for review in reviews:
                review_text = review.find('span', {'lang': 'en'}).text.strip()
                reviewer = review.find('a', class_='css-19v1rkv').text.strip()
                rating = review.find('div', class_='five-stars__09f24__mBKym five-stars--regular__09f24__DgBNj css-1jq1ouh')['aria-label'].split()[0]
                allreviews.append([restaurant_name, total_reviews, review_text, reviewer, rating])
        
        else:
            print(f'Failed to retrieve data from {url}')

    with open(output_csv, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Restaurant Name', 'Total Reviews', 'Review Text', 'Reviewer', 'Rating'])
        writer.writerows(allreviews)
        print(f'Restaurant information have been saved to {output_csv}')
    

output_csv_file = 'Restaurant_Reviews.csv'


restaurant_list = ['https://www.yelp.ca/biz/pai-northern-thai-kitchen-toronto-5?osq=Restaurants',
                   'https://www.yelp.ca/biz/mira-toronto?osq=Restaurants',
                   'https://www.yelp.ca/biz/katsuya-toronto-5?osq=Restaurants',
                   'https://www.yelp.ca/biz/gusto-101-toronto?osq=Restaurants',
                   'https://www.yelp.ca/biz/the-rabbit-hole-toronto?osq=Restaurants'
                   ]

restaurant_info(restaurant_list, output_csv_file)


# In[ ]:





# Yelp-Restaurant-Review-Web-Scraping

This Python script is designed to scrape restaurant review data from Yelp using the BeautifulSoup library. It extracts information such as restaurant names, total reviews, individual review texts, reviewers, and ratings for a list of Yelp restaurant URLs.

## Table of Contents
1. [Dependencies](#dependencies)
2. [How to Use](#how-to-use)
3. [Output](#output)
4. [Sample Restaurant List](#sample-restaurant-list)

## Dependencies
Before using this script, you need to make sure you have the following dependencies installed:
- Python (3.6+)
- BeautifulSoup4
- requests

You can install BeautifulSoup and requests using pip:

```bash
pip install beautifulsoup4 requests
```
## How to Use
1. Clone or download this repository to your local machine.
2. Open the script yelp_scraper.py in a code editor or IDE.
```python
# Importing the important libraries
import os
import requests
import re
from bs4 import BeautifulSoup
import csv
```
3. Modify the restaurant_list variable with the list of Yelp restaurant URLs you want to scrape. You can add or remove URLs as needed.
```python
restaurant_list = [
    'https://www.yelp.ca/biz/pai-northern-thai-kitchen-toronto-5?osq=Restaurants',
    'https://www.yelp.ca/biz/mira-toronto?osq=Restaurants',
    'https://www.yelp.ca/biz/katsuya-toronto-5?osq=Restaurants',
    # Add more URLs here
]
```
4. Specify the output CSV file name where the scraped restaurant information will be saved. You can change the output_csv_file variable if needed.
```python
output_csv_file = 'Restaurant_Reviews.csv'
```
5. Run the script. It will scrape the restaurant information and save it to the specified CSV file.
```python
python yelp_scraper.py
```

##Output
The script will create a CSV file containing the following columns:

-Restaurant Name
-Total Reviews
-Review Text
-Reviewer
-Rating

The scraped data for each restaurant will be stored as rows in the CSV file.

This README provides an overview of the web scraping script's functionality and how to use it. Please refer to the script comments for more details on its implementation.

## Contributors

- Kumud Kohli - [GitHub Profile](https://github.com/kumudkohli)

Feel free to contribute to this project by opening issues or pull requests!

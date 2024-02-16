import requests
from bs4 import BeautifulSoup

# Set the URL for the New York Times financial news page
url = 'https://www.nytimes.com/section/business/dealbook'

# Make a request to the page
page = requests.get(url)

# Parse the HTML of the page
soup = BeautifulSoup(page.content, 'html.parser')

# Find all article elements on the page
articles = soup.find_all('article')

# Print the headlines of the articles
for article in articles:
    headline = article.find('h2').text
    print(headline)
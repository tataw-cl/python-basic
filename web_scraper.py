import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://quotes.toscrape.com"

try:
    # Send a GET request to the website
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Raise an exception for bad status codes
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all quotes on the page
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    
    # Extract and print the data
    print("Scraping quotes from: " + url)
    print("=" * 50)
    
    for quote, author in zip(quotes, authors):
        quote_text = quote.get_text()
        author_text = author.get_text()
        print(f"\nQuote: {quote_text}")
        print(f"Author: {author_text}")
    
    print("\n" + "=" * 50)
    print(f"Total quotes scraped: {len(quotes)}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching the website: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

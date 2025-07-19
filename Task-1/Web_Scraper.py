import requests
from bs4 import BeautifulSoup

def fetch_quotes(url):
    """
    Fetches quotes and authors from the provided URL using BeautifulSoup.

    Args:
        url (str): The URL to scrape.

    Returns:
        list[tuple[str, str]]: A list of (quote, author) tuples.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad status
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    quote_blocks = soup.find_all('div', class_='quote')

    scraped_data = []
    for quote in quote_blocks:
        text = quote.find('span', class_='text').get_text(strip=True)
        author = quote.find('small', class_='author').get_text(strip=True)
        scraped_data.append((text, author))

    return scraped_data


def display_quotes(quotes):
    """
    Displays the scraped quotes and authors.

    Args:
        quotes (list): List of (quote, author) tuples.
    """
    print("\nExtracted Quotes:\n")
    for i, (quote, author) in enumerate(quotes, start=1):
        print(f"{i}. \"{quote}\" — {author}")


def main():
    print("Web Scraper: Quotes to Scrape")
    url = "https://quotes.toscrape.com"
    quotes = fetch_quotes(url)
    
    if quotes:
        display_quotes(quotes)
    else:
        print("No quotes found or an error occurred.")


if __name__ == "__main__":
    main()

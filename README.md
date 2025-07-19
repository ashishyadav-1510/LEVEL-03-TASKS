# Task - 1 : Web Scraper: Quotes to Scrape

This Python script scrapes quotes and their respective authors from the website [quotes.toscrape.com](https://quotes.toscrape.com). It uses `requests` for fetching the webpage and `BeautifulSoup` for parsing and extracting data.

## Features

* Extracts quotes and authors from the web page.
* Displays them in a clean, numbered format.
* Handles HTTP and connection errors gracefully.

## Technologies Used

* Python 3
* [requests](https://pypi.org/project/requests/)
* [BeautifulSoup (bs4)](https://pypi.org/project/beautifulsoup4/)

## Installation

Clone this repository:
git clone https://github.com/yourusername/quote-web-scraper.git
cd quote-web-scraper

Install dependencies:
pip install requests beautifulsoup4

## Usage

Run the script using:
python quotes_scraper.py

Sample Output:
Web Scraper: Quotes to Scrape

Extracted Quotes:

1. "The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking." — Albert Einstein
2. "It is our choices, Harry, that show what we truly are, far more than our abilities." — J.K. Rowling
   ...

## How It Works

### 1. `fetch_quotes(url)`

* Sends an HTTP GET request to the specified URL.
* Parses the HTML to find all `div` elements with the class `quote`.
* Extracts the quote text and author for each block and returns a list of tuples.

### 2. `display_quotes(quotes)`

* Loops through the list of tuples.
* Prints the quotes with a serial number in a readable format.

### 3. `main()`

* Main function to call the above functions and handle empty or error cases.

## Screenshot

### Code:

![image](https://github.com/ashishyadav-1510/LEVEL-03-TASKS/blob/main/Task-1/Screenshot%202025-07-18%20220906.png?raw=true)

### Output:

![image](https://github.com/ashishyadav-1510/LEVEL-03-TASKS/blob/main/Task-1/Screenshot%202025-07-18%20220924.png?raw=true)

## Video

[Video](https://youtu.be/tcS5228ZosU)

## Explanation

import requests
from bs4 import BeautifulSoup
requests: Used to send HTTP requests to the website.
BeautifulSoup (from bs4): Used to parse and extract data from HTML content.

def fetch_quotes(url):
    """
    Fetches quotes and authors from the provided URL using BeautifulSoup.
    Args:
        url (str): The URL to scrape.
    Returns:
        list[tuple[str, str]]: A list of (quote, author) tuples.
    """
Defines a function fetch_quotes that accepts a URL.
It returns a list of tuples, where each tuple contains a quote and its author.

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad status
Sends a GET request to the URL.
raise_for_status() throws an exception for HTTP errors (e.g., 404, 500).

    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []
If there’s any issue with the request (timeout, invalid URL, etc.), an error message is printed.
The function returns an empty list to indicate failure.

    soup = BeautifulSoup(response.text, 'html.parser')
response.text contains the raw HTML content of the page.
BeautifulSoup parses this HTML using the built-in 'html.parser'.

    quote_blocks = soup.find_all('div', class_='quote')
Finds all div elements with class quote (each quote is inside such a div).

    scraped_data = []
Initializes an empty list to store the (quote, author) pairs.

    for quote in quote_blocks:
        text = quote.find('span', class_='text').get_text(strip=True)
        author = quote.find('small', class_='author').get_text(strip=True)
        scraped_data.append((text, author))
Iterates through each quote block.
quote.find('span', class_='text'): Finds the actual quote text.
get_text(strip=True): Extracts clean text by removing leading/trailing whitespace.
quote.find('small', class_='author'): Finds the author of the quote.
Appends the (quote_text, author) as a tuple to scraped_data.

    return scraped_data
Returns the list of all scraped (quote, author) pairs.

def display_quotes(quotes):
    """
    Displays the scraped quotes and authors.
    Args:
        quotes (list): List of (quote, author) tuples.
    """
Defines a function display_quotes that accepts a list of (quote, author) tuples.

    print("\nExtracted Quotes:\n")
Prints a header before showing the quotes.

    for i, (quote, author) in enumerate(quotes, start=1):
        print(f"{i}.\"{quote}\" — {author}")
Loops through the list with an index i starting from 1.

Prints each quote in a numbered format:

1. "Quote text" — Author Name

def main():
    print("Web Scraper: Quotes to Scrape")
Defines the main() function.
Prints a title for the program.

    url = "https://quotes.toscrape.com"
URL to scrape quotes from.

    quotes = fetch_quotes(url)
Calls the fetch_quotes function and stores the result in quotes.

    if quotes:
        display_quotes(quotes)
    else:
        print("No quotes found or an error occurred.")
If quotes were successfully fetched, they are displayed.
Otherwise, an error message is printed.

if __name__ == "__main__":
    main()
This ensures the script runs only when it is executed directly (not when imported).
Calls the main() function to start the program.



# Task - 3 : Automated Sales Report Generator

This Python script automates the process of creating a detailed **sales report** from a CSV file. It generates a sample dataset (if missing), processes it, and creates a neatly formatted sales summary report in a `.txt` file.

## Features

* Automatically creates a sample `sales_data.csv` if not present
* Computes total sales and sales by category
* Generates a well-formatted, human-readable `sales_report.txt`
* Handles missing/invalid data rows with warnings
* Adds current timestamp to the report

## Files

| File                 | Description                                 |
| -------------------- | ------------------------------------------- |
| `sales_data.csv`   | Input data file (auto-generated if needed)  |
| `sales_report.txt` | Output report file with detailed sales info |
| `main_script.py`   | Main Python script (your provided code)     |

## Technologies Used

* Python 3
* Built-in modules: `csv`, `os`, `datetime`, `collections`

## How to Run

## Sample Output (`sales_report.txt`)

## Function Breakdown

### `generate_sample_csv()`

* Creates a CSV with sample sales data if `sales_data.csv` doesn’t exist.

### `read_csv_and_generate_report()`

* Parses the CSV, calculates:
  * Total sales
  * Category-wise breakdown
* Writes results to `sales_report.txt` in a structured format.

### `main()`

* Driver function that runs both generation and reporting tasks.

## Screenshot

### Code:

![image](https://github.com/ashishyadav-1510/LEVEL-03-TASKS/blob/main/Task-3/Screenshot%202025-07-19%20055109.png?raw=true)
![image](https://github.com/ashishyadav-1510/LEVEL-03-TASKS/blob/main/Task-3/Screenshot%202025-07-19%20055130.png?raw=true)

### Output:

![image](https://github.com/ashishyadav-1510/LEVEL-03-TASKS/blob/main/Task-3/Screenshot%202025-07-19%20055321.png?raw=true)
#### Text file
![image](https://github.com/ashishyadav-1510/LEVEL-03-TASKS/blob/main/Task-3/Screenshot%202025-07-19%20055341.png?raw=true)
#### CSV file
![image](https://github.com/ashishyadav-1510/LEVEL-03-TASKS/blob/main/Task-3/Screenshot%202025-07-19%20055353.png?raw=true)
![image](https://github.com/ashishyadav-1510/LEVEL-03-TASKS/blob/main/Task-3/Screenshot%202025-07-19%20055415.png?raw=true)

## Video

[Video](https://youtu.be/clogAyXBWqg)

## Explanation

import csv
import os
from datetime import datetime
from collections import defaultdict
csv: Used to read and write CSV (Comma-Separated Values) files.
os: Used to interact with the operating system (e.g., to check if a file exists).
datetime: Used to get the current date and time.
defaultdict: A dictionary subclass from collections that provides a default value for missing keys.

generate_sample_csv(): Create a sample CSV if not present

def generate_sample_csv(filename='sales_data.csv'):
    """
    Creates a sample sales CSV file automatically if it doesn't exist.
    """
Defines a function to create a default CSV file named sales_data.csv if it doesn't already exist.

    if os.path.exists(filename):
        print(f"[INFO] File '{filename}' already exists.")
        return
Checks if the file already exists. If it does, the function prints a message and exits.

    sample_data = [
        ['Date', 'Product', 'Category', 'Quantity', 'Unit_Price'],
        ['2025-07-15', 'Laptop', 'Electronics', '3', '45000'],
        ['2025-07-15', 'Pen', 'Stationery', '50', '10'],
        ['2025-07-16', 'Chair', 'Furniture', '5', '1500'],
        ['2025-07-17', 'Notebook', 'Stationery', '30', '25'],
        ['2025-07-17', 'Smartphone', 'Electronics', '2', '20000']
    ]
A list of lists representing the sample sales data (header + rows).

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(sample_data)
        print(f"[SUCCESS] Created sample CSV: {filename}")
Opens the file in write mode ('w') with UTF-8 encoding.
Uses csv.writer to write all the rows to the file.
Prints success message once done.

    except Exception as e:
        print(f"[ERROR] Could not create CSV: {e}")
Catches and displays any exceptions that occur during file writing.

read_csv_and_generate_report(): Read CSV and generate the report

def read_csv_and_generate_report(input_file='sales_data.csv', report_file='sales_report.txt'):
    """
    Processes the CSV file and generates a formatted text report.
    """
Defines a function that reads the CSV and writes the output report to a .txt file.

    if not os.path.exists(input_file):
        print(f"[ERROR] Input file '{input_file}' not found.")
        return
Checks if the input file exists. If not, it prints an error and exits.

    total_sales = 0
    category_sales = defaultdict(float)
    records = []
total_sales: stores the total amount from all transactions.
category_sales: a dictionary to store sales per category (e.g., Electronics, Stationery).
records: list to store all valid data rows for report generation.

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
Opens the CSV file for reading.
Uses DictReader to read rows as dictionaries (with keys from the header).

            for row in reader:
                try:
                    qty = int(row['Quantity'])
                    price = float(row['Unit_Price'])
                    sale = qty * price
                    category = row['Category']
Loops over each row in the CSV.
Converts Quantity and Unit_Price to numeric types.
Calculates total sale amount for that row.

Extracts the Category.

                    total_sales += sale
                    category_sales[category] += sale
Adds the sale to the overall total and the category-specific total.

                    records.append({
                        'Date': row['Date'],
                        'Product': row['Product'],
                        'Category': category,
                        'Quantity': qty,
                        'Unit_Price': price,
                        'Sale': sale
                    })
Stores the processed data into the records list.

                except (ValueError, KeyError) as e:
                    print(f"[WARNING] Skipping row due to error: {e}")
Catches and warns about any row that contains invalid or missing data.

    except Exception as e:
        print(f"[ERROR] Reading CSV failed: {e}")
        return
Catches errors related to file reading or parsing issues.

Write the final sales report

    try:
        with open(report_file, 'w', encoding='utf-8') as report:
            report.write("======= AUTOMATED SALES REPORT =======\n")
            report.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
Opens the report file for writing.
Writes the report title and the current timestamp.

            report.write(f"{'Date':<12}{'Product':<15}{'Category':<15}{'Qty':<5}{'Price':<10}{'Sale':<10}\n")
            report.write("-" * 70 + "\n")
Writes column headers with fixed-width formatting.

Adds a line separator.

            for r in records:
                report.write(f"{r['Date']:<12}{r['Product']:<15}{r['Category']:<15}"
                             f"{r['Quantity']:<5}{r['Unit_Price']:<10.2f}{r['Sale']:<10.2f}\n")
Iterates through the records and writes each transaction in a structured line.

            report.write("\n[SUMMARY]\n")
            report.write(f"Total Sales: ₹{total_sales:.2f}\n")
            report.write("Sales by Category:\n")
Adds a summary section: total sales and a breakdown by category.

            for cat, amount in category_sales.items():
                report.write(f"  - {cat}: ₹{amount:.2f}\n")
            report.write("======================================\n")
Loops through category-wise totals and writes them to the report.

        print(f"[SUCCESS] Report created: {report_file}")
Confirmation message after report creation.

    except Exception as e:
        print(f"[ERROR] Could not write report: {e}")
Handles any file writing errors.

Main driver function

def main():
    print("Automating Sales Report Generation\n")
    generate_sample_csv()  # auto-create file
    read_csv_and_generate_report()  # read + report
The main() function calls both:
generate_sample_csv() to ensure the CSV exists.
read_csv_and_generate_report() to process and report.

Script entry point

if __name__ == "__main__":
    main()
Ensures the main() function runs only when the script is executed directly (not imported).


### Author
***Ashish Yadav***
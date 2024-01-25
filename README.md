# Web Scraping Example

This is a simple Python script that uses the `requests` library to fetch the content of a webpage and `BeautifulSoup` to parse and extract specific information. In this example, the script fetches all the 'href' attributes from 'link' tags on the given webpage (`https://seatable.io/en/online-datenbank-kostenlos/`) and saves them to a file named `example.txt`.

## Requirements
- Python 3.x
- Requests library (`pip install requests`)
- BeautifulSoup (`pip install beautifulsoup4`)

## Setup
1. Install the required dependencies using the following command:
   ```bash
   pip install requests beautifulsoup4
   ```

2. Run the script:
   ```bash
   python your_script_name.py
   ```

3. Open the `links.txt` file to view the extracted URLs.

## Code Explanation
- The script uses the `requests` library to make a GET request to the specified URL.
- `BeautifulSoup` is then used to parse the HTML content.
- It extracts all 'href' attributes from 'link' tags and prints them to the console.
- The script also writes these URLs to a file named `links.txt`.

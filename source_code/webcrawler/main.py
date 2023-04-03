"""This module contains the main function to crawl a web page."""
import requests
from bs4 import BeautifulSoup


def crawl_page(url : str) -> None:
    """Send a GET request to the URL and parse the page content."""
    response = requests.get(url, timeout=5)

    # If the request was successful, process the page content
    if response.status_code == 200:
        # Parse the page content with BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the table with the class "wikitable"
        soup.find("table")
        # Find all the table rows
        table_row = soup.select(".wikitable tbody tr")[1:]
        print("[INFO]: Python types:")
        for element in table_row:
            table_data = element.select("td")[0]
            a_href = table_data.select("a")[0]
            print(a_href.get("title"))
    else:
        print(f"[ERROR]: Failed to fetch the page: {url}")


if __name__ == "__main__":
    WIKI_URL = "https://en.wikipedia.org/wiki/Python_(genus)"
    crawl_page(WIKI_URL)

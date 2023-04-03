"""Webcrawler Example for POST requests"""
import requests
import json


def get_all(url):
    """Get data from a url.

    Args:
        url (str): The URL from where we are reading data

    Returns:
        None
    """
    url_request = requests.get(url, timeout=5)
    print(url_request.text)

def get_id(url, id):
    """Get data from a id.

    Args:
        url (str): The URL from where we are reading data
        id (str): The id that we want to get

    Returns:
        None
    """
    url_request = requests.get(f"{url}/{id}", timeout=5)
    print(url_request.text)

def update_data(url):
    """Update data from a url.

    Args:
        url (str): The URL from where we are reading data

    Returns:
        None
    """
    headers = {"content-type": "application/json"}
    payload = json.dumps(
        {
            "name": "Nothing Phone",
            "data": {"color": "white", "generation": "1st", "price": 400},
        }
    )
    url_request = requests.post(url, data=payload, headers=headers)

    print(url_request.content)


if __name__ == "__main__":
    # Constant declaration
    API_URL = "https://api.restful-api.dev/objects"

    # Fetch the data using a GET request
    print("GET request:")
    get_all(API_URL)
    print("POST request:")
    update_data(API_URL)
    print("GET request from id:")
    get_id(API_URL,"ff808181873cebfc018742688af4004d")
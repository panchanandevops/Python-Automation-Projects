import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
API_KEY = os.getenv("CURRENCY_API_KEY")
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return data["data"]
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except ValueError:
        print("Invalid response received.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

while True:
    # Display supported currencies to the user
    print(f"\nSupported currencies: {', '.join(CURRENCIES)}")
    base = input("Enter the base currency (or 'Q' to quit): ").upper()

    # Check if the user wants to quit
    if base == "Q":
        break

    # Validate if the base currency is in the supported list
    if base not in CURRENCIES:
        print("Invalid currency. Please choose from the supported currencies.")
        continue

    data = convert_currency(base)
    if not data:
        continue

    # Remove the base currency from the output and print the results
    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}: {value}")

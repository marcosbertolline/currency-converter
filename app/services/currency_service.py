import requests, os
from dotenv import load_dotenv

load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv('exchange_api_key')

# Get the conversion rate between two currencies
def get_conversion_rate(base_currency: str, target_currency: str):
    api_url = f"http://api.exchangeratesapi.io/latest?base=EUR&access_key={api_key}"
    response = requests.get(api_url)
    response.raise_for_status()

    rates = response.json().get("rates", {})
    if base_currency == "EUR":
        return rates[target_currency]
    
    # If the base currency is not EUR, we need to convert it to EUR first
    rate_base = rates.get(base_currency)
    rate_target = rates.get(target_currency)
    if rate_base is None or rate_target is None:
        raise ValueError("Currency not supported")
    return rate_target / rate_base

# stocks/services.py

import requests
from datetime import datetime
from .models import StockData
from django.conf import settings

ALPHA_VANTAGE_API_URL = "https://www.alphavantage.co/query"

def fetch_stock_data(symbol):
    """
    Fetch historical stock data from Alpha Vantage and save it to the database.
    """
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'outputsize': 'full',
        'apikey': 'FYYEN13Y4REOFXPD',  # API Key stored in settings
    }

    response = requests.get(ALPHA_VANTAGE_API_URL, params=params)
    data = response.json()
    
    if "Time Series (Daily)" not in data:
        raise Exception("Failed to fetch data or API limit reached")

    # Loop through the daily time series data and store it in the database
    for date_str, price_info in data["Time Series (Daily)"].items():
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        StockData.objects.update_or_create(
            symbol=symbol,
            date=date,
            defaults={
                'open_price': price_info['1. open'],
                'close_price': price_info['4. close'],
                'high_price': price_info['2. high'],
                'low_price': price_info['3. low'],
                'volume': price_info['5. volume']
            }
        )

    return f"Stock data for {symbol} fetched and stored successfully."

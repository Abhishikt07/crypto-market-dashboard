import requests
import pandas as pd
import random
from datetime import datetime
import time

coin_geo_info = {
    'binance': ('China', 'Asia'),
    'coinbase': ('USA', 'North America'),
    'kraken': ('Germany', 'Europe'),
    'bitfinex': ('UK', 'Europe'),
    'kucoin': ('Japan', 'Asia'),
    'bitstamp': ('Canada', 'North America'),
    'huobi': ('South Korea', 'Asia'),
    'bittrex': ('Australia', 'Oceania')
}
exchanges = list(coin_geo_info.keys())

def safe_request(url, params, retries=3):
    for i in range(retries):
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                return response
        except requests.exceptions.RequestException:
            pass
        print(f"⚠️ Retry {i+1} failed. Retrying after 5 seconds...")
        time.sleep(5)
    return None

def fetch_crypto_data(pages=40):
    all_data = []
    for page in range(1, pages + 1):
        print(f"📦 Fetching page {page} of {pages}...")
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 50,
            "page": page,
            "sparkline": "false",
            "price_change_percentage": "24h,7d"
        }

        response = safe_request(url, params)
        if response is None:
            print(f"❌ Skipped page {page} after 3 failed attempts.")
            continue

        data = response.json()
        for coin in data:
            exchange = random.choice(exchanges)
            country, continent = coin_geo_info[exchange]

            row = {
                'Date': datetime.today().strftime('%Y-%m-%d'),
                'Coin Name': coin.get('name'),
                'Symbol': coin.get('symbol'),
                'Current Price (USD)': coin.get('current_price'),
                'Market Cap (USD)': coin.get('market_cap'),
                '24h Volume (USD)': coin.get('total_volume'),
                '24h Change (%)': coin.get('price_change_percentage_24h_in_currency'),
                '7d Change (%)': coin.get('price_change_percentage_7d_in_currency'),
                'Total Supply': coin.get('total_supply'),
                'Exchange': exchange,
                'Country': country,
                'Continent': continent
            }

            if random.random() < 0.05:
                row['Country'] = None
            if random.random() < 0.03:
                row['7d Change (%)'] = None

            all_data.append(row)

        time.sleep(3)

    return pd.DataFrame(all_data)

if __name__ == "__main__":
    df_crypto = fetch_crypto_data()
    df_crypto.to_csv("crypto_data.csv", index=False)
    print(f"✅ File saved: crypto_data.csv with {len(df_crypto)} records")
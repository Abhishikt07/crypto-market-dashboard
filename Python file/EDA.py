import pandas as pd

# Step 1: Load the file
df = pd.read_csv("crypto_data.csv")

# Step 2: Check and drop duplicates
df.drop_duplicates(inplace=True)

# Step 3: Check and handle missing values
print("🔍 Missing values before cleaning:\n", df.isnull().sum())

# Option A: Drop rows with critical missing values
df = df.dropna(subset=['Current Price (USD)', '24h Volume (USD)', 'Market Cap (USD)'])

# Option B: Fill non-critical missing fields
df['Country'].fillna("Unknown", inplace=True)
df['7d Change (%)'].fillna(df['7d Change (%)'].mean(), inplace=True)

print("\n✅ Missing values after cleaning:\n", df.isnull().sum())

# Step 4: Create 'Price Category'
def categorize_price(price):
    if price < 10:
        return 'Low'
    elif price < 500:
        return 'Mid'
    else:
        return 'High'

df['Price Category'] = df['Current Price (USD)'].apply(categorize_price)

# Step 5: Create 'Volume Tier'
def categorize_volume(vol):
    if vol < 1e6:
        return 'Low'
    elif vol < 1e8:
        return 'Mid'
    else:
        return 'High'

df['Volume Tier'] = df['24h Volume (USD)'].apply(categorize_volume)

# Step 6: Check results
print("\n📊 Price Categories:\n", df['Price Category'].value_counts())
print("\n📊 Volume Tiers:\n", df['Volume Tier'].value_counts())

# Step 7: Save cleaned version
df.to_csv("cleaned_crypto_data.csv", index=False)
print("\n✅ Cleaned data saved as 'cleaned_crypto_data.csv'")

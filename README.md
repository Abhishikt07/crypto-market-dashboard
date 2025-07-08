# 🪙 Crypto Market Analytics Dashboard
An end-to-end data analytics project that extracts real-time data from the **CoinGecko API**, performs **data cleaning and feature engineering in Python**, and builds a visually interactive **Power BI dashboard**.
---
## 🔧 Tools Used
- **Python** – requests, pandas
- **Power BI** – charts, slicers, maps, KPIs
- **CoinGecko API** – real-time crypto market data
- **GitHub** – version control
---
## 📁 Folder Structure
crypto-market-dashboard/
│
├── 📁 Python Scripts/
│   ├── API_integration.py         ← real-time data extraction script
│   └── EDA.py                     ← cleaning + feature engineering
│
├── 📁 Data/
│   ├── crypto_data.csv            ← raw data from API
│   └── cleaned_crypto_data.csv    ← final file for Power BI
│
├── 📁 Power BI/
│   ├── CryptoDashboard.pbix       ← Power BI interactive report
│   └── PowerBIPerformanceData.json← visual usage log
│   └── DATA_ANALYTICS_PROJECT.pdf ← PDF snapshot of dashboard
│
├── README.md                      ← detailed project doc


---
## 🚀 Python Workflow
### `API_integration.py`
- Connects to CoinGecko API (40 pages = ~2000 coins)
- Adds simulated geo fields: `Exchange`, `Country`, `Continent`
- Injects random missing values for realistic EDA
- Saves `crypto_data.csv`
### `EDA.py`
- Removes duplicates & missing critical values
- Fills nulls in `Country`, `7d Change (%)`
- Adds:
  - `Price Category` → Low / Mid / High
  - `Volume Tier` → Low / Mid / High
- Saves final `cleaned_crypto_data.csv`
---
## 📊 Power BI Dashboard
- ✅ Cards: Total Coins, Avg Price, Market Cap, 24h Volume
- ✅ Geo Map: Country-wise volume
- ✅ Donut Chart: Distribution by Continent
- ✅ Bar Charts: Price Category & Volume Tier
- ✅ Matrix: Region vs. Volume Heatmap
- ✅ Slicers: Exchange, Continent, Country, Tier, Date
### 📸 Preview:
![Crypto Market Dashboard](dashboard_preview.png)
> 🧠 Designed with a futuristic theme using #0D1117 (background), cyan and purple accents.
---
## 📄 PDF Snapshot & Performance Report
- `DATA_ANALYTICS_PROJECT.pdf` → Full visual snapshot
- `PowerBIPerformanceData.json` → Visual usage analysis from Power BI export
---
## 🧑‍💼 Author
**Abhishikt Kevin John**  
📫 GitHub: [Abhishikt07](https://github.com/Abhishikt07)  
🎓 Data Analyst | Python | Power BI
---
## 🏁 Final Output
> A portfolio-ready analytics project combining **real-world data**, **custom features**, and **clean visuals** — perfect for GitHub, LinkedIn, and interviews.

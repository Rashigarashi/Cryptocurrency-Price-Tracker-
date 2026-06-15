# Cryptocurrency Price Tracker 🪙

Real-time crypto data scraped from CoinMarketCap using **Selenium + Python**.

---

## 📁 Project Structure

```
crypto_tracker/
├── crypto_scraper.py   ← Main scraper (run this)
├── scheduler.py        ← Auto-repeat every N minutes
├── requirements.txt    ← Python dependencies
└── crypto_data.csv     ← Output (auto-created on first run)
```

---

## 🛠️ VS Code Setup — Step by Step

### Step 1 — Open the Project Folder
```
File → Open Folder → select crypto_tracker/
```

### Step 2 — Create a Virtual Environment
Open the **integrated terminal** (`Ctrl + `` ` ``):
```bash
python -m venv venv
```

### Step 3 — Activate the Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```
**Mac / Linux:**
```bash
source venv/bin/activate
```
You'll see `(venv)` in the terminal prompt.

### Step 4 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5 — Select the Python Interpreter in VS Code
- Press `Ctrl + Shift + P`
- Type **"Python: Select Interpreter"**
- Choose the one inside `./venv`

### Step 6 — Run the Scraper
```bash
python crypto_scraper.py
```

### Step 7 — (Optional) Run the Scheduler
```bash
python scheduler.py         # scrapes every 30 min
python scheduler.py 60      # scrapes every 60 min
```

---

## ⚙️ Configuration (inside crypto_scraper.py)

| Variable | Default | Description |
|---|---|---|
| `TOP_N` | `10` | Number of coins to scrape |
| `HEADLESS` | `True` | Run browser invisibly |
| `CSV_FILE` | `crypto_data.csv` | Output file name |
| `MIN_PRICE` | `None` | Filter: only coins above this price |
| `MIN_CHANGE_24H` | `None` | Filter: only coins with 24h gain above this % |

---

## 📊 Output CSV Columns

| Column | Description |
|---|---|
| rank | CoinMarketCap rank |
| name | Coin name (e.g. Bitcoin) |
| symbol | Ticker (e.g. BTC) |
| price_usd | Current price in USD |
| change_24h | 24-hour % price change |
| change_7d | 7-day % price change |
| market_cap | Market capitalisation in USD |
| timestamp | Date & time of scrape |

---

## 💡 Tips
- Set `HEADLESS = False` to watch the browser open and scrape live.
- CSV **appends** each run — great for building historical data.
- Connect `crypto_data.csv` to Excel / Power BI / Tableau for dashboards.

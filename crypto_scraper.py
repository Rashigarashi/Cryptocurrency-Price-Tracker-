import csv
import os
import time
from datetime import datetime

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# ==========================================
# CONFIGURATION
# ==========================================
URL = "https://coinmarketcap.com/"
TOP_N = 10

CSV_FILE = "crypto_data.csv"


# ==========================================
# CHROME DRIVER
# ==========================================
def build_driver():
    options = Options()

    # Open browser normally
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    return driver


# ==========================================
# SCRAPE DATA
# ==========================================
def scrape_crypto(driver, top_n):

    print("[INFO] Opening CoinMarketCap...")

    driver.get(URL)

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "table tbody tr")
        )
    )

    time.sleep(5)

    rows = driver.find_elements(
        By.CSS_SELECTOR,
        "table tbody tr"
    )

    print(f"[INFO] Found {len(rows)} rows")

    crypto_data = []

    for row in rows:

        try:
            cells = row.find_elements(By.TAG_NAME, "td")

            if len(cells) < 8:
                continue

            # Rank
            try:
                rank = cells[1].text.strip()
            except:
                rank = "N/A"

            # Coin Name
            try:
                name_data = cells[2].text.split("\n")
                coin_name = name_data[0]
            except:
                coin_name = "N/A"

            # Skip CoinMarketCap 20 Index
            if "CoinMarketCap 20" in coin_name:
                continue

            # Price
            try:
                price = cells[3].text.strip()
            except:
                price = "N/A"

            # 24h Change
            try:
                change_24h = cells[4].text.strip()
            except:
                change_24h = "N/A"

            # Market Cap
            try:
                market_cap = cells[7].text.strip()
            except:
                market_cap = "N/A"

            crypto_data.append({
                "Rank": rank,
                "Timestamp": datetime.now().strftime("%d-%m-%Y %H:%M"),
                "Coin Name": coin_name,
                "Price (USD)": price,
                "24h Change": change_24h,
                "Market Cap": market_cap
            })

            if len(crypto_data) >= top_n:
                break

        except Exception as e:
            print("[WARNING]", e)

    return crypto_data


# ==========================================
# DISPLAY TABLE
# ==========================================
def display_table(data):

    if not data:
        print("[WARNING] No data found")
        return

    df = pd.DataFrame(data)

    print("\n" + "=" * 110)
    print("TOP 10 CRYPTOCURRENCIES")
    print("=" * 110)

    print(df.to_string(index=False))

    print("=" * 110)


# ==========================================
# SAVE CSV
# ==========================================
def save_csv(data):

    if not data:
        return

    file_exists = os.path.isfile(CSV_FILE)

    with open(
        CSV_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=data[0].keys()
        )

        if not file_exists:
            writer.writeheader()

        writer.writerows(data)

    print(f"[INFO] Data saved to {CSV_FILE}")


# ==========================================
# MAIN
# ==========================================
def main():

    driver = build_driver()

    try:

        print("[INFO] Chrome opened")

        crypto_data = scrape_crypto(
            driver,
            TOP_N
        )

        display_table(crypto_data)

        save_csv(crypto_data)

        print("\n[INFO] Scraping completed successfully!")

        print("\nGenerated Files:")
        print(f"1. {CSV_FILE}")

        input("\nPress ENTER to close Chrome...")

    except Exception as e:
        print("[ERROR]", e)

    finally:
        driver.quit()
        print("[INFO] Browser closed")


if __name__ == "__main__":
    main()
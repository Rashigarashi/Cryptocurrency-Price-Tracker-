"""
scheduler.py  —  Run crypto_scraper.py at a fixed interval.
Usage:  python scheduler.py          (defaults to every 30 minutes)
        python scheduler.py 60       (every 60 minutes)
"""

import sys
import time
from crypto_scraper import build_driver, scrape_crypto, apply_filters, display_table, save_to_csv, TOP_N, HEADLESS

INTERVAL_MINUTES = int(sys.argv[1]) if len(sys.argv) > 1 else 30


def run_once():
    driver = build_driver(headless=HEADLESS)
    try:
        coins = scrape_crypto(driver, top_n=TOP_N)
        coins = apply_filters(coins)
        display_table(coins)
        save_to_csv(coins)
    finally:
        driver.quit()


if __name__ == "__main__":
    print(f"[SCHEDULER] Starting — interval: {INTERVAL_MINUTES} min. Press Ctrl+C to stop.\n")
    while True:
        run_once()
        print(f"[SCHEDULER] Next run in {INTERVAL_MINUTES} minutes …\n")
        time.sleep(INTERVAL_MINUTES * 60)

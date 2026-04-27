import pandas as pd
from api_client import fetch_data
from utils import setup_logger, log_info
from config import OUTPUT_FILE

def run_pipeline():
    setup_logger()
    log_info("Starting pipeline")

    data = fetch_data()

    if data:
        df = pd.DataFrame(data)
        df.to_json(OUTPUT_FILE, orient="records", indent=2)
        log_info(f"Saved {len(df)} records")
    else:
        log_info("No data fetched")

if __name__ == "__main__":
    run_pipeline()
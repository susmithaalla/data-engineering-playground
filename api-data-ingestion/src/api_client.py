import requests
import time
from config import BASE_URL, PAGE_SIZE, MAX_RETRIES
from utils import log_info, log_error

def fetch_data():
    all_data = []
    page = 1
    retries = 0

    while True:
        try:
            log_info(f"Fetching page {page}")

            response = requests.get(
                BASE_URL,
                params={"_page": page, "_limit": PAGE_SIZE}
            )

            if response.status_code != 200:
                log_error(f"Failed with status {response.status_code}")
                break

            data = response.json()

            if not data:
                log_info("No more data found")
                break

            all_data.extend(data)
            page += 1
            retries = 0

            time.sleep(1)

        except Exception as e:
            log_error(f"Error: {str(e)}")
            retries += 1

            if retries >= MAX_RETRIES:
                log_error("Max retries reached")
                break

            time.sleep(2)

    return all_data
import os
BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OUTPUT_FILE = os.path.join(BASE_DIR, "data", "output.json")
LOG_FILE = os.path.join(BASE_DIR, "logs", "app.log")

PAGE_SIZE = 10
MAX_RETRIES = 3
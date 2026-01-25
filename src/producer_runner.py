import time 
from log_producer_app import main 
from dotenv import load_dotenv
import os 

load_dotenv()

INTERVAL = int(os.getenv("Interval", "60"))
if not INTERVAL:
    raise ValueError(f"Interval is not set.")

while True:
    try:
        main()
    except Exception as e :
        print(f"Producer Error: {e}")
    time.sleep(INTERVAL)

    
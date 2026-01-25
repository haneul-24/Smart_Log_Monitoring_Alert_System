import time 
from alert_engine import main 
from dotenv import load_dotenv
import os 

load_dotenv()

INTERVAL = int(os.getenv("Interval"))
if not INTERVAL:
    raise ValueError(f"Interval is not set.")

while True:
    try:
        main()
    except Exception as e :
        print(f"Alert Error: {e}")
    time.sleep(INTERVAL)
import requests
import random 
import os 
from dotenv import load_dotenv
from logger_config import setup_logging
import logging


setup_logging()


load_dotenv()

url = os.getenv("LOG_SERVER_URL")
if not url :
    raise ValueError("url is not set.")

SERVICE = ["Authentication-service", "Payment-service", "Order-service"]
LEVEL =  ["INFO", "WARNING", "ERROR"]
MESSAGES = {
    "INFO": [
        "Service started successfully",
        "Request processed successfully",
        "Health check passed"
    ],
    "WARNING": [
        "Response time is slow",
        "Memory usage is high",
        "Retrying failed operation"
    ],
    "ERROR": [
        "Database connection failed",
        "Unhandled exception occurred",
        "Service crashed unexpectedly"
    ]
}

def generate_log():
    try :
        level = random.choice(LEVEL)
        log = {
            "service": random.choice(SERVICE),
            "level":level,
            "message": random.choice(MESSAGES[level])
        }

        response = requests.post(url, json=log)
        return response
    
    except Exception as e :
        msg = f"Failed to generate log: {e}"
        print(msg)
        logging.error(msg)
        return None 

def main():
    response = generate_log()
    if response is None:
        return 
    print(response)
    logging.info(f"INFO: {response.status_code}")

if __name__ == "__main__":
    main()
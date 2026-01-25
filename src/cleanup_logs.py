
from python_API import collection
from datetime import datetime, timedelta 
from pymongo.errors import PyMongoError
from utils import upper, upper2, lower, lower2
import logging 
from logger_config import setup_logging
from dotenv import load_dotenv
import os 

setup_logging()

load_dotenv()

days = int(os.getenv('days'))


def log_retention():
    try :
        cutoff_time = datetime.now() - timedelta(days=days)

        delete = collection.delete_many({
            "timestamp": {"$lte":cutoff_time}}
        )

        if delete.deleted_count > 0:
            msg = f"Deleted {delete.deleted_count} old logs"
            upper()
            print(msg)
            lower()
            logging.info(msg)
    
    except PyMongoError as e:
        msg = f"Database Error: {e}"
        upper2()
        print(msg)
        lower2()
        logging.error(msg)

def main():
    log_retention()

if __name__ == "__main__":
    main()

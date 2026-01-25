from datetime import datetime, timedelta, timezone
from python_API import collection
from utils import upper, upper2, lower, lower2
from pymongo.errors import PyMongoError                                         
import logging
from logger_config import setup_logging
import os 
from dotenv import load_dotenv
setup_logging()

load_dotenv()

min = int(os.getenv('min'))

def error_logs_alert() :
    now = datetime.now(timezone.utc)
    one_min_ago = now - timedelta(minutes=min)
    try :
        
        result  = list(collection.aggregate([
            {"$match":{
                "level":"ERROR",
                "timestamp":{
                    "$gte":one_min_ago,
                    "$lte":now
                }
            }},

            {"$group":{
                "_id":"$service",
                "count":{"$sum":1}
            }}
        ]))

        if not result:
            msg ="🟢 No ERROR logs in last 1 minute"
            upper2()
            print(msg)
            lower2()
            logging.info(msg)
            return 

        total_errors = sum(r["count"] for r in result)
        
        if total_errors >=10:
            msg = f"Higher Alert! {total_errors} ERRORS in one minute, system needs maintainence"
            upper2()
            print(msg)
            lower2()
            logging.critical(msg)
            
        elif total_errors >=5 :
            msg = f"🚨Alert!! {total_errors} ERRORS in one minute, system needs maintainence"
            upper2()
            print(msg)
            lower2()
            logging.error(msg)

        else :
            msg = f"System has {total_errors} ERROR in last one minute"
            upper2()
            print(msg)
            lower2()
            logging.warning(msg)
        

        logs = collection.find(
            {
                "level" : "ERROR",
                "timestamp": {
                    "$gte":one_min_ago,
                    "$lte":now
                }
            }
        )
        for log in logs:
            msg = f"Service: {log['service']}\nLevel: {log['level']}\nMessage: {log['message']}\nTimestamp: {log['timestamp']}"
            upper()
            print(msg)
            lower()
            logging.info(msg)
            

    except PyMongoError as e :
        msg = f"Database Error: {e}"
        upper2()
        print(msg)
        lower2()
        logging.error(msg)
        

def per_service_alert():

    now = datetime.now(timezone.utc)
    one_min_ago = now - timedelta(minutes=1)
    try:
        
        result  = list(collection.aggregate([
            {"$match":{
              "level":"ERROR",
                "timestamp":{
                    "$gte":one_min_ago,
                    "$lte":now
                }
            }},

            {"$group":{
                "_id":"$service",
                "count":{"$sum":1},
                "logs":{
                    "$push":{
                        "service":"$service",
                        "level":"$level",
                        "message":"$message",
                        "timestamp":"$timestamp"
                    }
                }
            }
            
            }

        ]))
        
        if not result:
            msg = "🟢 Services has no errors in last one minute."
            upper2()
            print(msg)
            lower2()
            logging.info(msg)
            return
        
        for r in result:
            service = r["_id"] 
            count = r["count"]
            logs = r["logs"] 


            if count >= 10:
                msg = f"🚨 Higher Alert!! {service} has {count} ERRORS in one minute."
                upper2()
                print(msg)
                lower2()
                logging.critical(msg)
                
            elif count >= 5:
                msg = f"🚨 Alert! {service} has {count} ERRORS in one minute."
                upper2()
                print(msg)
                lower2()
                logging.error(msg)
                
            else :
                msg = f"{service} has {count} ERRORS in one minute."
                upper2()
                print(msg)
                lower2()
                logging.warning(msg)

        
            for log in logs :
                msg = f"Service: {log['service']}\nLevel: {log['level']}\nMessage: {log['message']}\nTimestamp: {log['timestamp']}"
                upper()
                print(msg)
                lower()
                logging.error(msg)
                

    except PyMongoError as e :
        msg = f"Database Error: {e}"
        upper2()
        print(msg)
        lower2()
        logging.error(msg)


def main ():  
    error_logs_alert()
    per_service_alert()

if __name__ == "__main__":
    main()

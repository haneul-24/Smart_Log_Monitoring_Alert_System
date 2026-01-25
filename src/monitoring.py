import requests
import os 
from dotenv import load_dotenv
from utils import upper, lower, upper2, lower2
from logger_config import setup_logging
import logging

setup_logging()


load_dotenv()

BASE_URL = os.getenv("BASE_URL")
if not BASE_URL:
    raise ValueError("BASE_URL is not set.")

def fetch_all_logs():
    try :
        response = requests.get(f"{BASE_URL}/logs")
        if response.status_code == 200:
            data = response.json()
            for log in data :
                msg = f"Service: {log['service']}\nLevel: {log['level']}\nMessage: {log['message']}\nTimestamp: {log['timestamp']}"
                upper()
                print(msg)
                lower()
                
        else :
            msg = f"Failed to fetch logs.\nStatus code : {response.status_code}"
            upper2()
            print(msg)
            lower2()
    

    except Exception as e :
        msg = f"Failed to fetch logs: {e}"
        upper2()
        print(msg)
        lower2()
        logging.error(msg)


        
def fetch_error_logs():
    try :
        response = requests.get(f"{BASE_URL}/logs/error")
        if response.status_code == 200:
            data = response.json()
            for log in data :
                msg = f"Service: {log['service']}\nLevel: {log['level']}\nMessage: {log['message']}\nTimestamp: {log['timestamp']}"
                upper()
                print(msg)
                lower()
                

        else :
            msg = f"Failed to fetch error logs.\nStatus code: {response.status_code}"
            upper2()
            print(msg)
            lower2()


    except Exception as e :
        msg = f"Failed to fetch error logs: {e}"
        upper2()
        print(msg)
        lower2()
        logging.error(msg)

def log_summary():
    try :
        response = requests.get(f"{BASE_URL}/logs")
        
        if response.status_code != 200:
            msg = "Unable to fetch logs!!"
            upper2()
            print(msg)
            lower2()
            logging.error(msg)
            return 
        
        
        logs = response.json()
        if not logs :
            msg = "No logs available!!"
            upper2()
            print(msg)
            lower2()
            logging.error(msg)
            return
        

        total_logs = 0 
        info = warning = error = 0
        service_errors = {}

        for log in logs :
            total_logs += 1

            if log["level"] == "INFO":
                info += 1

            elif log["level"] == "WARNING":
                warning += 1 

            elif log["level"] == "ERROR":
                error += 1

                service = log["service"]
                service_errors[service] = service_errors.get(service, 0)+1
 
        upper()
        print(f"Total Logs: {total_logs}")
        print(f"INFO: {info}")
        print(f"WARNING: {warning}")
        print(f"ERROR: {error}")
        lower()
        upper2()
        print("Errors by services: ")
        for service, count in service_errors.items():
            print(f"{service}:{count}")
        lower2()

    except Exception as e :
        msg = f"Exception Error: {e}"
        upper2()
        print(msg)
        lower2()
        logging.error(msg)

        
def log_alert():
    try :
        response = requests.get(f"{BASE_URL}/logs/error")
        if response.status_code != 200:
            msg = "Unable to fetch logs"
            upper2()
            print(msg)
            lower2()
            logging.error(msg)
            return 

        logs = response.json()
        if not logs:
            msg = "No logs available!!"
            upper2()
            print(msg)
            lower2()
            logging.info(msg)
            return 

        service_errors = {}
        for log in logs :

            if log["level"] == "ERROR":
                service = log["service"]
                service_errors[service] = service_errors.get(service, 0)+1 
        print("ALERTS--")
        for service, count in service_errors.items():

            if count>=5:
                msg = f"🔴 Danger: {service} has {count} ERROR"
                upper()
                print(msg)
                lower()
                logging.critical(msg)

            elif count>=3:
                msg = f"🟠 Warning: {service} has {count} ERROR"
                upper()
                print(msg)
                lower()
                logging.error(msg)

            else :
                msg = f"🟡 High Warning: {service} has {count} ERROR"
                upper()
                print(msg) 
                lower()
                logging.warning(msg)
    except Exception as e :
        msg = f"Exception Error: {e}"
        upper2()
        print(msg)
        lower2()
        logging.error(msg)

def filter_logs():
    try :
        upper2()
        service_name = input("Enter service name(Authentication/Payment/Order-service/leave empty for all): ")
        lower2()
        upper2()
        level_name = input("Enter level name(INFO/WARNING/ERROR/leave empty for all): ")
        lower2()

        response = requests.get(f"{BASE_URL}/logs")
        if response.status_code != 200:
            msg = "Unable to fetch logs!!"
            upper2()
            print(msg)
            lower2()
            logging.error(msg)
            return 
        
        logs = response.json()

        if not logs:
            msg = "No logs available!!"
            upper2()
            print(msg)
            lower2()
            logging.info(msg)
            return 
        found = False

        for log in logs:
            if service_name and service_name != log["service"]:
                continue
            if level_name and level_name != log["level"]:
                continue 
            
            found = True 
            msg = f"Service: {log['service']}\nLevel: {log['level']}\nMessage: {log['message']}\nTimestamp: {log['timestamp']}"
            upper()
            print(msg)
            lower()
            

        if not found :
            msg = "No logs matched your filter!!"
            upper2()
            print(msg)
            lower2()
            logging.info(msg)

    except Exception as e :
        msg = f"Exception Error: {e}"
        upper2()
        print(msg)
        lower2()
        logging.error(msg)


import logging 
from utils import upper, upper2, lower, lower2
from monitoring import fetch_all_logs, fetch_error_logs, filter_logs, log_summary, log_alert
 


def main():
    upper()
    print("Welcome to the monitoring system...🤗")
    lower()
    while True:
        upper2()
        print("1. All Logs")
        print("2. Error Logs")
        print("3. Logs Summary")
        print("4. Logs Alerts")
        print("5. Filter Logs ")
        print("6. Exit Monitorinng System")
        lower2()
        upper2()
        choice = input("Enter your choice: ")
        lower2() 

        match choice :
            case "1":
                fetch_all_logs()
            case "2":
                fetch_error_logs()
            case "3":
                log_summary()
            case "4":
                log_alert()
            case "5":
                filter_logs()
            case "6":
                msg = "Exiting Monitoring system.."
                upper()
                print(msg)
                lower()
                logging.info(msg)
                break
            case __:
                msg = "Invalid choice!!"
                upper2()
                print(msg)
                lower2()
                logging.warning(msg)
                
                

if __name__ == "__main__":
    main()


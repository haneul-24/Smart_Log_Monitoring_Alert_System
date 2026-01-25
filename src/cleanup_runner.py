
from cleanup_logs import main 

while True:
    try:
        main()
    except Exception as e :
        print(f"Cleanup Error: {e}")
    
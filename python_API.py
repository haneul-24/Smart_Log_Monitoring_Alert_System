from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from pymongo import MongoClient
import os 
from dotenv import load_dotenv
from datetime import datetime, timezone
from pymongo.errors import PyMongoError
from bson import ObjectId
import certifi
import logging
from logger_config import setup_logging


setup_logging()


load_dotenv()
try :
    url = os.getenv("URL")
    client = MongoClient(url, tls=True,tlsCAFile=certifi.where(),serverSelectionTimeoutMS=30000,connect=True)
    client.server_info()
except Exception as e :
    print(f"MonogDB not ready: {e}")

db = client["smart_logs"]
collection = db["logs"]

app = FastAPI()

class Logs(BaseModel):
    service : str
    level : str
    message : str
    timestamp : datetime=Field(default_factory=lambda: datetime.now(timezone.utc))

@app.get("/")
def read_root():
    msg = {"message":"Welcome to the logs API..🤗"}
    logging.info(f'root endpoint hit: {msg}')

    return msg 


@app.post("/logs")
def create_logs(log:Logs):
    existing_log = collection.find_one({
        "service":log.service,
        "level":log.level,
        "message":log.message
    })
    if existing_log :
        raise HTTPException(
            status_code=409,
            detail="Conflict Error!!"
        )
        
    try:
        result = collection.insert_one(log.dict())
        return {
            "id": str(result.inserted_id),
            **log.dict() 
        }
        
    except PyMongoError as e :
        logging.error(f'{e}')
        raise HTTPException(
            status_code=500,
            detail=f"{e}"
        )


@app.get("/logs")
def view_all_logs():
    try :
        logs_list = []
        result = list(collection.find())
        if not result:
            raise HTTPException(
                status_code=404,
                detail="Logs not found!"
            )
            
        for doc in result:
            logs_list.append({
                "id" : str(doc["_id"]),
                "service":doc["service"],
                "level":doc["level"],
                "message":doc["message"],
                "timestamp":doc["timestamp"]
            })
        
        return logs_list
    
    except PyMongoError as e :
        logging.error(f'{e}')
        raise HTTPException(
            status_code=500,
            detail=f"{e}"                                              
        )
    

@app.get("/logs/error")
def view_level_logs():
    try :
        result = list(collection.find({"level": "ERROR" }))
        if not result:
            raise HTTPException(
                status_code=404,
                detail="Logs not found!"
            )
        
        else:
            final_list = []
            for doc in result:
                final_list.append({
                    "id":str(doc["_id"]),
                    "service":doc["service"],
                    "level":doc["level"],
                    "message":doc["message"],
                    "timestamp":doc["timestamp"]
                })
    
            return final_list
        
    except PyMongoError as e :
        logging.error(f'{e}')

        raise HTTPException(
            status_code=500,
            detail=f"{e}"
        )
    
        
@app.delete("/logs/{log_id}")
def delete_logs(log_id:str):
    try :
        deleted = collection.delete_one({"_id":ObjectId(log_id)})
        if deleted.deleted_count == 0:
            raise HTTPException(
                status_code=404,
                detail="ID not found!!"
            )
        else:
            msg = {"message":"Deleted successfully.."}
            logging.info("Deleted successfully.")
            return msg 
        
    except PyMongoError as e :
        logging.error(f"{e}")
        raise HTTPException(
            status_code=500,
            detail=f"{e}"
        )
    


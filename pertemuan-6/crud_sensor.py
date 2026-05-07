from dotenv import load_dotenv
from pymongo import MongoClient
from datetime import datetime, timedelta
import random, os
import logging

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]
collection = db["sensor"]

from dotenv import load_dotenv
from pymongo import MongoClient
from datetime import datetime, timedelta
import random, os
import logging

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]
collection = db["sensor"]

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("crud_sensor.log"),
        logging.StreamHandler()
    ]
)


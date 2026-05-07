import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"), serverSelectionTimeoutMS=5000)
db = client["latihan6"]

try:
    client.admin.command('ping')
    print("Koneksi MongoDB berhasil!")
except Exception as e:
    print("Gagal terhubung:", e)



import pandas as pd
from pymongo import MongoClient
from koneksi import db

#find
#cursor = db.maintenance.find({"biaya":{"$gt" : 1000000}},{"_id":0})

#update
#cursor = db.maintenance.update_one({"mesin":"CNC-01","biaya":1200000},{"$set":{"teknisi":"Dewi"}})

#jadiin data frame dan print
#df = pd.DataFrame(list(cursor))
#print(df)

#agregations

cursor = db["maintenance"].aggregate([
    {
        "$group": {
            "_id": {
                "bulan": {"$month": "$tanggal"},
                "tahun": {"$year": "$tanggal"}
            },
            "total_biaya": {"$sum": "$biaya"}
        }
    },
    {
        "$project": {
            "_id": 0,
            "bulan": "$_id.bulan",
            "tahun": "$_id.tahun",
            "total_biaya": 1
        }
    },
    {
        "$sort": {"tahun": 1, "bulan": 1}
    }
])


df = pd.DataFrame(list(cursor))
print(df)
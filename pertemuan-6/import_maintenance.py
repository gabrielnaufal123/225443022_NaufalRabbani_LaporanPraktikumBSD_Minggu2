import pandas as pd
from pymongo import MongoClient
from koneksi import db 

collection = db["maintenance"]

#membaca file csv
df = pd.read_csv("maintenance.csv")

#mengubah tanggal menjadi format datetime
df['tanggal'] = pd.to_datetime(df['tanggal'])
print(df.head())

#ubah data frame menjadi list dictionary
data_dict = df.to_dict(orient='records')

print(data_dict)

# insert banyak data sekaligus
collection.insert_many(data_dict)

print("Data berhasil dimasukkan!")
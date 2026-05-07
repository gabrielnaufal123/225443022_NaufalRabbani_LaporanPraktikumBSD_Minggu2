import pandas as pd
import matplotlib.pyplot as plt
from crud_sensor import collection


cursor = collection.find({}, {"_id": 0})
df = pd.DataFrame(list(cursor))

print(df.dtypes)

# ✅ ubah ke datetime dulu
df['timestamp'] = pd.to_datetime(df['timestamp'])

# ✅ jadikan index
df = df.set_index('timestamp')

# ❌ hapus ini (redundant)
# df.set_index('timestamp', inplace=True)

# ✅ baru ambil numerik
df_numeric = df.select_dtypes(include='number')

print(df.describe())

# ✅ sekarang aman
resampled = df_numeric.resample('10min').mean()
print(resampled.head())

# 📊 plot
plt.figure(figsize=(10,5))
df['suhu'].plot(title='Suhu dari Waktu ke Waktu')
plt.ylabel('Suhu (°C)')
plt.grid(True)
plt.savefig('suhu_plot.png')
plt.show()



# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 12:10:19 2024

@author: Muysaaa
"""

#IMPORT DATA 
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Mendefinisikan tanggal awal dan akhir
start_date = '2021-09-25'
end_date = '2024-09-25'

# Mendownload data harga saham
data = yf.download("AAPL", start=start_date, end=end_date)

# Menyiapkan data
data['Days'] = (data.index - data.index[0]).days
X = data[['Days']]
y = data['Close']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membuat model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediksi untuk 1 tahun ke depan
future_days = np.array([[data['Days'].max() + i] for i in range(1, 366)])
y_pred = model.predict(future_days)

# Visualisasi
plt.figure(figsize=(10, 5))
plt.plot(data.index, data['Close'], label='Data Historis')
future_dates = pd.date_range(start=data.index[-1] + pd.Timedelta(days=1), periods=365)
plt.plot(future_dates, y_pred, label='Prediksi 1 Tahun', color='orange')
plt.xlabel('Tanggal')
plt.ylabel('Harga Saham')
plt.title('Prediksi Harga Saham AAPL 1 Tahun Kedepan')
plt.legend()
plt.show()

import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

class StockTrendPredictor:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.data = self.download_data()
        self.model = LinearRegression()
        
        
    def download_data(self):
        # Download historical data for the specified ticker and date range
        data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
        return data['Close']

    def prepare_data(self):
        # Prepare the data for linear regression
        self.data = self.data.reset_index()
        self.data['Date'] = pd.to_datetime(self.data['Date'])
        self.data['Days'] = (self.data['Date'] - self.data['Date'].min()).dt.days
        
        X = self.data['Days'].values.reshape(-1, 1)
        y = self.data['Close'].values
        return X, y

    def fit_model(self):
        X, y = self.prepare_data()
        self.model.fit(X, y)

    def predict_future(self, days_to_predict=365):
        last_day = self.data['Days'].max()
        future_days = np.array(range(last_day + 1, last_day + days_to_predict + 1)).reshape(-1, 1)
        predictions = self.model.predict(future_days)
        return future_days, predictions

    def plot_results(self):
        self.fit_model()
        future_days, future_predictions = self.predict_future()

        plt.figure(figsize=(12, 6))

        # Plot actual data
        plt.plot(self.data['Date'], self.data['Close'], label='Harga Saham Aktual', color='blue')

        # Interpolasi (fit line)
        plt.plot(self.data['Date'], self.model.predict(self.data['Days'].values.reshape(-1, 1)), label='Interpolasi', color='orange')

        # Plot prediksi masa depan
        future_dates = [self.data['Date'].max() + timedelta(days=int(day)) for day in future_days.flatten()]
        plt.plot(future_dates, future_predictions, label='Prediksi 1 Tahun ke Depan', color='red')

        # Formatting the plot
        plt.title(f'Trend Harga Saham {self.ticker}')
        plt.xlabel('Tanggal')
        plt.ylabel('Harga Saham')
        plt.legend()
        plt.grid()
        plt.show()



import yfinance as yf
import pandas as pd
import pandas_ta as ta
import os

# Ham petrol fiyatlarını çekin
oil = yf.Ticker("CL=F")
data = oil.history(period="max", interval="1d")  # Son 10 yılın günlük verisi

# MACD hesaplama
macd_df = ta.macd(data['Close'])
data['MACD'] = macd_df['MACD_12_26_9']
data['MACD_Signal'] = macd_df['MACDs_12_26_9']
data['MACD_Hist'] = macd_df['MACDh_12_26_9']

# RSI hesaplama
data['RSI'] = ta.rsi(data['Close'], length=14)

# Bollinger Bandları hesaplama
bbands_df = ta.bbands(data['Close'], length=20)
data['Upper_Band'] = bbands_df['BBU_20_2.0']
data['Middle_Band'] = bbands_df['BBM_20_2.0']
data['Lower_Band'] = bbands_df['BBL_20_2.0']

# EMA hesaplama
data['EMA_25'] = ta.ema(data['Close'], length=25)
data['EMA_50'] = ta.ema(data['Close'], length=50)
data['EMA_100'] = ta.ema(data['Close'], length=100)
data['EMA_200'] = ta.ema(data['Close'], length=200)

# NaN değerlerini kontrol et
print(data.isna().sum())

# İlk 200 satırı sil
data = data.iloc[200:]

# 'Dividends' ve 'Stock Splits' sütunlarını kaldır
data = data.drop(columns=['Dividends', 'Stock Splits'], errors='ignore')

# Verileri CSV dosyası olarak kaydet
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')  # Masaüstü yolu
csv_file_path = os.path.join(desktop_path, 'crude_oil_data_with_indicators.csv')  # CSV dosya yolu
data.to_csv(csv_file_path, index=False, encoding='utf-8')

print(f"Veri başarıyla CSV dosyasına kaydedildi: {csv_file_path}")


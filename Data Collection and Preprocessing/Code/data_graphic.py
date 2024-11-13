import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Seaborn ile grafiklerin görünümünü iyileştirelim
sns.set(style="whitegrid")

# CSV dosyasının yolunu Kod klasöründen alıyoruz
csv_file_path = "Data\\crude_oil_data_with_indicators.csv"

# Veriyi okuyoruz, sınırlayıcı olarak virgül kullanıyoruz
df = pd.read_csv(csv_file_path, delimiter=",", encoding="utf-8")

# Tarih sütununu datetime formatına çeviriyoruz
df['Date'] = pd.to_datetime(df['Date'], utc=True)

# Numeric columns conversion
numeric_columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'MACD', 'MACD_Signal', 'MACD_Hist', 'RSI', 'Upper_Band', 'Middle_Band', 'Lower_Band', 'EMA_25', 'EMA_50', 'EMA_100', 'EMA_200']
for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors='coerce')

# Verileri numpy array'ine dönüştürüyoruz
date_values = np.array(df['Date'])
open_values = np.array(df['Open'])
high_values = np.array(df['High'])
low_values = np.array(df['Low'])
close_values = np.array(df['Close'])
volume_values = np.array(df['Volume'])
macd_values = np.array(df['MACD'])
macd_signal_values = np.array(df['MACD_Signal'])
macd_hist_values = np.array(df['MACD_Hist'])
rsi_values = np.array(df['RSI'])
upper_band_values = np.array(df['Upper_Band'])
middle_band_values = np.array(df['Middle_Band'])
lower_band_values = np.array(df['Lower_Band'])
ema_25_values = np.array(df['EMA_25'])
ema_50_values = np.array(df['EMA_50'])
ema_100_values = np.array(df['EMA_100'])
ema_200_values = np.array(df['EMA_200'])

# Altın Endeksi Verilerini Okuma
gold_index_path = "Data\\gold_index_prices.csv"
gold_df = pd.read_csv(gold_index_path, delimiter=",", encoding="utf-8")

# Tarih sütununu datetime formatına çeviriyoruz
gold_df['Tarih'] = pd.to_datetime(gold_df['Tarih'], utc=True)

# Numeric columns conversion for Gold Index
gold_numeric_columns = ['Açılış Fiyatı', 'En Yüksek Fiyat', 'En Düşük Fiyat', 'Kapanış Fiyatı']
for column in gold_numeric_columns:
    gold_df[column] = pd.to_numeric(gold_df[column], errors='coerce')

gold_date_values = np.array(gold_df['Tarih'])
gold_open_values = np.array(gold_df['Açılış Fiyatı'])
gold_high_values = np.array(gold_df['En Yüksek Fiyat'])
gold_low_values = np.array(gold_df['En Düşük Fiyat'])
gold_close_values = np.array(gold_df['Kapanış Fiyatı'])

# USD Endeksi Verilerini Okuma
usd_index_path = "Data\\usd_index_prices.csv"
usd_df = pd.read_csv(usd_index_path, delimiter=",", encoding="utf-8")

# Tarih sütununu datetime formatına çeviriyoruz
usd_df['Tarih'] = pd.to_datetime(usd_df['Tarih'], utc=True)

# Numeric columns conversion for USD Index
usd_numeric_columns = ['Açılış Fiyatı', 'En Yüksek Fiyat', 'En Düşük Fiyat', 'Kapanış Fiyatı']
for column in usd_numeric_columns:
    usd_df[column] = pd.to_numeric(usd_df[column], errors='coerce')

usd_date_values = np.array(usd_df['Tarih'])
usd_open_values = np.array(usd_df['Açılış Fiyatı'])
usd_high_values = np.array(usd_df['En Yüksek Fiyat'])
usd_low_values = np.array(usd_df['En Düşük Fiyat'])
usd_close_values = np.array(usd_df['Kapanış Fiyatı'])

# 1. Sayfa: İlk dört grafik
fig1, axs1 = plt.subplots(2, 2, figsize=(12, 10))

# 1. Açılış, En Yüksek, En Düşük ve Kapanış Fiyatları Grafiği
axs1[0, 0].plot(date_values, open_values, label="Açılış", color="blue")
axs1[0, 0].plot(date_values, high_values, label="En Yüksek", color="green")
axs1[0, 0].plot(date_values, low_values, label="En Düşük", color="red")
axs1[0, 0].plot(date_values, close_values, label="Kapanış", color="purple")
axs1[0, 0].set_xlabel("Tarih")
axs1[0, 0].set_ylabel("Fiyat")
axs1[0, 0].set_title("Ham Petrol/USD")
axs1[0, 0].legend()

# 2. Hacim (Volume) Grafiği
axs1[0, 1].bar(date_values, volume_values, color="darkblue", edgecolor="blue", label="Hacim", alpha=0.7)
axs1[0, 1].set_xlabel("Tarih")
axs1[0, 1].set_ylabel("Hacim")
axs1[0, 1].set_title("Ham Petrol Hacim (Volume)")
axs1[0, 1].legend()

# 3. MACD, MACD_Signal, MACD_Hist Grafiği
axs1[1, 0].plot(date_values, macd_values, label="MACD", color="blue")
axs1[1, 0].plot(date_values, macd_signal_values, label="MACD Sinyal", color="green")
axs1[1, 0].bar(date_values, macd_hist_values, label="MACD Histogram", color="darkred", edgecolor="tomato", alpha=0.5)
axs1[1, 0].set_xlabel("Tarih")
axs1[1, 0].set_ylabel("MACD Değerleri")
axs1[1, 0].set_title("MACD Göstergesi")
axs1[1, 0].legend()

# 4. RSI Grafiği
axs1[1, 1].plot(date_values, rsi_values, label="RSI", color="purple")
axs1[1, 1].axhline(70, color="red", linestyle="--")  # Aşırı alım çizgisi
axs1[1, 1].axhline(30, color="blue", linestyle="--")  # Aşırı satım çizgisi
axs1[1, 1].set_xlabel("Tarih")
axs1[1, 1].set_ylabel("RSI")
axs1[1, 1].set_title("Göreceli Güç Endeksi (RSI)")
axs1[1, 1].legend()

# 1. sayfa grafiklerini gösteriyoruz
plt.tight_layout()
plt.subplots_adjust(hspace=0.3, wspace=0.2)
plt.show()

# 2. Sayfa: Kalan dört grafik
fig2, axs2 = plt.subplots(2, 2, figsize=(12, 10))

# 5. Bollinger Bantları Grafiği
axs2[0, 0].plot(date_values, upper_band_values, label="Üst Bant", color="green")
axs2[0, 0].plot(date_values, middle_band_values, label="Orta Bant", color="blue")
axs2[0, 0].plot(date_values, lower_band_values, label="Alt Bant", color="red")
axs2[0, 0].fill_between(date_values, lower_band_values, upper_band_values, color="gray", alpha=0.2)
axs2[0, 0].set_xlabel("Tarih")
axs2[0, 0].set_ylabel("Fiyat")
axs2[0, 0].set_title("Bollinger Bantları")
axs2[0, 0].legend()

# 6. EMA Grafiği (EMA_25, EMA_50, EMA_100, EMA_200)
axs2[0, 1].plot(date_values, ema_25_values, label="EMA 25", color="orange")
axs2[0, 1].plot(date_values, ema_50_values, label="EMA 50", color="purple")
axs2[0, 1].plot(date_values, ema_100_values, label="EMA 100", color="blue")
axs2[0, 1].plot(date_values, ema_200_values, label="EMA 200", color="green")
axs2[0, 1].set_xlabel("Tarih")
axs2[0, 1].set_ylabel("EMA Değerleri")
axs2[0, 1].set_title("Üstel Hareketli Ortalamalar (EMA)")
axs2[0, 1].legend()

# 7. Altın Endeksi Grafiği
axs2[1, 0].plot(gold_date_values, gold_open_values, label="Altın Açılış", color="blue")
axs2[1, 0].plot(gold_date_values, gold_high_values, label="Altın En Yüksek", color="green")
axs2[1, 0].plot(gold_date_values, gold_low_values, label="Altın En Düşük", color="red")
axs2[1, 0].plot(gold_date_values, gold_close_values, label="Altın Kapanış", color="purple")
axs2[1, 0].set_xlabel("Tarih")
axs2[1, 0].set_ylabel("Fiyat")
axs2[1, 0].set_title("Altın İndex")
axs2[1, 0].legend()

# 8. USD Endeksi Grafiği
axs2[1, 1].plot(usd_date_values, usd_open_values, label="USD Açılış", color="blue")
axs2[1, 1].plot(usd_date_values, usd_high_values, label="USD En Yüksek", color="green")
axs2[1, 1].plot(usd_date_values, usd_low_values, label="USD En Düşük", color="red")
axs2[1, 1].plot(usd_date_values, usd_close_values, label="USD Kapanış", color="purple")
axs2[1, 1].set_xlabel("Tarih")
axs2[1, 1].set_ylabel("Fiyat")
axs2[1, 1].set_title("USD İndex")
axs2[1, 1].legend()

# İkinci sayfa grafiklerini gösteriyoruz
plt.tight_layout()
plt.subplots_adjust(hspace=0.3, wspace=0.2)
plt.show()

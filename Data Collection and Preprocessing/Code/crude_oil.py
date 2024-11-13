from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import os
import time

driver = webdriver.Chrome()
url = "https://finance.yahoo.com/quote/CL%3DF/history/?period1=971568000&period2=1729641600&filter=history"
driver.get(url)

time.sleep(5)
driver.maximize_window()
time.sleep(5)

data_list = []

for tr in range(1,5001):
    try:
        deneme = driver.find_element(By.XPATH, f"/html/body/div[2]/main/section/section/section/article/div[1]/div[3]/table/tbody/tr[{tr}]")
        row_text = deneme.text.strip("()")

        data_parts = row_text.split()

        # Veriyi ayrıştır ve uygun değişkenlere ata
        date = " ".join(data_parts[:3])  # Tarih (Oct 22, 2024)
        open_price = float(data_parts[3])  # Açılış Fiyatı
        high_price = float(data_parts[4])  # En Yüksek Fiyat
        low_price = float(data_parts[5])  # En Düşük Fiyat
        close_price = float(data_parts[6])  # Kapanış Fiyatı
        adjusted_close_price = float(data_parts[7])  # Düzeltme Kapanış Fiyatı
        try:
            volume = int(data_parts[8].replace(",", ""))
        except ValueError:
            volume = 0  # Eğer değer dönüştürülemezse 0 olarak ayarla
        
        
        data_list.append([date, open_price, high_price, low_price, close_price, adjusted_close_price, volume])

    except Exception as e:
        print(f"Veri çekme hatası tr[{tr}]: {e}")
        continue

time.sleep(2)

# DataFrame oluşturma
df = pd.DataFrame(data_list, columns=['Tarih', 'Açılış Fiyatı', 'En Yüksek Fiyat', 'En Düşük Fiyat', 'Kapanış Fiyatı', 'Düzeltme Kapanış Fiyatı', 'İşlem Hacmi'])

# CSV dosyasını masaüstüne kaydetme
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')  # Masaüstü yolu
csv_file_path = os.path.join(desktop_path, 'crude_oil_data.csv')  # CSV dosya yolu

df.to_csv(csv_file_path, index=False, encoding='utf-8')

# İşlem tamamlandı mesajı
print(f"Veri başarıyla CSV dosyasına kaydedildi: {csv_file_path}")


time.sleep(3)
driver.close()
# Ham Petrol Fiyat Tahmini - Zaman Serisi Projesi

Bu proje, ham petrol fiyatlarını tahmin etmek amacıyla zaman serisi analizine dayalı bir makine öğrenimi modelini geliştirmeyi amaçlamaktadır. İki aşamadan oluşan bu projede ilk olarak veri toplama, veri ön işleme ve veri görselleştirme adımları tamamlanmıştır. İkinci aşamada ise makine öğrenimi algoritmaları ile modelleme yapılacaktır.

## Proje Hakkında
Ham petrol fiyatları üzerine zaman serisi tahmin modelinin geliştirilmesi amaçlanan bu projede, ilk aşama veri toplama, ön işleme ve görselleştirmeden oluşmaktadır. Proje verilerini Yahoo Finance'ten Python Selenium ve Pandas kullanarak çektik ve bu verileri uygun formatta CSV dosyalarına kaydettik. Daha sonra finansal analizde sıklıkla kullanılan indikatörler hesaplanarak veri kümesine eklendi. Son olarak, verileri görselleştirerek anlamlı analizler yapılabilmesi için gerekli grafikler oluşturuldu.

## Kullanılan Teknolojiler
- **Python 3.9.0**
- **Selenium** - Web scraping işlemleri için
- **Pandas** - Veri işleme ve düzenleme
- **Pandas_ta** - İndikatör hesaplamaları için
- **Matplotlib & Seaborn** - Veri görselleştirme
- **Numpy** - Matematiksel işlemler ve hesaplamalar

## Proje Yapısı
Bu aşamada projeyi oluşturan ana adımlar:

1. **Konu Seçimi**: Ham petrol fiyat tahmini
2. **Veri Toplama**: Yahoo Finance üzerinden web scraping (Python Selenium ve Pandas ile)
3. **İndikatör Hesaplama**: MACD, RSI, Bollinger Bantları ve EMA gibi indikatörler
4. **Veri Ön İşleme**: Gereksiz ve uygun olmayan verilerin temizlenmesi
5. **Görselleştirme**: Veri dağılımlarının ve ilişkilerinin grafiklerle sunulması

## Veri Kaynakları ve Toplama
Ham petrol fiyatları, altın endeksi ve dolar endeksi verileri Yahoo Finance platformundan çekildi. Her veri kümesi **Tarih, Açılış Fiyatı, En Yüksek Fiyat, En Düşük Fiyat, Kapanış Fiyatı, Düzeltme Kapanış Fiyatı ve Hacim** bilgilerini içerir. Yaklaşık 5000 kayıt CSV formatında saklanmıştır.

## İndikatör Hesaplamaları
Verilerin daha anlamlı hale getirilmesi için aşağıdaki teknik indikatörler hesaplanmıştır:

- **MACD (Moving Average Convergence Divergence)**: `MACD`, `MACD_Signal`, `MACD_Histogram`
- **RSI (Relative Strength Index)**: `RSI`
- **Bollinger Bantları**: `Upper Band`, `Middle Band`, `Lower Band`
- **EMA (Exponential Moving Average)**: `EMA_25`, `EMA_50`, `EMA_100`, `EMA_200`

## Veri Ön İşleme
Toplanan ham veriler üzerinde çeşitli ön işleme adımları gerçekleştirildi:

- **Temizlik**: Eksik veya hatalı veriler temizlendi.
- **Gereksiz Alanların Kaldırılması**: Kullanılmayacak sütunlar veri setinden çıkarıldı.

Bu işlemler, modellemenin daha sağlıklı bir şekilde yapılması için uygun veriyi elde etmek adına önemlidir.

## Görselleştirme
Veri setine ait önemli trendleri ve dağılımları göstermek amacıyla çeşitli grafikler oluşturulmuştur:

1. **Ham Petrol/USD**: Açılış, En Yüksek, En Düşük, Kapanış
2. **Ham Petrol Hacim (Volume)**: Hacim
3. **MACD Göstergesi**: MACD, MACD Sinyal, MACD Histogram
4. **Göreceli Güç Endeksi (RSI)**: RSI
5. **Bollinger Bantları**: Üst Bant, Orta Bant, Alt Bant
6. **Üstel Hareketli Ortalamalar (EMA)**: EMA 25, EMA 50, EMA 100, EMA 200
7. **Altın İndex**: Açılış, En Yüksek, En Düşük, Kapanış
8. **USD İndex**: Açılış, En Yüksek, En Düşük, Kapanış

![Grafik 1](https://raw.githubusercontent.com/YusufPerktas/Time-Series-Machine-Learning/refs/heads/main/Data%20Collection%20and%20Preprocessing/Data/Grafik%201.png)
![Grafik 1](https://raw.githubusercontent.com/YusufPerktas/Time-Series-Machine-Learning/refs/heads/main/Data%20Collection%20and%20Preprocessing/Data/Grafik%202.png)

Grafikler, `Matplotlib` ve `Seaborn` kütüphaneleri kullanılarak görselleştirildi.

---

Bu dosya, projenin ilk aşaması hakkında genel bir rehber sunmaktadır. Projenin ikinci aşamasında makine öğrenimi modelleme işlemleri eklenecektir.

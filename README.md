# 💻 Bilgisayar Fiyat Tahmin Sistemi (PC Price Prediction)

Bu projede, bilgisayar donanım özellikleri kullanılarak **bilgisayar fiyatı tahmini yapan bir makine öğrenmesi modeli** geliştirilmiştir.  
Eğitilen model, **Flask tabanlı bir web arayüzü** ile kullanıcıya sunulmuştur.

---

## 📌 Proje Hakkında

Proje kapsamında, farklı bilgisayar donanım özelliklerini içeren bir veri seti üzerinde çalışılmıştır.  
Amaç, kullanıcıdan alınan donanım bilgilerine göre **tahmini piyasa fiyatını** hesaplayabilen bir sistem oluşturmaktır.

Model eğitimi tamamlandıktan sonra, model bir web uygulamasına entegre edilerek **gerçek zamanlı tahmin** yapılması sağlanmıştır.

---

## ⚙️ Kullanılan Teknolojiler

- **Python:** Projenin ana dili
- **Scikit-Learn:** Linear Regression modeli ve veri ön işleme
- **Pandas & NumPy:** Veri analizi ve düzenleme
- **Statsmodels:** Backward Elimination ile istatistiksel analiz
- **Flask:** Web uygulaması geliştirme
- **Bootstrap 5:** Arayüz tasarımı

---

## 🧪 Model ve Veri Süreci

Ham veriler doğrudan modele verilmemiştir. Model performansını artırmak için aşağıdaki adımlar uygulanmıştır:

### Veri Temizleme
- Eksik veriler (NaN) ortalama değerler ile doldurulmuştur.

### Özellik Mühendisliği
- İşlemci ve ekran kartı gibi kategorik bilgiler **sayısal değerlere** dönüştürülmüştür.
- Örneğin:
  - `RTX 4090` → 5
  - `GTX 1650` → 1

Bu sayede modelin donanım gücünü sayısal olarak öğrenmesi sağlanmıştır.

### İstatistiksel Analiz
- **Backward Elimination** yöntemi kullanılarak fiyat üzerinde etkisi olmayan değişkenler modelden çıkarılmıştır.
- Örneğin:
  - Kasa RGB durumu
  - Garanti süresi

Bu işlem, modelin daha sade ve anlamlı öğrenmesini sağlamıştır.

---

## 🌐 Web Arayüzü

- Flask kullanılarak basit ve anlaşılır bir web arayüzü geliştirilmiştir.
- Kullanıcı:
  - Donanım özelliklerini form üzerinden seçer
  - Modelden tahmini fiyat bilgisini alır
- Arayüz tasarımında Bootstrap 5 kullanılmıştır.

---

## 📂 Proje Yapısı

```text
├── app.py              # Flask uygulamasının ana dosyası
├── model.pkl           # Eğitilmiş makine öğrenmesi modeli
├── static/
│   └── background.png  # Arka plan görseli
├── templates/
│   └── index.html      # Kullanıcı arayüzü
└── README.md           # Proje dokümantasyonu
```

---

**Ad:** Yusuf 
**Soyad:** TUNÇ 
**Okul No:** 2012721024"

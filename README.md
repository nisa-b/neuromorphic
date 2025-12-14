# Spike Tabanlı Ses Tanıma (Evet / Hayır)

Bu projede **ham ses sinyallerinden spike (diken) dizileri** üretilerek **Leaky Integrate-and-Fire (LIF)** nöron modeli ile basit bir nöral hesaplama yapılmaktadır.

---

## Adım 1: Ham Ses Sinyali

* Her biri **1 saniyelik** olacak şekilde **15 adet "evet"** ve **15 adet "hayır"** ses kaydı alınmıştır.
* Örnekleme frekansı **16 kHz** olup, her kayıt **16.000 veri noktası** içerir.
* Amaç:

  * Hesaplama yükünü azaltmak
  * Sesin temel zaman yapısını koruyarak aşırı detayları filtrelemek

---

## Adım 2: Veri Hazırlama ve Özellik Çıkarımı

Bu adımlar `spike_encoding.py` dosyasında gerçekleştirilir.

### 1. Downsampling

* `downsample` fonksiyonu ile sinyal **50 veri noktasına** indirgenir.
* Böylece zamansal yapı korunurken veri boyutu ciddi şekilde azaltılır.

### 2. Wavelet Analizi

* İndirgenmiş sinyal, `pywt.dwt` kullanılarak **ayrık dalgacık dönüşümüne (DWT)** tabi tutulur.
* Çıktı:

  * `cA`: Approximation coefficients (genel yapı)
  * `cD`: Detail coefficients (yüksek frekanslı ani değişimler)

Bu projede **ani değişimler** önemli olduğu için **yalnızca detay katsayıları (`cD`)** kullanılır.

### 3. Spike (Diken) Kodlama

* `cD` katsayılarının **mutlak değeri** alınır.
* Her değer, belirlenen bir eşik değeri ile karşılaştırılır:

  * Eşik: `0.005`
  * Büyükse → `1` (spike)
  * Küçükse → `0`

**Çıktı:**

* Uzunluğu **25** olan, ikili bir spike dizisi:

```
[0, 0, 0, 1, 1, 0, 1, 0, ...]
```

Bu dizi, nöron modeline verilen girdiyi temsil eder.

---

## Adım 3: Nöral Hesaplama

Elde edilen spike dizisi, yapay bir sinir hücresine (nörona) beslenir.

### Leaky Integrate-and-Fire (LIF) Modeli

LIF modeli, biyolojik nöronun temel davranışlarını taklit eder:

* Entegrasyon (biriktirme)
* Sızıntı (leak)
* Ateşleme (spike üretimi)

### Zar Potansiyeli Güncelleme

Her zaman adımında zar potansiyeli (`V`) aşağıdaki adımlardan geçer:

#### 1. Entegrasyon (Girdi)

Gelen spike (`s`) varsa potansiyel artırılır:

```
V_new = V_old + (weight * s)
```

#### 2. Sızıntı (Leak)

Potansiyel, dinlenme seviyesine dönme eğilimi gösterecek şekilde azaltılır:

```
V_new = V_new - leak
```

#### 3. Ateşleme ve Sıfırlama

* Eğer `V` değeri belirlenen **eşik (threshold)** değerine ulaşır veya aşarsa:

  * Nöron **1 adet çıkış spike'ı** üretir
  * Zar potansiyeli **0.0** değerine sıfırlanır

Bu mekanizma, biyolojik nöronlardaki **refrakter dönem** davranışını simüle eder.

---

## Özet Akış

1. Ham ses kaydı alınır
2. Downsampling uygulanır
3. Wavelet detay katsayıları çıkarılır
4. Eşikleme ile spike dizisi üretilir
5. Spike dizisi LIF nörona beslenir

Bu yapı, spike tabanlı sinir ağları (SNN) için temel bir ses işleme hattı sunar.

# Insider Web Test Otomasyon Projesi

## Gereksinimler

- Python 3.x
- Google Chrome Tarayıcısı
- pip (Python paket yöneticisi)

## Kurulum

1. Projeyi bilgisayarınıza klonlayın:
```bash
git clone [gh repo clone emiryilmazz/InsiderQAAutomationTest]
cd InsiderQATest
```

2. Gerekli Python paketlerini yükleyin:
```bash
pip install -r requirements.txt
```

3. ChromeDriver'ı indirin:
   - ChromeDriver'ı [buradan](https://chromedriver.chromium.org/downloads) indirin
   - İndirilen ChromeDriver'ı proje klasörüne kopyalayın

## Proje Yapısı

```
InsiderQATest/
├── locators/
│   ├── __init__.py
│   └── insider_locators.py
├── pages/
│   ├── __init__.py
│   ├── home_page.py
│   ├── careers_page.py
│   └── positions_page.py
├── tests/
│   ├── __init__.py
│   └── test_insider_steps.py
├── Screenshots/
├── chromedriver.exe
└── requirements.txt
```

## Test Senaryosu

Test aşağıdaki adımları gerçekleştirir:
1. Ana sayfaya git ve logo kontrolü yap
2. Company menüsünden Careers sayfasına git
3. Careers sayfasındaki bölümleri kontrol et
4. Find your dream job butonuna tıkla ve Open Positions sayfasına git
5. Filter by Department kısmından "Quallity Assurance" seçeneğini seç
6. Filter by Location kısmından İstanbul lokasyonunu seç
7. Rastgele bir iş ilanı seç View Role butonuna tıkla ve başvuru kısmına git

# Tüm testleri çalıştır
pytest tests/test_insider_steps.py -v

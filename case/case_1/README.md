## Asumsi
- Data discrap dari halaman pencarian dengan filter dan pengurutan default Tokopedia
- Data yang didapatkan berupa nama produk (exact), harga (exact), total penjualan (estimate), dan muncul di halaman ke berapa (exact)

## Tantangan
- Sistem anti-scraping Tokopedia yang kemungkinan dapat memblokir IP dan webdriver tertentu.
- Identifier elemen-elemen yang sering berubah.
- Lazy loading dari web Tokopedia yang membuat tidak semua elemen langsung terload ketika membuka halaman pencarian.
- Error yang disebabkan oleh berbagai hal.

## Pembelajaran
- Scraping awalnya berjalan lancar namun setelah beberapa saat terjadi kendala website tidak mau terload. Hal ini mengindikasikan bahwa Tokopedia memiliki sistem anti-scraping yang aktif, dengan memblokir IP client yang diduga melakukan scraping. Namun setelah membaca beberapa sumber, hal ini diatasi dengan mengganti chromedriver menjadi firefoxdriver.
- Elemen yang memuat data-data penting sering kali berubah identifiernya, misal id atau class name nya. Hal ini dapat diatasi dengan menggunakan pencarian XPath.
- Lazy loading web Tokopedia dapat diatasi dengan wait dengan webdriver dan melakukan behaviour scrolling.
- Diperlukan handling ketika jumlah halaman kurang dari total halaman yang diminta client, yaitu dengan mengecek apakah ada element button untuk next page.
- Diperlukan error handling ketika program tidak berjalan dengan semestinya.

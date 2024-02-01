## Masalah scraping secara masal
- Legal issue
    Saat ini, setahu saya, belum ada peraturan yang mengatur tentang kebijakan scraping data di Indonesia. Namun di beberapa negara yang sudah memiliki peraturan tentang scraping, scraping data dapat menjadi tricky karena harus mematuhi peraturan yang berlaku. Bisa jadi di masa depan, pemerintah Indonesia lebih aware dengan issue ini dan menerapkan peraturan tentang scraping data.
- Sistem anti-scraping
    Sistem anti-scraping seperti IP blocking dan rate limiter dengan captcha dapat menghambat scraping data secara masal. Hal ini dapat diatasi dengan penggunaan fake IP (proxy), menirukan behaviour manusia, dan meminimalkan scraping secara paralel agar tidak mencapai rate limit.
- Kualitas data hasil scraping
    Banyak hal yang dapat menyebabkan kualitas data hasil dari scraping menurun, seperti perubahan identifier elemen yang memuat data-data penting dan sistem anti-scraping. Hal tersebut dapat diatasi dengan hotfix, namun untuk indentifikasi masalah dan perbaikan yang dapat dikakukan dengan cepat diperlukan sistem alerting yang real time.
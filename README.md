# Soal Technical

Jawaban soal technical ada di folder masing-masing. Untuk melakukan test terhadap hasil dari function jawaban yang telah dibuat dapat menggunakan unit test yang sudah disediakan. Step untuk menjalankan unit test:
- buat python virtual environment
    ```
    virtualenv env
    ```
- aktifkan virtual environment
    ```
    . env/bin/activate
    ```
- install python package yang diperlukan
    ```
    pip install -r requirements.txt 
    ```
- jalankan unit test
    ```
    pytest
    ```

# Soal Case Study

Jawaban soal case study ada di folder masing-masing. Untuk menjalankan script scrapingnya, perlu menjalankan script di atas terlebih dahulu (membuat virtual environment dan menginstall package yang diperlukan). Kemudian jalankan script ini:
```
python case/case_1/main.py
```
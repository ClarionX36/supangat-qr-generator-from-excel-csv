# SUPANGAT QR Code Generator

Aplikasi desktop berbasis Python menggunakan pustaka **Tkinter** yang dirancang untuk memudahkan pembuatan QR Code secara massal (*bulk*) langsung dari file **Excel (.xlsx, .xls)** atau **CSV**.

## ✨ Fitur Utama
- **Multi-Format Support**: Mendukung pembacaan file format Excel (`.xlsx`, `.xls`) dan CSV dengan deteksi pemisah (*separator*) otomatis.
- **Pemilihan Sheet Dinamis**: Memilih sheet tertentu pada file Excel menggunakan menu dropdown interaktif.
- **Kustomisasi Kolom Fleksibel**: Bebas menentukan kolom data untuk isi QR Code serta kolom untuk nama file gambar (`.png`).
- **Pembersihan Nama File (*Sanitize*)**: Otomatis menyaring karakter ilegal agar nama file aman disimpan di berbagai sistem operasi.
- **Antarmuka Grafis (GUI)**: Tampilan antarmuka desktop yang bersih, ringan, dan mudah digunakan.

---

## 🛠️ Kebutuhan Sistem & Dependensi

Pastikan Anda telah menginstal **Python (3.8 atau yang lebih baru)** di komputer Anda. 

Pustaka/library Python yang dibutuhkan:
* `pandas` (Pengolahan data tabular)
* `openpyxl` (Membaca file Excel)
* `qrcode` (Pembangkit QR Code)
* `tkinter` (Biasanya sudah disertakan secara *default* dalam instalasi standar Python)

---

## 🚀 Cara Instalasi & Menjalankan

1. **Clone repository ini** (atau unduh sebagai ZIP):
   ```bash
   git clone [https://github.com/ClarionX36/supangat-qr-generator-from-excel-csv.git](https://github.com/ClarionX36/supangat-qr-generator-from-excel-csv.git)
   cd supangat-qr-generator-from-excel-csv

```

2. **Buat file dependensi (`requirements.txt`)** di folder utama dengan isi berikut:
```text
pandas>=1.0.0
openpyxl>=3.0.0
qrcode>=7.0

```


3. **Instal dependensi** melalui terminal/command prompt:
```bash
pip install -r requirements.txt

```


4. **Jalankan aplikasi**:
```bash
python qr.py

```



---

## 📖 Cara Penggunaan

1. Jalankan aplikasi, lalu klik tombol **"Cari File..."** untuk memilih file Excel atau CSV sumber data Anda.
2. Jika menggunakan file Excel, pilih **Sheet** yang ingin diproses melalui menu dropdown yang tersedia.
3. Tentukan kolom pada bagian pengaturan:
* **Kolom Isi QR Code**: Berisi data/teks/tautan yang akan diubah menjadi bentuk QR.
* **Kolom Nama File**: Berisi teks yang akan dijadikan nama file gambar hasil (`.png`).


4. Klik tombol hijau **"Generate QR Code"**.
5. Pilih folder direktori tujuan penyimpanan file QR Code di komputer Anda. Tunggu hingga proses selesai dan dialog sukses muncul!

---

## 📁 Struktur Repositori

```text
supangat-qr-generator-from-excel-csv/
│
├── qr.py               # Script utama aplikasi Python (Tkinter & Pandas)
├── requirements.txt    # Daftar pustaka/library Python
└── README.md           # Dokumentasi proyek

```

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

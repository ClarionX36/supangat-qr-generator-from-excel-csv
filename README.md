**# SUPANGAT QR Code Generator

Aplikasi desktop berbasis Python menggunakan pustaka **Tkinter** yang dirancang untuk memudahkan pembuatan QR Code secara massal (*bulk*) langsung dari file **Excel (.xlsx, .xls)** atau **CSV**.

## ✨ Fitur Utama
- **Multi-Format Support**: Mendukung pembacaan file format Excel (`.xlsx`, `.xls`) dan CSV (dengan deteksi pemisah/separator otomatis).
- **Pemilihan Sheet**: Memilih sheet tertentu pada file Excel dengan mudah menggunakan dropdown.
- **Kustomisasi Kolom**: Bebas menentukan kolom mana yang akan dijadikan isi/data QR Code dan kolom mana yang akan digunakan sebagai nama file gambar (`.png`).
- **Pembersihan Nama File (*Sanitize*)**: Otomatis membersihkan karakter ilegal pada nama file agar aman disimpan di berbagai sistem operasi.
- **Antarmuka Grafis (GUI)**: Tampilan antarmuka desktop yang bersih, interaktif, dan mudah digunakan.

---

## 🛠️ Kebutuhan Sistem & Dependensi

Pastikan Anda telah menginstal **Python (3.8 atau yang lebih baru)** di komputer Anda. 

Pustaka/library Python yang dibutuhkan:
* `pandas` (Pengolahan data tabular)
* `openpyxl` (Membaca file Excel)
* `qrcode` (Pembangkit QR Code)
* `tkinter` (Biasanya sudah bawaan dari instalasi standar Python di Windows/macOS)

---

## 🚀 Cara Instalasi & Menjalankan

1. **Clone repository ini** (atau unduh sebagai ZIP):
   ```bash
   git clone [https://github.com/USERNAME/nama-repo-anda.git](https://github.com/USERNAME/nama-repo-anda.git)
   cd nama-repo-anda**

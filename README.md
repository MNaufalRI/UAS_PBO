# 🦠 Hantavirus Outbreak Management & Analysis System
Sistem Analisis Manajemen Wabah Hantavirus adalah aplikasi berbasis CLI (*Command Line Interface*) yang dirancang khusus untuk mengolah, menganalisis, dan menyajikan laporan komprehensif dari data surveilans epidemiologi secara terstruktur. 
Sistem ini dibangun dengan mengimplementasikan prinsip Pemrograman Berorientasi Objek (**OOP**) tingkat lanjut serta memenuhi lima prinsip desain **SOLID** untuk memastikan kode mudah dipelihara (*maintainable*), diuji (*testable*), dan dikembangkan (*extensible*).
---
## 🚀 Fitur Utama
Sistem menyediakan 6 modul analisis analitik mendalam yang dieksekusi secara otomatis dari berkas dataset:
1. **Analisis Klinis Keparahan** – Menghitung tingkat rawat inap (*hospitalization rate*) dan tingkat fatalitas kasus (*Case Fatality Rate* / CFR).
2. **Analisis Demografis Pasien** – Menyajikan rata-rata usia pengidap beserta distribusi kelompok umur dan gender.
3. **Analisis Jalur Transmisi** – Mengidentifikasi metode penularan utama dan klaster lokasi paparan tertinggi.
4. **Analisis Klimatologi Lingkungan** – Menghitung korelasi rata-rata suhu dan kelembaban terhadap sebaran kasus.
5. **Analisis Manajemen Karantina** – Mengukur efisiensi durasi isolasi mandiri serta rata-rata waktu pemulihan pasien.
6. **Analisis Karakteristik Varian (Strain)** – Menyediakan metrik performa komparatif antargolongan strain virus.
7. **Laporan Eksekutif Otomatis** – Mengompilasi seluruh analisis menjadi kesimpulan ringkas beserta rekomendasi tindakan medis.
8. **Pengujian Unit Otomatis** – Modul pengujian internal yang terintegrasi menggunakan *framework* `unittest`.
---
## 📐 Arsitektur Kode & Penerapan SOLID
Aplikasi ini dirancang menggunakan arsitektur berlapis (*Layered Architecture*) untuk memisahkan tanggung jawab komponen secara tegas:
| Komponen / Berkas | Peran Arsitektur | Implementasi Konsep OOP & SOLID |
| :--- | :--- | :--- |
| `model.py` | **Domain Model Layer** | Enkapsulasi data pasien dan rekam medis melalui properti privat, Asosiasi/Komposisi, serta Polimorfisme (*dunder method override*). |
| `repository.py` | **Data Access Layer** | Menggunakan Abstraksi (`ABC`). Menerapkan *Interface Segregation Principle* (ISP) dan *Dependency Inversion Principle* (DIP). |
| `analyzer.py` | **Analysis Engine Layer** | Memanfaatkan Pewarisan (*Inheritance*), Polimorfisme (*Method Overriding*), *Single Responsibility Principle* (SRP), *Open/Closed Principle* (OCP), dan *Liskov Substitution Principle* (LSP). |
| `service.py` | **Business Logic Layer** | Menjembatani UI dan Data. Memenuhi prinsip SRP (memisahkan UI dari kalkulasi data) serta DIP (bergantung pada abstraction repository). |
| `main.py` | **Presentation Layer (CLI)** | Berfungsi sebagai pengatur antarmuka pengguna berbasis menu dinamis memanfaatkan *Action Map Dictionary* (memenuhi OCP). |
| `test_analyzer.py` | **Testing Layer** | Menyediakan skenario *automated unit testing* terisolasi untuk memverifikasi akurasi perhitungan matematis pada mesin analisis. |
---
## 📂 Struktur Direktori
```text
├── global_hantavirus_surveillance_dataset_2026.csv  # Sumber data utama
├── model.py                                         # Blueprint entitas objek data
├── repository.py                                    # Komponen manajemen pembacaan file
├── analyzer.py                                      # Mesin komputasi rumus analisis
├── service.py                                       # Pengendali logika bisnis aplikasi
├── main.py                                          # Alur utama aplikasi & CLI Menu
└── test_analyzer.py                                 # Berkas unit testing otomatis
```
---
## 🛠️ Prasyarat Sistem
Aplikasi ini dirancang menggunakan pustaka bawaan (*standard library*) dari Python tanpa memerlukan dependensi eksternal dari pihak ketiga (seperti `pandas`, `numpy`, dll.).

- **Python:** Versi 3.x atau yang lebih baru.
- **Sistem Operasi:** Windows, macOS, atau Linux.
- **Dataset:** Pastikan berkas `global_hantavirus_surveillance_dataset_2026.csv` berada di dalam direktori atau folder yang sama dengan berkas-berkas Python di atas.
---
## 💻 Cara Penggunaan
Ikuti langkah-langkah di bawah ini untuk menjalankan program melalui Terminal, Command Prompt, atau PowerShell:

1. Buka terminal atau terminal bawaan di VSCode.
2. Arahkan direktori aktif ke folder tempat kamu menyimpan seluruh berkas proyek ini.
3. Jalankan perintah berikut:

```bash
python main.py
```

### Panduan Navigasi Menu CLI

| Menu | Fungsi |
| :---: | :--- |
| **Menu 1** | ⚠️ **Langkah Awal (Wajib)** – Memuat data dari berkas CSV ke dalam sistem sebelum melakukan analisis. |
| **Menu 2** | Melihat sampel data yang berhasil dimuat (*Pemeriksaan Data*). |
| **Menu 3–8** | Melihat hasil analisis spesifik untuk tiap parameter medis dan lingkungan (*Analisis Sektoral*). |
| **Menu 9** | Menampilkan kompilasi ringkasan eksekutif dan rekomendasi tindakan secara keseluruhan (*Ringkasan Komprehensif*). |
| **Menu 11** | Menghentikan jalannya program (*Keluar*). |

---
## 🧪 Menjalankan Pengujian Otomatis
Aplikasi menyediakan modul *Unit Testing* terintegrasi untuk menjamin validitas dan akurasi rumus kalkulasi pada komponen analisis data. Pengujian dapat dilakukan dengan dua cara alternatif:

### 1. Melalui Menu Utama Aplikasi
Pilih opsi **Menu 10** dari dalam antarmuka menu saat program utama (`main.py`) sedang berjalan.

### 2. Melalui Perintah Terminal Secara Terpisah
Jika ingin menjalankan pengujian secara langsung tanpa membuka menu program utama, eksekusi perintah berikut di terminal kamu:

```bash
python -m unittest test_analyzer.py
```

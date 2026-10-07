# Tugas Mandiri: Python Advanced Topics 🚀

Selamat datang di repositori solusi **Tugas Mandiri: Python Advanced Topics** untuk mata kuliah **Pemrograman Berorientasi Objek (PBO)**. Repositori ini berisi implementasi solusi komprehensif untuk tiga studi kasus nyata yang dirancang untuk mengasah pemahaman fitur-fitur lanjutan Python.

---

## 👤 Identitas Mahasiswa
- **Nama Lengkap** : Abbi Maulana Malik
- **NIM**          : 2595114007
- **Mata Kuliah**  : Pemrograman Berorientasi Objek (PBO)
- **Semester**     : 3 (Ganjil)
- **Dosen Pengampu**: Tim Dosen Pengampu Pemrograman Berorientasi Objek (Pak Edwin)

---

## 📋 Ringkasan 3 Studi Kasus

| Direktori Kasus | Topik Utama | Konsep Python Utama | Status |
| :--- | :--- | :--- | :---: |
| [`case-01-analisis-nilai`](case-01-analisis-nilai/) | Analisis Nilai Mahasiswa | List Comprehension, Lambda Function, Pythonic Sorting & Filtering | Selesai |
| [`case-02-iot-generator`](case-02-iot-generator/) | Streaming Sensor IoT Hemat Memori | Generator Function (`yield`), Iterator Pattern (`next()`), Memory Profiling | Selesai |
| [`case-03-login-security`](case-03-login-security/) | Sistem Keamanan Akun & Audit Trail | Regular Expressions (`re`), `@property` Encapsulation, Python Decorator & Closure | Selesai |

---

### 1. [Studi Kasus 1: Analisis Nilai Mahasiswa](case-01-analisis-nilai/)
- **Masalah**: Mengolah tumpukan data mentah nilai akademik mahasiswa tanpa *nested for-loop* manual yang panjang dan lambat.
- **Solusi**:
  - Menghitung nilai akhir dengan bobot resmi (Tugas: 30%, UTS: 30%, UAS: 40%) menggunakan **List Comprehension**.
  - Mengurutkan klasemen mahasiswa dari peraih nilai tertinggi ke terendah menggunakan `sorted()` dengan `key=lambda`.
  - Memfilter mahasiswa berprestasi (nilai akhir > 80.0) secara deklaratif.
  - Mengumumkan mahasiswa terbaik (Peringkat 1) dengan rincian lengkap.

### 2. [Studi Kasus 2: Streaming Data Sensor IoT Hemat Memori](case-02-iot-generator/)
- **Masalah**: Pembacaan ribuan titik sensor cuaca berpotensi menguras RAM server jika seluruh data dimuat sekaligus ke dalam list (*eager evaluation*).
- **Solusi**:
  - Mengimplementasikan generator function `sensor_suhu_generator` dengan kata kunci `yield` untuk memproduksi angka suhu (15.0°C - 38.0°C) secara *lazy evaluation* (*on-demand*).
  - Mengonsumsi data bertahap satu per satu menggunakan pemanggilan `next()`.
  - Mengelompokkan status kondisi suhu secara real-time: Dingin (< 20°C), Normal (20°C - 30°C), dan Panas (> 30°C).
  - Menyediakan pembuktian efisiensi memori: generator mempertahankan jejak memori konstan $O(1)$ (~280 bytes) yang menghemat lebih dari **99,9%** memori dibandingkan list konvensional pada 100.000 data.

### 3. [Studi Kasus 3: Sistem Keamanan Akun & Audit Log Login](case-03-login-security/)
- **Masalah**: Verifikasi kredensial login memerlukan aturan format ketat agar akun terlindungi, serta pencatatan audit trail otomatis tanpa mengotori logika utama otentikasi.
- **Solusi**:
  - Validasi ketat format kredensial menggunakan modul `re` (RegEx):
    - Username: `^[a-zA-Z0-9]{5,}$` (min. 5 karakter alfanumerik, tanpa simbol/spasi).
    - Password: `^(?=.*\d).{8,}$` (min. 8 karakter & wajib memuat angka).
  - Class `User` dengan getter/setter `@property` untuk enkapsulasi kredensial yang aman.
  - Decorator `@audit_trail` yang membungkus fungsi `proses_login` untuk mencatat timestamp, username, status (`BERHASIL`/`DITOLAK`), dan alasan kegagalan ke dalam rekap riwayat audit trail.
  - Skenario pengujian lengkap: validasi username salah, password salah/tanpa angka, kredensial tidak terdaftar, hingga login berhasil.

---

## 🗂️ Struktur Direktori Repositori

```text
python-advanced-case-study/
│
├── README.md                            <- Identitas, ringkasan studi kasus, & panduan repositori
├── generate_screenshot.py               <- Helper utility rendering terminal screenshot PNG
│
├── case-01-analisis-nilai/
│   ├── main.py                          <- Solusi kalkulasi nilai dan ranking
│   ├── output.png                       <- Screenshot bukti program berhasil jalan
│   └── README.md                        <- Penjelasan konsep & cara menjalankan kasus 1
│
├── case-02-iot-generator/
│   ├── main.py                          <- Solusi streaming sensor dengan yield & memory analysis
│   ├── output.png                       <- Screenshot bukti program berhasil jalan
│   └── README.md                        <- Penjelasan konsep & cara menjalankan kasus 2
│
└── case-03-login-security/
    ├── main.py                          <- Solusi validasi regex, decorator log, & @property
    ├── output.png                       <- Screenshot bukti program berhasil jalan
    └── README.md                        <- Penjelasan konsep & cara menjalankan kasus 3
```

---

## ⚙️ Petunjuk Menjalankan Program

Setiap studi kasus dirancang sebagai modul mandiri dan dapat dijalankan langsung:

```bash
# Menjalankan Studi Kasus 1
cd case-01-analisis-nilai
python main.py

# Menjalankan Studi Kasus 2
cd ../case-02-iot-generator
python main.py

# Menjalankan Studi Kasus 3
cd ../case-03-login-security
python main.py
```

---

## 📈 Checklist Progres Pengerjaan

- [x] **Studi Kasus 1**:
  - [x] Dataset awal minimal 5 mahasiswa (6 data mahasiswa).
  - [x] Perhitungan bobot Nilai Akhir (Tugas 30%, UTS 30%, UAS 40%) dengan *List Comprehension*.
  - [x] Filter mahasiswa berprestasi (Nilai > 80.0) tanpa loop bersarang.
  - [x] Pemeringkatan (ranking) dengan `sorted()` dan `lambda`.
  - [x] Pengumuman mahasiswa peringkat 1 (Terbaik).
  - [x] `output.png` bukti eksekusi terminal & `README.md` terlampir.

- [x] **Studi Kasus 2**:
  - [x] Simulator pembacaan data suhu sensor berbasis generator function (`yield`).
  - [x] Konsumsi data streaming satu per satu menggunakan `next()`.
  - [x] Kategorisasi suhu otomatis (Dingin, Normal, Panas).
  - [x] Tampilan minimal 10 kali pembacaan berturut-turut (12 pembacaan).
  - [x] Analisis efisiensi memori (Generator vs List raksasa).
  - [x] `output.png` bukti eksekusi terminal & `README.md` terlampir.

- [x] **Studi Kasus 3**:
  - [x] Validasi RegEx untuk Username (min. 5 char alfanumerik).
  - [x] Validasi RegEx untuk Password (min. 8 char & wajib memuat angka).
  - [x] Class `User` dengan enkapsulasi `@property` & setter.
  - [x] Decorator `@audit_trail` pencatat timestamp, username, status, dan alasan.
  - [x] Pengujian skenario kegagalan dan keberhasilan otentikasi.
  - [x] `output.png` bukti eksekusi terminal & `README.md` terlampir.

- [x] **Standar Repositori & Git**:
  - [x] Struktur folder mandiri per kasus.
  - [x] Dokumentasi `README.md` di root dan masing-masing sub-folder.
  - [x] Tangkapan layar bukti eksekusi nyata (`output.png`).
  - [x] Riwayat commit git bertahap dan bermakna (*semantic commits*).

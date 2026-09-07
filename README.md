<div align="center">

# 🐍 Pemrograman Berorientasi Objek (PBO)
### **Semester 3 • Program Studi Informatika / FTI • Universitas Hasyim Asy'ari**

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Course](https://img.shields.io/badge/Course-PBO--Python-4B8BBE?style=for-the-badge&logo=codeforces&logoColor=white)](https://github.com/)
[![Campus](https://img.shields.io/badge/Campus-UNHASY%20Tebuireng-006A4E?style=for-the-badge&logo=google-earth&logoColor=white)](https://unhasy.ac.id/)
[![License](https://img.shields.io/badge/License-MIT-F7DF1E?style=for-the-badge&logo=opensourceinitiative&logoColor=black)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-Yes-success?style=for-the-badge)](https://github.com/)

<p align="center">
  <b>Arsip Latihan, Praktikum Mandiri, Tugas Proyek, dan Eksplorasi OOP berbasis Python</b><br>
  Mata Kuliah Pemrograman Berorientasi Objek (PBO) — Tahun Akademik Semester Ganjil
</p>

---

[Ringkasan](#-ikhtisar-mata-kuliah) •
[Dosen & Mahasiswa](#-informasi-akademik) •
[4 Pilar OOP](#-4-pilar-oop-dalam-python) •
[Silabus & Progres](#-roadmap--silabus-perkuliahan) •
[Struktur Direktori](#-struktur-repositori) •
[Memulai](#-instalasi--menjalankan-kode)

---

</div>

## 📌 Ikhtisar Mata Kuliah

Repositori ini disusun sebagai dokumentasi akademik dan *code showcase* untuk mata kuliah **Pemrograman Berorientasi Objek (Object-Oriented Programming - OOP)**. Berbeda dengan pendekatan prosedural, di sini kita merancang solusi perangkat lunak menggunakan paradigma objek dengan memanfaatkan fleksibilitas dan sintaks elegan dari bahasa pemrograman **Python**.

> *"Simple is better than complex. Readability counts."*  
> — **The Zen of Python (PEP 20)**

---

## 👨‍🏫 Informasi Akademik

| Komponen | Keterangan |
| :--- | :--- |
| **Dosen Pengampu** | **Edwin Hari Agus Prastyo, S.Kom., M.Kom.** |
| **Institusi** | Fakultas Teknologi Informasi (FTI), Universitas Hasyim Asy'ari (UNHASY) Tebuireng |
| **Mata Kuliah** | Pemrograman Berorientasi Objek (PBO) |
| **Mahasiswa** | `[Abbi Maulanha Malik]` |
| **NIM** | `[2595114007]` |
| **Kelas / Angkatan** | `[TI-A/2025]` |

---

## 🏛️ 4 Pilar OOP dalam Python

Materi inti difokuskan pada implementasi empat pilar OOP menggunakan mekanisme bawaan Python:

```
                  ┌─────────────────────────────────┐
                  │      4 PILAR OOP (PYTHON)       │
                  └─────────────────────────────────┘
                     │          │          │        │
     ┌───────────────┘          │          │        └───────────────┐
     ▼                          ▼          ▼                        ▼
┌──────────────┐         ┌───────────┐ ┌──────────────┐      ┌─────────────┐
│ ENCAPSULATION│         │INHERITANCE│ │ POLYMORPHISM │      │ ABSTRACTION │
│ _protected   │         │ super()   │ │ Method Over- │      │ from abc    │
│ __private    │         │ Multiple  │ │   riding &   │      │ import ABC, │
│ @property    │         │ Inherit.  │ │ Duck Typing  │      │ abstract-   │
│              │         │           │ │              │      │ method      │
└──────────────┘         └───────────┘ └──────────────┘      └─────────────┘
```

1. **Encapsulation (Enkapsulasi)**: Melindungi *state* internal objek memakai konvensi attribute naming (`_single_underscore`, `__double_underscore`) serta `@property`, `@<name>.setter`.
2. **Inheritance (Pewarisan)**: Menurunkan logika dan perilaku kelas induk ke kelas anak via sintaks `class Child(Parent):` dan `super().__init__()`, termasuk dukungan *Multiple Inheritance* dan *Method Resolution Order (MRO)*.
3. **Polymorphism (Polimorfisme)**: Memanfaatkan *Duck Typing* (*"If it walks like a duck and quacks like a duck..."*), method overriding, dan antarmuka dinamis seragam antar-kelas.
4. **Abstraction (Abstraksi)**: Menyembunyikan kompleksitas implementasi menggunakan modul bawaan `abc` (`ABC`, `@abstractmethod`).

---

## 🗺️ Roadmap & Silabus Perkuliahan

| Sesi | Materi Pembelajaran | Fokus Utama di Python | Status |
| :---: | :--- | :--- | :---: |
| **01** | Pengantar OOP vs Prosedural | Penyiapan Environment, Konsep Class & Instance | ✅ Selesai |
| **02** | Constructor & Instance Attributes | `__init__()`, `self`, Class Variable vs Instance Variable | ✅ Selesai |
| **03** | Python Magic / Dunder Methods | `__str__()`, `__repr__()`, `__len__()`, `__eq__()` | ✅ Selesai |
| **04** | **Pilar 1: Encapsulation** | Private Attributes (`__`), `@property`, Getter & Setter | 🔄 Berjalan |
| **05** | **Pilar 2: Inheritance** | Single & Multi-level Inheritance, fungsi `super()` | ⏳ Antrean |
| **06** | **Pilar 3: Polymorphism** | Method Overriding, Duck Typing, Operator Overloading | ⏳ Antrean |
| **07** | **Pilar 4: Abstraction** | Module `abc`, `abstractmethod`, Interface Contracts | ⏳ Antrean |
| **UTS** | **Ujian Tengah Semester** | **Review Teori & Implementasi Proyek Studi Kasus** | ⏳ Antrean |
| **08** | Object Relationship & UML | Association, Aggregation, Composition di Python | ⏳ Antrean |
| **09** | Robust Code: Exception Handling | Custom Exception Class, `try-except-else-finally` | ⏳ Antrean |
| **10** | Persistence: File I/O & JSON | Serialisasi Object (`pickle`, `json`, `dataclasses`) | ⏳ Antrean |
| **11** | Database Integration (CRUD) | Koneksi OOP ke SQLite3 / MySQL (`sqlite3`, `PyMySQL`) | ⏳ Antrean |
| **12** | GUI Desktop Development | PyQt6 / CustomTkinter berbasis arsitektur OOP | ⏳ Antrean |
| **13** | Design Pattern Dasar | Singleton, Factory Method, Observer Pattern | ⏳ Antrean |
| **14** | Architecture & Clean Code | Modularisasi Package, Type Hinting (`typing`), Docstrings | ⏳ Antrean |
| **UAS** | **Ujian Akhir Semester** | **Presentasi Final Project GUI/Database Desktop App** | ⏳ Antrean |

---

## 📂 Struktur Repositori

```bash
PBO-semester-3/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt            # Daftar pustaka pendukung (CustomTkinter, PyMySQL, dll.)
│
├── 01_dasar_oop/               # Class, object, instance variables
│   ├── 01_class_object.py
│   └── 02_constructor_init.py
│
├── 02_dunder_methods/          # Magic methods (__str__, __repr__, dll.)
│   └── dunder_examples.py
│
├── 03_enkapsulasi/             # Private variables, property decorators
│   ├── rekening_bank.py
│   └── properti_setter.py
│
├── 04_pewarisan/               # Single, multiple, hierarchical inheritance
│   ├── inheritance_dasar.py
│   └── multiple_inheritance_mro.py
│
├── 05_polimorfisme/            # Method overriding & duck typing
│   └── duck_typing_demo.py
│
├── 06_abstraksi/               # Modul abc dan abstract class
│   └── abstract_payment_gateway.py
│
├── tugas_mandiri/              # Kumpulan tugas mingguan
│   ├── tugas_01/
│   └── tugas_02/
│
├── project_uts/                # Proyek Ujian Tengah Semester
│   └── sistem_kasir_oop/
│
└── project_uas/                # Proyek Akhir Terintegrasi (GUI + Database)
    ├── assets/
    ├── database/
    ├── src/
    └── main.py
```

---

## 🛠️ Instalasi & Menjalankan Kode

### 1. Prasyarat
Pastikan Anda telah menginstal **Python 3.10** atau versi yang lebih baru pada perangkat Anda. Periksa dengan:
```bash
python --version
# atau
python3 --version
```

### 2. Clone Repositori
```bash
git clone https://github.com/[username-github-anda]/PBO-semester-3.git
cd PBO-semester-3
```

### 3. Buat Virtual Environment *(Disarankan)*
```bash
# Membuat virtual environment
python -m venv venv

# Aktivasi venv:
# Windows (PowerShell/CMD):
venv\Scripts\activate

# Linux / macOS:
source venv/bin/activate
```

### 4. Instal Dependensi (Jika Diperlukan)
```bash
pip install -r requirements.txt
```

### 5. Jalankan Contoh Program
```bash
# Menjalankan salah satu modul latihan
python 03_enkapsulasi/rekening_bank.py
```

---

## 💡 Cuplikan Gaya Kode (OOP Python Standard)

Berikut adalah konvensi gaya penulisan kode berorientasi objek yang diterapkan di repositori ini (menggunakan *type hinting* dan *clean code*):

```python
from abc import ABC, abstractmethod

class Kendaraan(ABC):
    """Abstract base class yang mendefinisikan kontrak kendaraan."""
    
    def __init__(self, merk: str, tahun: int) -> None:
        self._merk = merk          # Protected attribute
        self.__tahun = tahun       # Private attribute

    @property
    def tahun(self) -> int:
        """Getter untuk atribut private tahun."""
        return self.__tahun

    @abstractmethod
    def nyalakan_mesin(self) -> str:
        """Method abstrak yang wajib diimplementasikan subclass."""
        pass


class Mobil(Kendaraan):
    def __init__(self, merk: str, tahun: int, model: str) -> None:
        super().__init__(merk, tahun)
        self.model = model

    def nyalakan_mesin(self) -> str:
        return f"Mesin mobil {self._merk} {self.model} ({self.tahun}) siap meluncur! 🚗💨"


if __name__ == "__main__":
    mobil_saya = Mobil("Toyota", 2024, "GR Yaris")
    print(mobil_saya.nyalakan_mesin())
```

---

## 🤝 Catatan & Kontribusi

* Repositori ini dikembangkan sebagai portofolio akademik pada perkuliahan PBO Semester 3.
* Dibuat mengikuti standar gaya penulisan **PEP 8**.
* Terbuka untuk diskusi, masukan, dan perbaikan logika program via tab **Issues** atau **Pull Request**.

---

<div align="center">
  <sub>Dibangun dengan ❤️ dan ☕ oleh Mahasiswa FTI UNHASY • Dosen Pengampu: <b>Edwin Hari Agus Prastyo, S.Kom., M.Kom.</b></sub><br>
  <sub><b>Universitas Hasyim Asy'ari Tebuireng Jombang</b></sub>
</div>

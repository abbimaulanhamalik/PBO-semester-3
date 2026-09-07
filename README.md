<div align="center">

# 🐍 Pemrograman Berorientasi Objek (PBO)
### Repositori Praktikum & Tugas Perkuliahan — Semester 3

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Campus](https://img.shields.io/badge/Kampus-UNHASY%20Tebuireng-005C29?style=for-the-badge&logo=google-earth&logoColor=white)](https://unhasy.ac.id/)
[![Course](https://img.shields.io/badge/Mata%20Kuliah-PBO%20Python-4B8BBE?style=for-the-badge&logo=codeforces&logoColor=white)](https://github.com/)
[![Code Style](https://img.shields.io/badge/Code%20Style-PEP%208-brightgreen?style=for-the-badge)](https://peps.python.org/pep-0008/)
[![Reference](https://img.shields.io/badge/Tutorial-Programiz-2563EB?style=for-the-badge&logo=google-chrome&logoColor=white)](https://www.programiz.com/python-programming/getting-started)

<p align="center">
  <b>Dokumentasi Pembelajaran, Praktikum Kode, dan Tugas Proyek Berorientasi Objek</b><br>
  Program Studi S1 Teknik Informatika • Fakultas Teknologi Informasi • Universitas Hasyim Asy'ari
</p>

---

[Profil](#-identitas-mahasiswa) •
[Referensi Modul](#-referensi-modul-pembelajaran) •
[4 Pilar OOP](#-4-pilar-oop-dalam-python) •
[Silabus & Progres](#-silabus--roadmap-materi) •
[Struktur Folder](#-struktur-direktori) •
[Cara Menjalankan](#-panduan-instalasi--menjalankan-kode)

---

</div>

## 👨‍🎓 Identitas Mahasiswa

| Informasi | Keterangan |
| :--- | :--- |
| **Nama Lengkap** | **Abbi Maulanha Malik** |
| **NIM** | **2595114007** |
| **Kelas / Angkatan** | **TI-A / 2025** |
| **Program Studi** | S1 Teknik Informatika |
| **Fakultas** | Fakultas Teknologi Informasi (FTI) |
| **Perguruan Tinggi** | Universitas Hasyim Asy'ari (UNHASY) Tebuireng |
| **Dosen Pengampu** | **Edwin Hari Agus Prastyo, S.Kom., M.Kom.** |

---

## 🌐 Referensi Modul Pembelajaran

Studi dan implementasi kode dalam repositori ini mengacu pada panduan silabus perkuliahan serta dokumentasi online:

* 📖 **Modul Praktik Utama**: [Programiz — Getting Started with Python](https://www.programiz.com/python-programming/getting-started)
* 📖 **Dokumentasi OOP Python**: [Python 3 Official Docs — Classes](https://docs.python.org/3/tutorial/classes.html)
* 📖 **Panduan Gaya Kode**: [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)

---

## 🏛️ 4 Pilar OOP dalam Python

Paradigma berorientasi objek dalam repositori ini berlandaskan empat pilar utama:

```
                  ┌─────────────────────────────────────────┐
                  │          4 PILAR UTAMA OOP              │
                  └─────────────────────────────────────────┘
                         │           │           │         │
       ┌─────────────────┘           │           │         └─────────────────┐
       ▼                             ▼           ▼                           ▼
┌───────────────┐             ┌───────────┐ ┌──────────────┐          ┌─────────────┐
│ ENCAPSULATION │             │INHERITANCE│ │ POLYMORPHISM │          │ ABSTRACTION │
│ _protected    │             │  super()  │ │   Method     │          │ from abc    │
│ __private     │             │  Tunggal/ │ │  Overriding  │          │ import ABC, │
│ @property     │             │  Multiple │ │& Duck Typing │          │ abstract-   │
│               │             │           │ │              │          │ method      │
└───────────────┘             └───────────┘ └──────────────┘          └─────────────┘
```

1. **Encapsulation (Enkapsulasi)**: Membatasi akses langsung ke variabel objek menggunakan konvensi `_protected`, atribut `__private`, serta memanfaatkan decorator `@property` dan `@setter`.
2. **Inheritance (Pewarisan)**: Menurunkan fungsi dan properti dari kelas induk (*parent*) ke kelas anak (*child*) menggunakan `super().__init__()`.
3. **Polymorphism (Polimorfisme)**: Memberikan perilaku dinamis melalui *method overriding* dan fleksibilitas *duck typing* khas Python.
4. **Abstraction (Abstraksi)**: Menyediakan cetak biru antarmuka tanpa mengekspos detail implementasi melalui modul bawaan `abc` (`ABC` dan `@abstractmethod`).

---

## 🗺️ Silabus & Roadmap Materi

| No | Modul / Topik | Fokus Bahasan | Referensi / Catatan | Status |
| :---: | :--- | :--- | :--- | :---: |
| **01** | **Python Fundamentals** | Sintaks dasar, variabel, tipe data, control flow | [Programiz Getting Started](https://www.programiz.com/python-programming/getting-started) | ✅ Selesai |
| **02** | **Class & Instance** | Blueprint class, constructor `__init__()`, keyword `self` | [Programiz OOP Basics](https://www.programiz.com/python-programming/class) | ✅ Selesai |
| **03** | **Dunder / Magic Methods** | `__str__()`, `__repr__()`, `__len__()`, `__eq__()` | Dokumentasi Python | 🔄 Berjalan |
| **04** | **Pilar 1: Encapsulation** | Private variable (`__`), Getter & Setter, `@property` | Latihan Studi Kasus | ⏳ Antrean |
| **05** | **Pilar 2: Inheritance** | Single/Multiple Inheritance, fungsi `super()` | Latihan Studi Kasus | ⏳ Antrean |
| **06** | **Pilar 3: Polymorphism** | Method Overriding, Duck Typing, Operator Overloading | Latihan Studi Kasus | ⏳ Antrean |
| **07** | **Pilar 4: Abstraction** | Abstract Base Classes (`ABC`), `@abstractmethod` | Latihan Studi Kasus | ⏳ Antrean |
| **UTS** | **Ujian Tengah Semester** | **Penerapan 4 Pilar OOP dalam Studi Kasus Mandiri** | Evaluasi Teori & Praktik | ⏳ Antrean |
| **08** | **Exception Handling** | Blok `try-except-else-finally`, Custom Exceptions | Programiz Exceptions | ⏳ Antrean |
| **09** | **File Handling & Serialisasi** | File I/O, format JSON, dan modul `pickle` | Pengolahan Data | ⏳ Antrean |
| **10** | **Database Integration** | Akses basis data SQLite / MySQL berbasis OOP | CRUD Data Mahasiswa | ⏳ Antrean |
| **11** | **GUI Programming** | Antarmuka grafis desktop (Tkinter / CustomTkinter) | Aplikasi GUI Kasir | ⏳ Antrean |
| **UAS** | **Ujian Akhir Semester** | **Aplikasi Desktop Terintegrasi (OOP + GUI + DB)** | Proyek Akhir Perkuliahan | ⏳ Antrean |

---

## 📂 Struktur Direktori

```text
PBO-semester-3/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
│
├── 01_python_fundamentals/
│   ├── getting_started.py
│   └── data_types_and_flow.py
│
├── 02_class_dan_object/
│   ├── class_dasar.py
│   └── constructor_dan_self.py
│
├── 03_enkapsulasi/
│   ├── bank_account.py
│   └── property_decorator.py
│
├── 04_pewarisan/
│   ├── single_inheritance.py
│   └── super_keyword.py
│
├── 05_polimorfisme/
│   ├── method_overriding.py
│   └── duck_typing.py
│
├── 06_abstraksi/
│   └── abstract_class_abc.py
│
├── tugas_mingguan/
│   ├── tugas_01/
│   └── tugas_02/
│
└── project_uas/
    ├── database/
    ├── src/
    └── main.py
```

---

## 🛠️ Panduan Instalasi & Menjalankan Kode

### 1. Kloning Repositori
```bash
git clone https://github.com/AbbiMaulanha/PBO-semester-3.git
cd PBO-semester-3
```

### 2. Buat & Aktifkan Virtual Environment *(Disarankan)*
* **Windows (PowerShell / Command Prompt):**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
* **Linux / macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Pasang Dependensi *(Opsional)*
Jika terdapat pustaka pihak ketiga pada `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Jalankan Berkas Program
```bash
python 01_python_fundamentals/getting_started.py
```

---

## 💻 Contoh Implementasi OOP (PEP 8)

```python
from abc import ABC, abstractmethod

class Mahasiswa(ABC):
    """Representasi kelas abstrak civitas akademika."""

    def __init__(self, nama: str, nim: str) -> None:
        self.nama = nama
        self.__nim = nim  # Private attribute

    @property
    def nim(self) -> str:
        """Getter untuk atribut private nim."""
        return self.__nim

    @abstractmethod
    def sapa(self) -> str:
        """Method abstrak wajib di-override oleh kelas turunan."""
        pass


class MahasiswaInformatika(Mahasiswa):
    def __init__(self, nama: str, nim: str, kelas: str) -> None:
        super().__init__(nama, nim)
        self.kelas = kelas

    def sapa(self) -> str:
        return f"Halo, saya {self.nama} ({self.nim}) dari kelas {self.kelas} FTI UNHASY!"


if __name__ == "__main__":
    mhs = MahasiswaInformatika("Abbi Maulanha Malik", "2595114007", "TI-A/2025")
    print(mhs.sapa())
```

---

<div align="center">
  <sub>Dikelola oleh <b>Abbi Maulanha Malik</b> • NIM: <b>2595114007</b></sub><br>
  <sub>Dosen Pengampu: <b>Edwin Hari Agus Prastyo, S.Kom., M.Kom.</b></sub><br>
  <sub><b>Program Studi Teknik Informatika • Universitas Hasyim Asy'ari (UNHASY) Tebuireng</b></sub>
</div>

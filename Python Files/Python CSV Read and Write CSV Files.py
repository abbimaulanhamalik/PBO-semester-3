"""Contoh membaca dan menulis file CSV menggunakan Python.

File CSV contoh dibuat di folder yang sama dengan program ini sehingga program
dapat langsung dijalankan tanpa membutuhkan file atau pustaka tambahan.
"""

import csv
from pathlib import Path


FOLDER_PROGRAM = Path(__file__).resolve().parent
PEOPLE_FILE = FOLDER_PROGRAM / "people.csv"
PROTAGONIST_FILE = FOLDER_PROGRAM / "protagonist.csv"


def buat_people_csv() -> None:
    """Membuat file people.csv berisi data orang."""
    rows = [
        ["Name", "Age", "Profession"],
        ["Jack", 23, "Doctor"],
        ["Miller", 22, "Engineer"],
    ]

    with PEOPLE_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def baca_people_dengan_reader() -> None:
    """Membaca people.csv menggunakan csv.reader()."""
    print("Membaca people.csv dengan csv.reader():")

    with PEOPLE_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def baca_people_dengan_dict_reader() -> None:
    """Membaca people.csv menggunakan csv.DictReader()."""
    print("\nMembaca people.csv dengan csv.DictReader():")

    with PEOPLE_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(
                f"Nama: {row['Name']}, "
                f"Umur: {row['Age']}, "
                f"Pekerjaan: {row['Profession']}"
            )


def buat_dan_baca_protagonist_csv() -> None:
    """Menulis dictionary ke protagonist.csv lalu membacanya kembali."""
    rows = [
        {"SN": 1, "Movie": "Lord of the Rings", "Protagonist": "Frodo Baggins"},
        {"SN": 2, "Movie": "Harry Potter", "Protagonist": "Harry Potter"},
    ]
    fieldnames = ["SN", "Movie", "Protagonist"]

    with PROTAGONIST_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print("\nIsi protagonist.csv:")
    with PROTAGONIST_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)


def main() -> None:
    buat_people_csv()
    baca_people_dengan_reader()
    baca_people_dengan_dict_reader()
    buat_dan_baca_protagonist_csv()
    print(f"\nFile CSV tersimpan di: {FOLDER_PROGRAM}")


if __name__ == "__main__":
    main()
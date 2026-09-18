"""Menerima input pengguna dan menyimpannya ke file CSV."""

import csv
from pathlib import Path


FILE_PATH = Path(__file__).resolve().parent / "people_input.csv"
FIELDNAMES = ["Name", "Age", "Profession"]


def minta_umur() -> int:
    """Meminta umur sampai pengguna memasukkan bilangan bulat yang valid."""
    while True:
        nilai = input("Umur: ").strip()
        try:
            umur = int(nilai)
        except ValueError:
            print("Umur harus berupa angka bulat.")
            continue

        if umur < 0:
            print("Umur tidak boleh negatif.")
            continue
        return umur


def simpan_data() -> None:
    """Mengumpulkan input dan menambahkannya sebagai satu baris CSV."""
    nama = input("Nama: ").strip()
    while not nama:
        print("Nama tidak boleh kosong.")
        nama = input("Nama: ").strip()

    umur = minta_umur()
    pekerjaan = input("Pekerjaan: ").strip()

    file_baru = not FILE_PATH.exists() or FILE_PATH.stat().st_size == 0
    with FILE_PATH.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        if file_baru:
            writer.writeheader()
        writer.writerow(
            {"Name": nama, "Age": umur, "Profession": pekerjaan}
        )

    print(f"Data berhasil disimpan ke: {FILE_PATH}")


def main() -> None:
    simpan_data()


if __name__ == "__main__":
    main()
"""
Studi Kasus 2: Streaming Data Sensor IoT Hemat Memori
Implementasi generator function untuk simulasi pembacaan data sensor IoT secara bertahap:
- Generator Function dengan kata kunci 'yield'
- Iterator Pattern & streaming data menggunakan next() atau lazy iteration
- Kategorisasi status suhu real-time (Dingin, Normal, Panas)
- Analisis efisiensi memori (Generator vs List konvensional)
"""

import random
import sys
import time


def sensor_suhu_generator(jumlah_data=10, min_suhu=15.0, max_suhu=38.0, seed=42):
    """
    Generator function yang memproduksi angka bacaan sensor suhu secara bertahap (on-demand/lazy evaluation).
    Rentang suhu: 15.0°C - 38.0°C.
    Tidak mengalokasikan seluruh deret data ke dalam memori list sekaligus.
    """
    # Gunakan seed agar hasil pengujian konsisten dan dapat direproduksi
    rng = random.Random(seed)
    for _ in range(jumlah_data):
        # Simulasi pembacaan suhu dari sensor dengan 1 angka desimal
        suhu = round(rng.uniform(min_suhu, max_suhu), 1)
        yield suhu


def kategorikan_suhu(suhu):
    """
    Mengkategorikan nilai suhu ke dalam status kondisi lingkungan:
    - Dingin : suhu < 20.0°C
    - Normal : 20.0°C <= suhu <= 30.0°C
    - Panas  : suhu > 30.0°C
    """
    if suhu < 20.0:
        return "Dingin"
    elif 20.0 <= suhu <= 30.0:
        return "Normal"
    else:
        return "Panas"


def demonstrasi_efisiensi_memori(n_titik_data=100_000):
    """
    Mendemonstrasikan perbandingan alokasi memori (RAM)
    antara list konvensional (eager evaluation) vs generator streaming (lazy evaluation).
    """
    print("\n" + "=" * 70)
    print(" ANALISIS EFISIENSI MEMORI (GENERATOR VS LIST BESAR) ".center(70, "="))
    print("=" * 70)

    # 1. Alokasi List Konvensional
    list_sensor = [round(random.uniform(15.0, 38.0), 1) for _ in range(n_titik_data)]
    ukuran_list_bytes = sys.getsizeof(list_sensor)

    # 2. Generator Object
    gen_sensor = sensor_suhu_generator(jumlah_data=n_titik_data)
    ukuran_gen_bytes = sys.getsizeof(gen_sensor)

    rasio_hemat = (ukuran_list_bytes - ukuran_gen_bytes) / ukuran_list_bytes * 100

    print(f" Jumlah Titik Data Uji  : {n_titik_data:,} data bacaan sensor")
    print(f" Ukuran List di RAM     : {ukuran_list_bytes:,} bytes (~{ukuran_list_bytes / 1024:.2f} KB)")
    print(f" Ukuran Generator di RAM: {ukuran_gen_bytes:,} bytes (~{ukuran_gen_bytes / 1024:.2f} KB)")
    print(f" Penghematan Memori     : {rasio_hemat:.2f}% lebih hemat memori!")
    print(" Kesimpulan             : Generator mempertahankan jejak memori O(1) konstan")
    print("                          tanpa mempedulikan seberapa besar jumlah data streaming.")
    print("=" * 70)


def main():
    print("=" * 70)
    print(" STASIUN CUACA IoT - MONITORING SUHU BERBASIS STREAMING ".center(70, "#"))
    print("=" * 70)
    print(" Mode         : Lazy Evaluation (Generator Streaming)")
    print(" Protokol     : Pemanggilan Iterator bertahap dengan next()")
    print(" Parameter    : Rentang Simulasi 15.0 C - 38.0 C")
    print("=" * 70)

    total_pembacaan = 12  # Minimal 10 kali pembacaan berturut-turut
    generator_cuaca = sensor_suhu_generator(jumlah_data=total_pembacaan, seed=2026)

    print(f"\n{'No':<4} | {'Timestamp':<10} | {'Suhu (C)':<12} | {'Kategori':<10} | {'Indikator Visual'}")
    print("-" * 70)

    nomor = 1
    # Konsumsi data satu per satu tanpa menampung ke dalam list besar
    while True:
        try:
            # Memanggil titik data berikutnya secara on-demand
            suhu = next(generator_cuaca)
            kategori = kategorikan_suhu(suhu)

            # Indikator visual berbasis teks kompatibel lintas platform
            if kategori == "Dingin":
                visual = "[DINGIN]  ----"
            elif kategori == "Normal":
                visual = "[NORMAL]  =========="
            else:
                visual = "[PANAS]   ================"

            total_menit = nomor * 5
            jam = 8 + (total_menit // 60)
            menit = total_menit % 60
            simulasi_waktu = f"{jam:02d}:{menit:02d}:00"
            print(f"{nomor:<4} | {simulasi_waktu:<10} | {suhu:<12.1f} | {kategori:<10} | {visual}")
            nomor += 1

        except StopIteration:
            # Sinyal bahwa generator telah selesai memproduksi data
            print("-" * 70)
            print(f" [INFO] Aliran data selesai. Total {nomor - 1} pembacaan berhasil diproses.")
            break

    # Tampilkan analisis efisiensi memori
    demonstrasi_efisiensi_memori(100_000)


if __name__ == "__main__":
    main()

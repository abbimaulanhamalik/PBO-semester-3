"""
Studi Kasus 1: Analisis Nilai Mahasiswa
Modul analisis data nilai mahasiswa menggunakan kapabilitas fungsional bawaan Python:
- List Comprehension untuk kalkulasi dan transformasi data
- Lambda Function untuk key sorting dan pemetaan ringkas
- Pythonic Filtering & Sorting dengan sorted(..., key=lambda, reverse=True)
"""

# 1. Dataset Awal Mahasiswa
data_mahasiswa = [
    {"nama": "Aisyah", "nim": "230101", "tugas": 85, "uts": 80, "uas": 88},
    {"nama": "Budi", "nim": "230102", "tugas": 70, "uts": 65, "uas": 75},
    {"nama": "Cantika", "nim": "230103", "tugas": 90, "uts": 85, "uas": 92},
    {"nama": "Dedi", "nim": "230104", "tugas": 60, "uts": 72, "uas": 68},
    {"nama": "Erina", "nim": "230105", "tugas": 95, "uts": 92, "uas": 96},
    {"nama": "Fajar", "nim": "230106", "tugas": 78, "uts": 82, "uas": 80},
]


def hitung_nilai_akhir(data):
    """
    Menghitung nilai akhir setiap mahasiswa menggunakan List Comprehension.
    Bobot penilaian:
    - Tugas : 30% (0.30)
    - UTS   : 30% (0.30)
    - UAS   : 40% (0.40)
    """
    return [
        {
            **mhs,
            "nilai_akhir": round(
                (mhs["tugas"] * 0.30) + (mhs["uts"] * 0.30) + (mhs["uas"] * 0.40), 2
            ),
        }
        for mhs in data
    ]


def filter_mahasiswa_berprestasi(data_terhitung, ambang_batas=80.0):
    """
    Memfilter mahasiswa dengan nilai akhir di atas ambang batas (> 80.0)
    secara Pythonic tanpa perulangan for bertingkat.
    """
    # Menggunakan List Comprehension dengan conditional filtering
    return [mhs for mhs in data_terhitung if mhs["nilai_akhir"] > ambang_batas]


def urutkan_peringkat(data_terhitung):
    """
    Mengurutkan seluruh mahasiswa dari nilai akhir tertinggi ke terendah
    menggunakan fungsi sorted() dengan parameter key berbasis lambda function.
    """
    return sorted(data_terhitung, key=lambda mhs: mhs["nilai_akhir"], reverse=True)


def cetak_tabel(data, judul="DATA MAHASISWA"):
    """Fungsi helper untuk mencetak tabel rapi di konsol terminal."""
    garis = "=" * 70
    garis_tipis = "-" * 70
    print(f"\n{garis}")
    print(f"{judul.center(70)}")
    print(garis)
    print(
        f"{'No':<4} | {'NIM':<8} | {'Nama':<12} | {'Tugas':<6} | {'UTS':<6} | {'UAS':<6} | {'Akhir':<6}"
    )
    print(garis_tipis)
    for idx, mhs in enumerate(data, start=1):
        print(
            f"{idx:<4} | {mhs['nim']:<8} | {mhs['nama']:<12} | {mhs['tugas']:<6} | {mhs['uts']:<6} | {mhs['uas']:<6} | {mhs['nilai_akhir']:<6.2f}"
        )
    print(garis)


def main():
    print("=" * 70)
    print(" SISTEM ANALISIS NILAI AKADEMIK MAHASISWA ".center(70, "#"))
    print("=" * 70)

    # 1. Hitung Nilai Akhir dengan List Comprehension
    data_dengan_nilai_akhir = hitung_nilai_akhir(data_mahasiswa)

    # 2. Pemeringkatan (Ranking) dengan sorted() dan key Lambda
    data_ranking = urutkan_peringkat(data_dengan_nilai_akhir)
    cetak_tabel(data_ranking, "KLASEMEN PERINGKAT NILAI MAHASISWA (TERTINGGI -> TERENDAH)")

    # 3. Filter Mahasiswa Berprestasi (Nilai Akhir > 80)
    berprestasi = filter_mahasiswa_berprestasi(data_ranking, ambang_batas=80.0)
    print("\n" + "#" * 70)
    print(" DAFTAR MAHASISWA BERPRESTASI (NILAI AKHIR > 80.0) ".center(70))
    print("#" * 70)
    for idx, mhs in enumerate(berprestasi, start=1):
        print(
            f" {idx}. [{mhs['nim']}] {mhs['nama']:<10} -> Nilai Akhir: {mhs['nilai_akhir']} "
            f"(Tugas: {mhs['tugas']}, UTS: {mhs['uts']}, UAS: {mhs['uas']})"
        )
    print(f" Total mahasiswa berprestasi: {len(berprestasi)} dari {len(data_mahasiswa)} mahasiswa")

    # 4. Mahasiswa Terbaik (Peringkat 1)
    mahasiswa_terbaik = data_ranking[0]
    print("\n" + "=" * 70)
    print(" PENGHARGAAN MAHASISWA TERBAIK (PERINGKAT 1) ".center(70, "*"))
    print("=" * 70)
    print(f" Nama Lengkap : {mahasiswa_terbaik['nama']}")
    print(f" NIM          : {mahasiswa_terbaik['nim']}")
    print(f" Nilai Akhir  : {mahasiswa_terbaik['nilai_akhir']}")
    print(
        f" Rincian Nilai: Tugas={mahasiswa_terbaik['tugas']} (30%), UTS={mahasiswa_terbaik['uts']} (30%), UAS={mahasiswa_terbaik['uas']} (40%)"
    )
    print(f" Status       : LULUS DENGAN PREDIKAT TERBAIK (CUM LAUDE)")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()

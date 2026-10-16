# ==============================================================================
# Tugas - Sesi #7: Python datetime.strftime()
# Mahasiswa : Abbi Maulanha Malik
# NIM       : 2595114007
# Kelas     : TI-A / 2025
# Matakuliah: Pemrograman Berorientasi Objek (PBO) - Python
# Dosen     : Edwin Hari Agus Prastyo, S.Kom., M.Kom.
# Sumber    : https://www.programiz.com/python-programming/datetime/strftime
# ==============================================================================

from datetime import datetime

def separator(title: str):
    print("\n" + "=" * 60)
    print(f" {title} ")
    print("=" * 60)

def main():
    # -------------------------------------------------------------------------
    # Example 1: datetime to string using strftime()
    # -------------------------------------------------------------------------
    separator("Example 1: datetime to string using strftime()")
    now = datetime.now()  # current date and time

    year = now.strftime("%Y")
    print("year:", year)

    month = now.strftime("%m")
    print("month:", month)

    day = now.strftime("%d")
    print("day:", day)

    time_str = now.strftime("%H:%M:%S")
    print("time:", time_str)

    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    print("date and time:", date_time)

    # -------------------------------------------------------------------------
    # Example 2: Creating string from a timestamp
    # -------------------------------------------------------------------------
    separator("Example 2: Creating string from a timestamp")
    timestamp = 1528797322
    date_time_obj = datetime.fromtimestamp(timestamp)

    print("Date time object:", date_time_obj)

    d2 = date_time_obj.strftime("%m/%d/%Y, %H:%M:%S")
    print("Output 2:", d2)

    d3 = date_time_obj.strftime("%d %b, %Y")
    print("Output 3:", d3)

    d4 = date_time_obj.strftime("%d %B, %Y")
    print("Output 4:", d4)

    d5 = date_time_obj.strftime("%I%p")
    print("Output 5:", d5)

    # -------------------------------------------------------------------------
    # Example 3: Locale's appropriate date and time
    # -------------------------------------------------------------------------
    separator("Example 3: Locale's appropriate date and time (%c, %x, %X)")
    d_c = date_time_obj.strftime("%c")
    print("Output 1 (%c - Locale date and time):", d_c)

    d_x = date_time_obj.strftime("%x")
    print("Output 2 (%x - Locale date)         :", d_x)

    d_X = date_time_obj.strftime("%X")
    print("Output 3 (%X - Locale time)         :", d_X)

    # -------------------------------------------------------------------------
    # Format Code List Demonstration
    # -------------------------------------------------------------------------
    separator("Daftar Kode Format (Format Code List) Lengkap")
    format_codes = [
        ("%a", "Nama hari disingkat"),
        ("%A", "Nama hari lengkap"),
        ("%w", "Hari dalam seminggu (0=Minggu, 6=Sabtu)"),
        ("%d", "Hari dalam bulan (01..31)"),
        ("%b", "Nama bulan disingkat"),
        ("%B", "Nama bulan lengkap"),
        ("%m", "Bulan dalam angka (01..12)"),
        ("%y", "Tahun 2 digit"),
        ("%Y", "Tahun 4 digit"),
        ("%H", "Jam 24-format (00..23)"),
        ("%I", "Jam 12-format (01..12)"),
        ("%p", "AM / PM"),
        ("%M", "Menit (00..59)"),
        ("%S", "Detik (00..59)"),
        ("%f", "Mikrodetik (000000..999999)"),
        ("%j", "Hari dalam setahun (001..366)"),
        ("%U", "Minggu dalam setahun (Minggu awal pekan)"),
        ("%W", "Minggu dalam setahun (Senin awal pekan)"),
        ("%c", "Representasi tanggal & waktu lokal"),
        ("%x", "Representasi tanggal lokal"),
        ("%X", "Representasi waktu lokal"),
        ("%%", "Karakter persen literal %"),
    ]

    for code, desc in format_codes:
        formatted = date_time_obj.strftime(code)
        print(f"Format {code:4} -> {formatted:30} | {desc}")

if __name__ == "__main__":
    main()

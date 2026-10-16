# ==============================================================================
# Tugas - Sesi #7: Python time.sleep()
# Mahasiswa : Abbi Maulanha Malik
# NIM       : 2595114007
# Kelas     : TI-A / 2025
# Matakuliah: Pemrograman Berorientasi Objek (PBO) - Python
# Dosen     : Edwin Hari Agus Prastyo, S.Kom., M.Kom.
# Sumber    : https://www.programiz.com/python-programming/time/sleep
# ==============================================================================

import time

def separator(title: str):
    print("\n" + "=" * 60)
    print(f" {title} ")
    print("=" * 60)

def main():
    # -------------------------------------------------------------------------
    # Example 1: Basic sleep() Method
    # -------------------------------------------------------------------------
    separator("Example 1: Basic sleep() Method")
    print("Mulai jeda 1 detik...")
    time.sleep(1)
    print("Wait until 1 second (Selesai jeda).")

    # -------------------------------------------------------------------------
    # Example 2: sleep() with float seconds
    # -------------------------------------------------------------------------
    separator("Example 2: sleep() with float seconds (2.4 seconds)")
    print("Printed immediately.")
    time.sleep(2.4)
    print("Printed after 2.4 seconds.")

    # -------------------------------------------------------------------------
    # Example 3: Create a Digital Clock in Python
    # -------------------------------------------------------------------------
    separator("Example 3: Create a Digital Clock in Python (5 Detik Demo)")
    print("Simulasi jam digital 12-jam (berjalan selama 5 tick agar run selesai):")

    tick_count = 0
    max_ticks = 5  # Dibatasi 5 iterasi untuk demonstrasi terminal & pembuatan laporan

    while tick_count < max_ticks:
        # get current local time as structured data
        current_time = time.localtime()
        # format the time in 12-hour clock with AM/PM
        formatted_time = time.strftime("%I:%M:%S %p", current_time)
        print(f"Tick {tick_count + 1}: {formatted_time}")
        time.sleep(1)
        tick_count += 1

    print("Simulasi Digital Clock selesai dengan aman.")

if __name__ == "__main__":
    main()

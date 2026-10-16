# ==============================================================================
# Tugas - Sesi #7: Python Current Time
# Mahasiswa : Abbi Maulanha Malik
# NIM       : 2595114007
# Kelas     : TI-A / 2025
# Matakuliah: Pemrograman Berorientasi Objek (PBO) - Python
# Dosen     : Edwin Hari Agus Prastyo, S.Kom., M.Kom.
# Sumber    : https://www.programiz.com/python-programming/datetime/current-time
# ==============================================================================

from datetime import datetime
import time
import pytz

def separator(title: str):
    print("\n" + "=" * 60)
    print(f" {title} ")
    print("=" * 60)

def main():
    # -------------------------------------------------------------------------
    # Example 1: Current time using the datetime object
    # -------------------------------------------------------------------------
    separator("Example 1: Current time using the datetime object")
    now = datetime.now()
    current_time_dt = now.strftime("%H:%M:%S")
    print("Current Time (via datetime) =", current_time_dt)

    # -------------------------------------------------------------------------
    # Example 2: Current time using time module
    # -------------------------------------------------------------------------
    separator("Example 2: Current time using time module")
    t = time.localtime()
    current_time_tm = time.strftime("%H:%M:%S", t)
    print("Current Time (via time module) =", current_time_tm)

    # -------------------------------------------------------------------------
    # Example 3: Current time of a Certain timezone
    # -------------------------------------------------------------------------
    separator("Example 3: Current time of Certain Timezones with pytz")
    # Get the timezone object for New York
    tz_NY = pytz.timezone('America/New_York')
    # Get the current time in New York
    datetime_NY = datetime.now(tz_NY)
    print("NY time    :", datetime_NY.strftime("%H:%M:%S"))

    # Get the timezone object for London
    tz_London = pytz.timezone('Europe/London')
    # Get the current time in London
    datetime_London = datetime.now(tz_London)
    print("London time:", datetime_London.strftime("%H:%M:%S"))

    # Local WIB time
    tz_Jakarta = pytz.timezone('Asia/Jakarta')
    datetime_Jakarta = datetime.now(tz_Jakarta)
    print("Jakarta (WIB) time:", datetime_Jakarta.strftime("%H:%M:%S"))

if __name__ == "__main__":
    main()

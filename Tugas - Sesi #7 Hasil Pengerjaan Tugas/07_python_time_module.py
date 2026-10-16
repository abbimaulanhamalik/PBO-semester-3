# ==============================================================================
# Tugas - Sesi #7: Python time Module
# Mahasiswa : Abbi Maulanha Malik
# NIM       : 2595114007
# Kelas     : TI-A / 2025
# Matakuliah: Pemrograman Berorientasi Objek (PBO) - Python
# Dosen     : Edwin Hari Agus Prastyo, S.Kom., M.Kom.
# Sumber    : https://www.programiz.com/python-programming/time
# ==============================================================================

import time

def separator(title: str):
    print("\n" + "=" * 60)
    print(f" {title} ")
    print("=" * 60)

def main():
    # -------------------------------------------------------------------------
    # 1. Python time.time() Function
    # -------------------------------------------------------------------------
    separator("1. Python time.time() Function")
    seconds = time.time()
    print("Seconds since epoch =", seconds)

    # -------------------------------------------------------------------------
    # 2. Python time.ctime() Function
    # -------------------------------------------------------------------------
    separator("2. Python time.ctime() Function")
    sample_seconds = 1672215379.5045543
    local_time = time.ctime(sample_seconds)
    print(f"Converted {sample_seconds} -> Local time: {local_time}")
    print("Current time.ctime() without arguments:", time.ctime())

    # -------------------------------------------------------------------------
    # 3. Python time.sleep() Function
    # -------------------------------------------------------------------------
    separator("3. Python time.sleep() Function")
    print("Printed immediately.")
    time.sleep(1.0)  # disesuaikan 1 detik agar demonstrasi responsif
    print("Printed after 1.0 second delay.")

    # -------------------------------------------------------------------------
    # 4. Python time.localtime() Function
    # -------------------------------------------------------------------------
    separator("4. Python time.localtime() Function")
    result_local = time.localtime(1672214933)
    print("result (from fixed epoch):", result_local)
    print("year   :", result_local.tm_year)
    print("tm_hour:", result_local.tm_hour)

    curr_local = time.localtime()
    print("Current localtime() struct_time:", curr_local)

    # -------------------------------------------------------------------------
    # 5. Python time.gmtime() Function (UTC)
    # -------------------------------------------------------------------------
    separator("5. Python time.gmtime() Function (UTC)")
    result_utc = time.gmtime(1672214933)
    print("result (UTC):", result_utc)
    print("year   :", result_utc.tm_year)
    print("tm_hour:", result_utc.tm_hour)

    # -------------------------------------------------------------------------
    # 6. Python time.mktime() Function
    # -------------------------------------------------------------------------
    separator("6. Python time.mktime() Function")
    # time_tuple: (year, month, day, hour, minute, second, weekday, day of the year, daylight saving)
    time_tuple = (2022, 12, 28, 8, 44, 4, 4, 362, 0)
    sec_from_tuple = time.mktime(time_tuple)
    print("time_tuple          :", time_tuple)
    print("time.mktime() output:", sec_from_tuple)

    # -------------------------------------------------------------------------
    # 7. Python time.asctime() Function
    # -------------------------------------------------------------------------
    separator("7. Python time.asctime() Function")
    t = (2022, 12, 28, 8, 44, 4, 4, 362, 0)
    result_asc = time.asctime(t)
    print("time.asctime(t) =", result_asc)
    print("time.asctime() with current localtime:", time.asctime(time.localtime()))

    # -------------------------------------------------------------------------
    # 8. Python time.strftime() Function
    # -------------------------------------------------------------------------
    separator("8. Python time.strftime() Function")
    named_tuple = time.localtime()
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    print("Formatted struct_time with time.strftime():", time_string)

    # -------------------------------------------------------------------------
    # 9. Python time.strptime() Function
    # -------------------------------------------------------------------------
    separator("9. Python time.strptime() Function")
    time_str_input = "14 July, 2023"
    result_strptime = time.strptime(time_str_input, "%d %B, %Y")
    print(f"time.strptime('{time_str_input}', '%d %B, %Y'):")
    print("result struct_time:", result_strptime)
    print("Parsed Year :", result_strptime.tm_year)
    print("Parsed Month:", result_strptime.tm_mon)
    print("Parsed Day  :", result_strptime.tm_mday)

if __name__ == "__main__":
    main()

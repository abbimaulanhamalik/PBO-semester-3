# ==============================================================================
# Tugas - Sesi #7: Python Timestamp to Datetime and Vice-Versa
# Mahasiswa : Abbi Maulanha Malik
# NIM       : 2595114007
# Kelas     : TI-A / 2025
# Matakuliah: Pemrograman Berorientasi Objek (PBO) - Python
# Dosen     : Edwin Hari Agus Prastyo, S.Kom., M.Kom.
# Sumber    : https://www.programiz.com/python-programming/datetime/timestamp-datetime
# ==============================================================================

from datetime import datetime

def separator(title: str):
    print("\n" + "=" * 60)
    print(f" {title} ")
    print("=" * 60)

def main():
    # -------------------------------------------------------------------------
    # Example 1: Python timestamp to datetime
    # -------------------------------------------------------------------------
    separator("Example 1: Python timestamp to datetime")
    # timestamp is number of seconds since 1970-01-01 (UNIX Epoch)
    timestamp = 1545730073

    # convert the timestamp to a datetime object in the local timezone
    dt_object = datetime.fromtimestamp(timestamp)

    # print the datetime object and its type
    print("dt_object      =", dt_object)
    print("type(dt_object)=", type(dt_object))

    # Optional formatted output using strftime()
    formatted = dt_object.strftime("%d %B, %Y %H:%M:%S")
    print("Formatted date =", formatted)

    # -------------------------------------------------------------------------
    # Example 2: Python datetime to timestamp
    # -------------------------------------------------------------------------
    separator("Example 2: Python datetime to timestamp")
    # current date and time
    now = datetime.now()
    print("Current datetime =", now)

    # convert from datetime to timestamp
    ts = datetime.timestamp(now)
    print("Timestamp        =", ts)

    # -------------------------------------------------------------------------
    # Example 3: Two-way Conversion Verification
    # -------------------------------------------------------------------------
    separator("Example 3: Two-way Conversion Verification")
    reconstructed_dt = datetime.fromtimestamp(ts)
    print("Reconstructed datetime from timestamp:", reconstructed_dt)
    print("Differences between now and reconstructed:", now - reconstructed_dt)

if __name__ == "__main__":
    main()

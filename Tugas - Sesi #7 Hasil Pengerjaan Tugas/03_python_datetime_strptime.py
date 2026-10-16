# ==============================================================================
# Tugas - Sesi #7: Python datetime.strptime()
# Mahasiswa : Abbi Maulanha Malik
# NIM       : 2595114007
# Kelas     : TI-A / 2025
# Matakuliah: Pemrograman Berorientasi Objek (PBO) - Python
# Dosen     : Edwin Hari Agus Prastyo, S.Kom., M.Kom.
# Sumber    : https://www.programiz.com/python-programming/datetime/strptime
# ==============================================================================

from datetime import datetime

def separator(title: str):
    print("\n" + "=" * 60)
    print(f" {title} ")
    print("=" * 60)

def main():
    # -------------------------------------------------------------------------
    # Example 1: string to datetime object using strptime()
    # -------------------------------------------------------------------------
    separator("Example 1: string to datetime object using strptime()")
    date_string = "21 June, 2018"
    print("date_string         =", date_string)
    print("type of date_string =", type(date_string))

    date_object = datetime.strptime(date_string, "%d %B, %Y")
    print("date_object         =", date_object)
    print("type of date_object =", type(date_object))

    # -------------------------------------------------------------------------
    # Example 2: string to datetime object with multiple formats
    # -------------------------------------------------------------------------
    separator("Example 2: string to datetime object (Format Ambiguity)")
    dt_string = "12/11/2018 09:15:32"
    print("Input string:", dt_string)

    # Considering date is in dd/mm/yyyy format
    dt_object1 = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
    print("dt_object1 (dd/mm/yyyy):", dt_object1)

    # Considering date is in mm/dd/yyyy format
    dt_object2 = datetime.strptime(dt_string, "%m/%d/%Y %H:%M:%S")
    print("dt_object2 (mm/dd/yyyy):", dt_object2)

    # -------------------------------------------------------------------------
    # Example 3: Handling ValueError in strptime()
    # -------------------------------------------------------------------------
    separator("Example 3: ValueError in strptime() & Error Handling")
    invalid_date_string = "12/11/2018"
    print("Input string :", invalid_date_string)
    print("Target format: %d %m %Y (spasi alih-alih garis miring)")

    try:
        date_object_err = datetime.strptime(invalid_date_string, "%d %m %Y")
        print("date_object =", date_object_err)
    except ValueError as e:
        print("Caught Expected Exception:")
        print(f"ValueError: {e}")

    # Correct parsing:
    print("\nPerbaikan parsing dengan format yang sesuai (%d/%m/%Y):")
    date_object_fixed = datetime.strptime(invalid_date_string, "%d/%m/%Y")
    print("date_object_fixed =", date_object_fixed)

if __name__ == "__main__":
    main()

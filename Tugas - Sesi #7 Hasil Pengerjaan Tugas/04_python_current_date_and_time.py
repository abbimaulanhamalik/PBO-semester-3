# ==============================================================================
# Tugas - Sesi #7: Python Current Date and Time
# Mahasiswa : Abbi Maulanha Malik
# NIM       : 2595114007
# Kelas     : TI-A / 2025
# Matakuliah: Pemrograman Berorientasi Objek (PBO) - Python
# Dosen     : Edwin Hari Agus Prastyo, S.Kom., M.Kom.
# Sumber    : https://www.programiz.com/python-programming/datetime/current-datetime
# ==============================================================================

from datetime import date, datetime

def separator(title: str):
    print("\n" + "=" * 60)
    print(f" {title} ")
    print("=" * 60)

def main():
    # -------------------------------------------------------------------------
    # Example 1: Python get today's date
    # -------------------------------------------------------------------------
    separator("Example 1: Python get today's date using date.today()")
    today = date.today()
    print("Today's date:", today)

    # -------------------------------------------------------------------------
    # Example 2: Current date in different formats
    # -------------------------------------------------------------------------
    separator("Example 2: Current date in different formats")
    # dd/mm/YY
    d1 = today.strftime("%d/%m/%Y")
    print("d1 (dd/mm/YYYY)           =", d1)

    # Textual month, day and year
    d2 = today.strftime("%B %d, %Y")
    print("d2 (MonthName DD, YYYY)   =", d2)

    # mm/dd/y
    d3 = today.strftime("%m/%d/%y")
    print("d3 (mm/dd/yy)             =", d3)

    # Month abbreviation, day and year
    d4 = today.strftime("%b-%d-%Y")
    print("d4 (MonAbbr-DD-YYYY)      =", d4)

    # -------------------------------------------------------------------------
    # Example 3: Get the current date and time in Python
    # -------------------------------------------------------------------------
    separator("Example 3: Get current date and time using datetime.now()")
    # datetime object containing current date and time
    now = datetime.now()
    print("now =", now)

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)

if __name__ == "__main__":
    main()

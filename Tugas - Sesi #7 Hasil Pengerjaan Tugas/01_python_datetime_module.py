# ==============================================================================
# Tugas - Sesi #7: Python datetime Module
# Mahasiswa : Abbi Maulanha Malik
# NIM       : 2595114007
# Kelas     : TI-A / 2025
# Matakuliah: Pemrograman Berorientasi Objek (PBO) - Python
# Dosen     : Edwin Hari Agus Prastyo, S.Kom., M.Kom.
# Sumber    : https://www.programiz.com/python-programming/datetime
# ==============================================================================

import datetime
from datetime import date, time, datetime as dt, timedelta
import pytz

def separator(title: str):
    print("\n" + "=" * 60)
    print(f" {title} ")
    print("=" * 60)

def main():
    # -------------------------------------------------------------------------
    # Example 1: Get Current Date and Time
    # -------------------------------------------------------------------------
    separator("Example 1: Get Current Date and Time")
    now = datetime.datetime.now()
    print("datetime.datetime.now():", now)

    # -------------------------------------------------------------------------
    # Example 2: Get Current Date
    # -------------------------------------------------------------------------
    separator("Example 2: Get Current Date")
    current_date = datetime.date.today()
    print("datetime.date.today()  :", current_date)

    # -------------------------------------------------------------------------
    # Attributes of datetime Module
    # -------------------------------------------------------------------------
    separator("Attributes of datetime Module: dir(datetime)")
    print(dir(datetime))

    # -------------------------------------------------------------------------
    # Example 3: Date object to represent a date
    # -------------------------------------------------------------------------
    separator("Example 3: Date object to represent a date")
    d = datetime.date(2022, 12, 25)
    print("d = datetime.date(2022, 12, 25):", d)

    # -------------------------------------------------------------------------
    # Import Only date Class
    # -------------------------------------------------------------------------
    separator("Import Only date Class")
    d_only = date(2022, 12, 25)
    print("date(2022, 12, 25):", d_only)

    # -------------------------------------------------------------------------
    # Example 4: Get current date using today()
    # -------------------------------------------------------------------------
    separator("Example 4: Get the current date using today()")
    todays_date = date.today()
    print("Today's date =", todays_date)

    # -------------------------------------------------------------------------
    # Example 5: Get the date from a timestamp
    # -------------------------------------------------------------------------
    separator("Example 5: Get the date from a timestamp")
    timestamp_date = date.fromtimestamp(1326244364)
    print("Date from timestamp (1326244364) =", timestamp_date)

    # -------------------------------------------------------------------------
    # Example 6: Print today's year, month, and day
    # -------------------------------------------------------------------------
    separator("Example 6: Print today's year, month, and day")
    today = date.today()
    print("Current year :", today.year)
    print("Current month:", today.month)
    print("Current day  :", today.day)

    # -------------------------------------------------------------------------
    # Python datetime.time Class
    # Example 7: Time object to represent time
    # -------------------------------------------------------------------------
    separator("Example 7: Python datetime.time Class")
    # time(hour = 0, minute = 0, second = 0)
    a = time()
    print("a =", a)

    # time(hour, minute and second)
    b = time(11, 34, 56)
    print("b =", b)

    # time(hour, minute and second)
    c = time(hour=11, minute=34, second=56)
    print("c =", c)

    # time(hour, minute, second, microsecond)
    d_time = time(11, 34, 56, 234566)
    print("d =", d_time)

    # -------------------------------------------------------------------------
    # Example 8: Print hour, minute, second and microsecond
    # -------------------------------------------------------------------------
    separator("Example 8: Print hour, minute, second and microsecond")
    time_val = time(11, 34, 56)
    print("Hour        =", time_val.hour)
    print("Minute      =", time_val.minute)
    print("Second      =", time_val.second)
    print("Microsecond =", time_val.microsecond)

    # -------------------------------------------------------------------------
    # The datetime.datetime Class
    # Example 9: Python datetime object
    # -------------------------------------------------------------------------
    separator("Example 9: Python datetime object")
    dt1 = dt(2022, 12, 28)
    print("datetime(2022, 12, 28):", dt1)

    dt2 = dt(2022, 12, 28, 23, 55, 59, 342380)
    print("datetime(2022, 12, 28, 23, 55, 59, 342380):", dt2)

    # -------------------------------------------------------------------------
    # Example 10: Print year, month, hour, minute and timestamp
    # -------------------------------------------------------------------------
    separator("Example 10: Print year, month, hour, minute and timestamp")
    sample_dt = dt(2022, 12, 28, 23, 55, 59, 342380)
    print("Year      =", sample_dt.year)
    print("Month     =", sample_dt.month)
    print("Day       =", sample_dt.day)
    print("Hour      =", sample_dt.hour)
    print("Minute    =", sample_dt.minute)
    print("Timestamp =", sample_dt.timestamp())

    # -------------------------------------------------------------------------
    # Python datetime.timedelta Class
    # Example 11: Difference between two dates and times
    # -------------------------------------------------------------------------
    separator("Example 11: Difference between two dates and times (timedelta)")
    # using date()
    t1 = date(year=2018, month=7, day=12)
    t2 = date(year=2017, month=12, day=23)
    t3 = t1 - t2
    print("t3 (t1 - t2) =", t3)

    # using datetime()
    t4 = dt(year=2018, month=7, day=12, hour=7, minute=9, second=33)
    t5 = dt(year=2019, month=6, day=10, hour=5, minute=55, second=13)
    t6 = t4 - t5
    print("t6 (t4 - t5) =", t6)
    print("Type of t3   =", type(t3))
    print("Type of t6   =", type(t6))

    # -------------------------------------------------------------------------
    # Example 12: Difference between two timedelta objects
    # -------------------------------------------------------------------------
    separator("Example 12: Difference between two timedelta objects")
    td1 = timedelta(weeks=2, days=5, hours=1, seconds=33)
    td2 = timedelta(days=4, hours=11, minutes=4, seconds=54)
    td3 = td1 - td2
    print("td1 - td2 =", td3)

    # -------------------------------------------------------------------------
    # Example 13: Negative timedelta object
    # -------------------------------------------------------------------------
    separator("Example 13: Negative timedelta object")
    td_neg1 = timedelta(seconds=33)
    td_neg2 = timedelta(seconds=54)
    td_neg3 = td_neg1 - td_neg2
    print("td_neg3 =", td_neg3)
    print("abs(td_neg3) =", abs(td_neg3))

    # -------------------------------------------------------------------------
    # Example 14: Time duration in seconds
    # -------------------------------------------------------------------------
    separator("Example 14: Time duration in seconds (total_seconds())")
    t_sec = timedelta(days=5, hours=1, seconds=33, microseconds=233423)
    print("Total seconds =", t_sec.total_seconds())

    # -------------------------------------------------------------------------
    # Example 15: Python format datetime (strftime)
    # -------------------------------------------------------------------------
    separator("Example 15: Python format datetime (strftime)")
    now_curr = dt.now()
    t_str = now_curr.strftime("%H:%M:%S")
    print("Time:", t_str)
    s1 = now_curr.strftime("%m/%d/%Y, %H:%M:%S")  # mm/dd/YY H:M:S format
    print("s1:", s1)
    s2 = now_curr.strftime("%d/%m/%Y, %H:%M:%S")  # dd/mm/YY H:M:S format
    print("s2:", s2)

    # -------------------------------------------------------------------------
    # Example 16: Python strptime() Method
    # -------------------------------------------------------------------------
    separator("Example 16: Python strptime() Method")
    date_string = "25 December, 2022"
    print("date_string =", date_string)
    date_object = dt.strptime(date_string, "%d %B, %Y")
    print("date_object =", date_object)

    # -------------------------------------------------------------------------
    # Example 17: Handling timezone in Python (pytz)
    # -------------------------------------------------------------------------
    separator("Example 17: Handling timezone in Python with pytz")
    local = dt.now()
    print("Local :", local.strftime("%m/%d/%Y, %H:%M:%S"))

    tz_NY = pytz.timezone('America/New_York')
    datetime_NY = dt.now(tz_NY)
    print("NY    :", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

    tz_London = pytz.timezone('Europe/London')
    datetime_London = dt.now(tz_London)
    print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))

if __name__ == "__main__":
    main()

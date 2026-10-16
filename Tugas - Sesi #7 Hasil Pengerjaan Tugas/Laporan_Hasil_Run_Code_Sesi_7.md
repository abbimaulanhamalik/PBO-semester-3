# 📄 LAPORAN HASIL RUN CODE — PRAKTIKUM SESI #7
## Pemrograman Berorientasi Objek (PBO) — Modul `datetime` & `time` Python

---

### 👨‍🎓 Identitas Mahasiswa

| Informasi | Keterangan |
| :--- | :--- |
| **Nama Lengkap** | **Abbi Maulanha Malik** |
| **NIM** | **2595114007** |
| **Kelas / Angkatan** | **TI-A / 2025** |
| **Program Studi** | S1 Teknik Informatika |
| **Fakultas** | Fakultas Teknologi Informasi (FTI) |
| **Perguruan Tinggi** | Universitas Hasyim Asy'ari (UNHASY) Tebuireng Jombang |
| **Dosen Pengampu** | **Edwin Hari Agus Prastyo, S.Kom., M.Kom.** |
| **Waktu Eksekusi** | 2026-10-16 14:40:13 |
| **Link Repositori Git** | [GitHub: abbimaulanhamalik/PBO-semester-3](https://github.com/abbimaulanhamalik/PBO-semester-3) |

---

## 📌 Ringkasan Materi & URL Sumber (Programiz)

Seluruh kode sumber pada tugas ini diimplementasikan secara komprehensif dari 8 modul resmi Programiz:

| No | Topik Modul | Berkas Program | URL Sumber Programiz | Status Run |
|:--:|:---|:---|:---|:---:|
| 01 | **Python datetime Module** | [`01_python_datetime_module.py`](01_python_datetime_module.py) | [https://www.programiz.com/python-programming/datetime](https://www.programiz.com/python-programming/datetime) | ✅ Sukses |
| 02 | **Python datetime.strftime()** | [`02_python_datetime_strftime.py`](02_python_datetime_strftime.py) | [https://www.programiz.com/python-programming/datetime/strftime](https://www.programiz.com/python-programming/datetime/strftime) | ✅ Sukses |
| 03 | **Python datetime.strptime()** | [`03_python_datetime_strptime.py`](03_python_datetime_strptime.py) | [https://www.programiz.com/python-programming/datetime/strptime](https://www.programiz.com/python-programming/datetime/strptime) | ✅ Sukses |
| 04 | **Python Current Date and Time** | [`04_python_current_date_and_time.py`](04_python_current_date_and_time.py) | [https://www.programiz.com/python-programming/datetime/current-datetime](https://www.programiz.com/python-programming/datetime/current-datetime) | ✅ Sukses |
| 05 | **Python Current Time** | [`05_python_current_time.py`](05_python_current_time.py) | [https://www.programiz.com/python-programming/datetime/current-time](https://www.programiz.com/python-programming/datetime/current-time) | ✅ Sukses |
| 06 | **Python Timestamp to Datetime and Vice-Versa** | [`06_python_timestamp_to_datetime.py`](06_python_timestamp_to_datetime.py) | [https://www.programiz.com/python-programming/datetime/timestamp-datetime](https://www.programiz.com/python-programming/datetime/timestamp-datetime) | ✅ Sukses |
| 07 | **Python time Module** | [`07_python_time_module.py`](07_python_time_module.py) | [https://www.programiz.com/python-programming/time](https://www.programiz.com/python-programming/time) | ✅ Sukses |
| 08 | **Python time.sleep()** | [`08_python_time_sleep.py`](08_python_time_sleep.py) | [https://www.programiz.com/python-programming/time/sleep](https://www.programiz.com/python-programming/time/sleep) | ✅ Sukses |

---

## 🖥️ Detail Laporan Hasil Run Code Tiap Modul

### 1. Python datetime Module
- **Berkas Kode**: [`01_python_datetime_module.py`](01_python_datetime_module.py)
- **Sumber Tutorial**: [https://www.programiz.com/python-programming/datetime](https://www.programiz.com/python-programming/datetime)
- **Exit Code**: `0`

```text
============================================================
 Example 1: Get Current Date and Time 
============================================================
datetime.datetime.now(): 2026-10-16 14:40:03.691598

============================================================
 Example 2: Get Current Date 
============================================================
datetime.date.today()  : 2026-10-16

============================================================
 Attributes of datetime Module: dir(datetime) 
============================================================
['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']

============================================================
 Example 3: Date object to represent a date 
============================================================
d = datetime.date(2022, 12, 25): 2022-12-25

============================================================
 Import Only date Class 
============================================================
date(2022, 12, 25): 2022-12-25

============================================================
 Example 4: Get the current date using today() 
============================================================
Today's date = 2026-10-16

============================================================
 Example 5: Get the date from a timestamp 
============================================================
Date from timestamp (1326244364) = 2012-01-11

============================================================
 Example 6: Print today's year, month, and day 
============================================================
Current year : 2026
Current month: 10
Current day  : 16

============================================================
 Example 7: Python datetime.time Class 
============================================================
a = 00:00:00
b = 11:34:56
c = 11:34:56
d = 11:34:56.234566

============================================================
 Example 8: Print hour, minute, second and microsecond 
============================================================
Hour        = 11
Minute      = 34
Second      = 56
Microsecond = 0

============================================================
 Example 9: Python datetime object 
============================================================
datetime(2022, 12, 28): 2022-12-28 00:00:00
datetime(2022, 12, 28, 23, 55, 59, 342380): 2022-12-28 23:55:59.342380

============================================================
 Example 10: Print year, month, hour, minute and timestamp 
============================================================
Year      = 2022
Month     = 12
Day       = 28
Hour      = 23
Minute    = 55
Timestamp = 1672246559.34238

============================================================
 Example 11: Difference between two dates and times (timedelta) 
============================================================
t3 (t1 - t2) = 201 days, 0:00:00
t6 (t4 - t5) = -333 days, 1:14:20
Type of t3   = <class 'datetime.timedelta'>
Type of t6   = <class 'datetime.timedelta'>

============================================================
 Example 12: Difference between two timedelta objects 
============================================================
td1 - td2 = 14 days, 13:55:39

============================================================
 Example 13: Negative timedelta object 
============================================================
td_neg3 = -1 day, 23:59:39
abs(td_neg3) = 0:00:21

============================================================
 Example 14: Time duration in seconds (total_seconds()) 
============================================================
Total seconds = 435633.233423

============================================================
 Example 15: Python format datetime (strftime) 
============================================================
Time: 14:40:03
s1: 10/16/2026, 14:40:03
s2: 16/10/2026, 14:40:03

============================================================
 Example 16: Python strptime() Method 
============================================================
date_string = 25 December, 2022
date_object = 2022-12-25 00:00:00

============================================================
 Example 17: Handling timezone in Python with pytz 
============================================================
Local : 10/16/2026, 14:40:03
NY    : 10/16/2026, 03:40:03
London: 10/16/2026, 08:40:03
```

---

### 2. Python datetime.strftime()
- **Berkas Kode**: [`02_python_datetime_strftime.py`](02_python_datetime_strftime.py)
- **Sumber Tutorial**: [https://www.programiz.com/python-programming/datetime/strftime](https://www.programiz.com/python-programming/datetime/strftime)
- **Exit Code**: `0`

```text
============================================================
 Example 1: datetime to string using strftime() 
============================================================
year: 2026
month: 10
day: 16
time: 14:40:03
date and time: 10/16/2026, 14:40:03

============================================================
 Example 2: Creating string from a timestamp 
============================================================
Date time object: 2018-06-12 16:55:22
Output 2: 06/12/2018, 16:55:22
Output 3: 12 Jun, 2018
Output 4: 12 June, 2018
Output 5: 04PM

============================================================
 Example 3: Locale's appropriate date and time (%c, %x, %X) 
============================================================
Output 1 (%c - Locale date and time): Tue Jun 12 16:55:22 2018
Output 2 (%x - Locale date)         : 06/12/18
Output 3 (%X - Locale time)         : 16:55:22

============================================================
 Daftar Kode Format (Format Code List) Lengkap 
============================================================
Format %a   -> Tue                            | Nama hari disingkat
Format %A   -> Tuesday                        | Nama hari lengkap
Format %w   -> 2                              | Hari dalam seminggu (0=Minggu, 6=Sabtu)
Format %d   -> 12                             | Hari dalam bulan (01..31)
Format %b   -> Jun                            | Nama bulan disingkat
Format %B   -> June                           | Nama bulan lengkap
Format %m   -> 06                             | Bulan dalam angka (01..12)
Format %y   -> 18                             | Tahun 2 digit
Format %Y   -> 2018                           | Tahun 4 digit
Format %H   -> 16                             | Jam 24-format (00..23)
Format %I   -> 04                             | Jam 12-format (01..12)
Format %p   -> PM                             | AM / PM
Format %M   -> 55                             | Menit (00..59)
Format %S   -> 22                             | Detik (00..59)
Format %f   -> 000000                         | Mikrodetik (000000..999999)
Format %j   -> 163                            | Hari dalam setahun (001..366)
Format %U   -> 23                             | Minggu dalam setahun (Minggu awal pekan)
Format %W   -> 24                             | Minggu dalam setahun (Senin awal pekan)
Format %c   -> Tue Jun 12 16:55:22 2018       | Representasi tanggal & waktu lokal
Format %x   -> 06/12/18                       | Representasi tanggal lokal
Format %X   -> 16:55:22                       | Representasi waktu lokal
Format %%   -> %                              | Karakter persen literal %
```

---

### 3. Python datetime.strptime()
- **Berkas Kode**: [`03_python_datetime_strptime.py`](03_python_datetime_strptime.py)
- **Sumber Tutorial**: [https://www.programiz.com/python-programming/datetime/strptime](https://www.programiz.com/python-programming/datetime/strptime)
- **Exit Code**: `0`

```text
============================================================
 Example 1: string to datetime object using strptime() 
============================================================
date_string         = 21 June, 2018
type of date_string = <class 'str'>
date_object         = 2018-06-21 00:00:00
type of date_object = <class 'datetime.datetime'>

============================================================
 Example 2: string to datetime object (Format Ambiguity) 
============================================================
Input string: 12/11/2018 09:15:32
dt_object1 (dd/mm/yyyy): 2018-11-12 09:15:32
dt_object2 (mm/dd/yyyy): 2018-12-11 09:15:32

============================================================
 Example 3: ValueError in strptime() & Error Handling 
============================================================
Input string : 12/11/2018
Target format: %d %m %Y (spasi alih-alih garis miring)
Caught Expected Exception:
ValueError: time data '12/11/2018' does not match format '%d %m %Y'

Perbaikan parsing dengan format yang sesuai (%d/%m/%Y):
date_object_fixed = 2018-11-12 00:00:00
```

---

### 4. Python Current Date and Time
- **Berkas Kode**: [`04_python_current_date_and_time.py`](04_python_current_date_and_time.py)
- **Sumber Tutorial**: [https://www.programiz.com/python-programming/datetime/current-datetime](https://www.programiz.com/python-programming/datetime/current-datetime)
- **Exit Code**: `0`

```text
============================================================
 Example 1: Python get today's date using date.today() 
============================================================
Today's date: 2026-10-16

============================================================
 Example 2: Current date in different formats 
============================================================
d1 (dd/mm/YYYY)           = 16/10/2026
d2 (MonthName DD, YYYY)   = October 16, 2026
d3 (mm/dd/yy)             = 10/16/26
d4 (MonAbbr-DD-YYYY)      = Oct-16-2026

============================================================
 Example 3: Get current date and time using datetime.now() 
============================================================
now = 2026-10-16 14:40:03.987156
date and time = 16/10/2026 14:40:03
```

---

### 5. Python Current Time
- **Berkas Kode**: [`05_python_current_time.py`](05_python_current_time.py)
- **Sumber Tutorial**: [https://www.programiz.com/python-programming/datetime/current-time](https://www.programiz.com/python-programming/datetime/current-time)
- **Exit Code**: `0`

```text
============================================================
 Example 1: Current time using the datetime object 
============================================================
Current Time (via datetime) = 14:40:04

============================================================
 Example 2: Current time using time module 
============================================================
Current Time (via time module) = 14:40:04

============================================================
 Example 3: Current time of Certain Timezones with pytz 
============================================================
NY time    : 03:40:04
London time: 08:40:04
Jakarta (WIB) time: 14:40:04
```

---

### 6. Python Timestamp to Datetime and Vice-Versa
- **Berkas Kode**: [`06_python_timestamp_to_datetime.py`](06_python_timestamp_to_datetime.py)
- **Sumber Tutorial**: [https://www.programiz.com/python-programming/datetime/timestamp-datetime](https://www.programiz.com/python-programming/datetime/timestamp-datetime)
- **Exit Code**: `0`

```text
============================================================
 Example 1: Python timestamp to datetime 
============================================================
dt_object      = 2018-12-25 16:27:53
type(dt_object)= <class 'datetime.datetime'>
Formatted date = 25 December, 2018 16:27:53

============================================================
 Example 2: Python datetime to timestamp 
============================================================
Current datetime = 2026-10-16 14:40:04.152760
Timestamp        = 1792136404.15276

============================================================
 Example 3: Two-way Conversion Verification 
============================================================
Reconstructed datetime from timestamp: 2026-10-16 14:40:04.152760
Differences between now and reconstructed: 0:00:00
```

---

### 7. Python time Module
- **Berkas Kode**: [`07_python_time_module.py`](07_python_time_module.py)
- **Sumber Tutorial**: [https://www.programiz.com/python-programming/time](https://www.programiz.com/python-programming/time)
- **Exit Code**: `0`

```text
============================================================
 1. Python time.time() Function 
============================================================
Seconds since epoch = 1792136404.206948

============================================================
 2. Python time.ctime() Function 
============================================================
Converted 1672215379.5045543 -> Local time: Wed Dec 28 15:16:19 2022
Current time.ctime() without arguments: Fri Oct 16 14:40:04 2026

============================================================
 3. Python time.sleep() Function 
============================================================
Printed immediately.
Printed after 1.0 second delay.

============================================================
 4. Python time.localtime() Function 
============================================================
result (from fixed epoch): time.struct_time(tm_year=2022, tm_mon=12, tm_mday=28, tm_hour=15, tm_min=8, tm_sec=53, tm_wday=2, tm_yday=362, tm_isdst=0)
year   : 2022
tm_hour: 15
Current localtime() struct_time: time.struct_time(tm_year=2026, tm_mon=10, tm_mday=16, tm_hour=14, tm_min=40, tm_sec=5, tm_wday=4, tm_yday=289, tm_isdst=0)

============================================================
 5. Python time.gmtime() Function (UTC) 
============================================================
result (UTC): time.struct_time(tm_year=2022, tm_mon=12, tm_mday=28, tm_hour=8, tm_min=8, tm_sec=53, tm_wday=2, tm_yday=362, tm_isdst=0)
year   : 2022
tm_hour: 8

============================================================
 6. Python time.mktime() Function 
============================================================
time_tuple          : (2022, 12, 28, 8, 44, 4, 4, 362, 0)
time.mktime() output: 1672191844.0

============================================================
 7. Python time.asctime() Function 
============================================================
time.asctime(t) = Fri Dec 28 08:44:04 2022
time.asctime() with current localtime: Fri Oct 16 14:40:05 2026

============================================================
 8. Python time.strftime() Function 
============================================================
Formatted struct_time with time.strftime(): 10/16/2026, 14:40:05

============================================================
 9. Python time.strptime() Function 
============================================================
time.strptime('14 July, 2023', '%d %B, %Y'):
result struct_time: time.struct_time(tm_year=2023, tm_mon=7, tm_mday=14, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=195, tm_isdst=-1)
Parsed Year : 2023
Parsed Month: 7
Parsed Day  : 14
```

---

### 8. Python time.sleep()
- **Berkas Kode**: [`08_python_time_sleep.py`](08_python_time_sleep.py)
- **Sumber Tutorial**: [https://www.programiz.com/python-programming/time/sleep](https://www.programiz.com/python-programming/time/sleep)
- **Exit Code**: `0`

```text
============================================================
 Example 1: Basic sleep() Method 
============================================================
Mulai jeda 1 detik...
Wait until 1 second (Selesai jeda).

============================================================
 Example 2: sleep() with float seconds (2.4 seconds) 
============================================================
Printed immediately.
Printed after 2.4 seconds.

============================================================
 Example 3: Create a Digital Clock in Python (5 Detik Demo) 
============================================================
Simulasi jam digital 12-jam (berjalan selama 5 tick agar run selesai):
Tick 1: 02:40:08 PM
Tick 2: 02:40:09 PM
Tick 3: 02:40:10 PM
Tick 4: 02:40:11 PM
Tick 5: 02:40:12 PM
Simulasi Digital Clock selesai dengan aman.
```

---

<div align="center">
  <sub>Laporan ini digenerate secara otomatis dari output eksekusi Python asli pada sistem.</sub><br>
  <sub><b>Teknik Informatika — Universitas Hasyim Asy'ari Tebuireng Jombang</b></sub>
</div>
"""
Studi Kasus 3: Sistem Keamanan Akun & Audit Log Login
Implementasi sistem verifikasi kredensial dan logging keamanan:
- Validasi format ketat dengan Regular Expressions (re module)
- Enkapsulasi OOP elegan dengan @property & setter pada class User
- Pencatatan Audit Trail otomatis menggunakan Python Decorator & Closure
"""

import re
from datetime import datetime
from functools import wraps

# Global repository untuk menyimpan riwayat audit trail
audit_logs = []


def audit_trail(func):
    """
    Decorator / Closure untuk mencatat setiap usaha autentikasi ke dalam audit trail
    secara transparan tanpa mengubah logika inti dari fungsi login.
    Mencatat: Timestamp, Username, Status (BERHASIL/DITOLAK), dan Alasan.
    """
    @wraps(func)
    def wrapper(username, password, *args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        berhasil, pesan = func(username, password, *args, **kwargs)
        status = "BERHASIL" if berhasil else "DITOLAK"

        # Simpan ke audit trail log
        log_entry = {
            "timestamp": timestamp,
            "username": username,
            "status": status,
            "alasan": pesan,
        }
        audit_logs.append(log_entry)

        # Output feedback seketika
        indikator = "[OK]" if berhasil else "[X ]"
        print(f" {indikator} [{timestamp}] Percobaan Login '{username}' -> {status}")
        print(f"      Detail: {pesan}")

        return berhasil, pesan

    return wrapper


class User:
    """
    Model Pengguna OOP yang memanfaatkan @property untuk enkapsulasi atribut kredensial.
    Validasi format dilakukan melalui ekspresi reguler (RegEx).
    """
    # Aturan RegEx:
    # 1. Username: minimal 5 karakter, hanya alfanumerik (huruf & angka), tanpa spasi/simbol
    REGEX_USERNAME = re.compile(r"^[a-zA-Z0-9]{5,}$")

    # 2. Password: minimal 8 karakter dan wajib memiliki setidaknya satu angka
    REGEX_PASSWORD = re.compile(r"^(?=.*\d).{8,}$")

    def __init__(self, username, password):
        self._username = None
        self._password = None
        # Menggunakan setter berproperti untuk validasi otomatis saat inisialisasi
        self.username = username
        self.password = password

    @property
    def username(self):
        """Getter untuk username terenkapsulasi."""
        return self._username

    @username.setter
    def username(self, value):
        """Setter dengan validasi format username berbasis RegEx."""
        if not self.validasi_format_username(value):
            raise ValueError(
                "Username tidak valid: minimal 5 karakter, hanya huruf & angka tanpa spasi/simbol."
            )
        self._username = value

    @property
    def password(self):
        """Getter terenkapsulasi: menyembunyikan raw password dari akses luar."""
        return "********"

    @property
    def raw_password(self):
        """Properti internal untuk verifikasi kecocokan kredensial."""
        return self._password

    @password.setter
    def password(self, value):
        """Setter dengan validasi format password berbasis RegEx."""
        if not self.validasi_format_password(value):
            raise ValueError(
                "Password tidak valid: minimal 8 karakter dan wajib memuat minimal 1 karakter angka."
            )
        self._password = value

    @classmethod
    def validasi_format_username(cls, username):
        """Metode utilitas untuk validasi format username via RegEx."""
        return bool(cls.REGEX_USERNAME.match(str(username)))

    @classmethod
    def validasi_format_password(cls, password):
        """Metode utilitas untuk validasi format password via RegEx."""
        return bool(cls.REGEX_PASSWORD.match(str(password)))


# Database simulasi pengguna terdaftar
DATABASE_USERS = {}


def daftarkan_user(username, password):
    """Mendaftarkan akun baru yang valid ke dalam sistem."""
    try:
        user_baru = User(username, password)
        DATABASE_USERS[username] = user_baru
        return True, "Akun berhasil didaftarkan."
    except ValueError as e:
        return False, str(e)


@audit_trail
def proses_login(username, password):
    """
    Fungsi otentikasi login inti yang dibungkus oleh decorator @audit_trail.
    Menguji format RegEx terlebih dahulu sebelum memvalidasi kecocokan akun.
    """
    # 1. Validasi Format Username dengan RegEx
    if not User.validasi_format_username(username):
        return (
            False,
            "Format username tidak sesuai (minimal 5 karakter, alfanumerik, tanpa spasi/simbol).",
        )

    # 2. Validasi Format Password dengan RegEx
    if not User.validasi_format_password(password):
        return (
            False,
            "Format password tidak sesuai (minimal 8 karakter & wajib memuat minimal 1 angka).",
        )

    # 3. Validasi Keberadaan Akun
    if username not in DATABASE_USERS:
        return False, "Pengguna tidak terdaftar dalam database."

    # 4. Verifikasi Password
    user = DATABASE_USERS[username]
    if user.raw_password != password:
        return False, "Kredensial sandi tidak cocok."

    return True, "Otentikasi sukses. Akses sistem diberikan."


def cetak_audit_log_table():
    """Mencetak tabel rekap riwayat audit trail di terminal."""
    print("\n" + "=" * 92)
    print(" REKAPITULASI AUDIT TRAIL LOG SISTEM KEAMANAN ".center(92, "="))
    print("=" * 92)
    print(f"{'No':<3} | {'Waktu (Timestamp)':<19} | {'Username':<12} | {'Status':<9} | {'Alasan / Keterangan'}")
    print("-" * 92)
    for idx, log in enumerate(audit_logs, start=1):
        status_tag = f"[{log['status']}]"
        print(
            f"{idx:<3} | {log['timestamp']:<19} | {log['username']:<12} | {status_tag:<9} | {log['alasan']}"
        )
    print("=" * 92)


def main():
    print("=" * 70)
    print(" SISTEM KEAMANAN OTENTIKASI & AUDIT TRAIL LOGIN ".center(70, "#"))
    print("=" * 70)

    # Inisialisasi Akun Resmi
    daftarkan_user("admin2026", "AdminPass999")
    daftarkan_user("aisyah99", "AisyahAman123")
    print(" [SETUP] Pengguna resmi terdaftar:")
    print("         - 'admin2026' (Password: AdminPass999)")
    print("         - 'aisyah99'  (Password: AisyahAman123)")
    print("=" * 70)

    print("\n--- SKENARIO PENGUJIAN OTENTIKASI ---")

    # Skenario 1: Username terlalu pendek (< 5 karakter)
    print("\n[Pengujian 1]: Username kurang dari 5 karakter")
    proses_login("budi", "Rahasia1234")

    # Skenario 2: Username mengandung spasi atau karakter ilegal
    print("\n[Pengujian 2]: Username mengandung simbol ilegal ('@' dan spasi)")
    proses_login("user@super", "Rahasia1234")

    # Skenario 3: Password terlalu pendek (< 8 karakter)
    print("\n[Pengujian 3]: Password terlalu pendek (< 8 karakter)")
    proses_login("budi123", "Pass1")

    # Skenario 4: Password tidak memiliki karakter angka
    print("\n[Pengujian 4]: Password panjang namun tanpa angka")
    proses_login("budi123", "passwordtanpaangka")

    # Skenario 5: Format valid, tetapi pengguna belum terdaftar
    print("\n[Pengujian 5]: Format valid tapi user tidak terdaftar")
    proses_login("budi123", "PasswordValid99")

    # Skenario 6: Format valid, akun terdaftar, namun password salah
    print("\n[Pengujian 6]: User terdaftar tetapi salah memasukkan password")
    proses_login("aisyah99", "PasswordSalah123")

    # Skenario 7: Login Sukses - Seluruh kriteria terpenuhi
    print("\n[Pengujian 7]: Login Sukses (Kredensial valid dan benar)")
    proses_login("admin2026", "AdminPass999")

    # Skenario 8: Login Sukses Pengguna Kedua
    print("\n[Pengujian 8]: Login Sukses Akun Kedua")
    proses_login("aisyah99", "AisyahAman123")

    # Tampilkan Ringkasan Tabel Audit Trail
    cetak_audit_log_table()


if __name__ == "__main__":
    main()

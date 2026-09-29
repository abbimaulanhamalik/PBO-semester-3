# ==========================================
# KASUS 02: INHERITANCE (PEWARISAN SIFAT)
# Sistem Rental Kendaraan
# Pemrograman Berorientasi Objek - Python
# Mahasiswa: Abbi Maulanha Malik (NIM: 2595114007)
# ==========================================

class Kendaraan:
    def __init__(self, nama, merk, tahun, kecepatan):
        self.nama = nama
        self.merk = merk
        self.tahun = tahun
        self.kecepatan = kecepatan

    def info_dasar(self):
        return f"{self.nama} ({self.merk}, {self.tahun}) - Maks: {self.kecepatan} km/jam"

class Mobil(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, jumlah_kursi):
        super().__init__(nama, merk, tahun, kecepatan)
        self.jumlah_kursi = jumlah_kursi

    def cek_spesifikasi(self):
        print(f"[MOBIL RENTAL]")
        print(f"Armada       : {self.info_dasar()}")
        print(f"Kapasitas    : {self.jumlah_kursi} Kursi Penumpang")
        print("-" * 40)

class Motor(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, tipe_motor):
        super().__init__(nama, merk, tahun, kecepatan)
        self.tipe_motor = tipe_motor

    def cek_spesifikasi(self):
        print(f"[MOTOR RENTAL]")
        print(f"Armada       : {self.info_dasar()}")
        print(f"Tipe Motor   : {self.tipe_motor}")
        print("-" * 40)

# Instansiasi Objek
mobil1 = Mobil("Avanza Veloz", "Toyota", 2022, 160, 7)
mobil2 = Mobil("Innova Zenix", "Toyota", 2023, 180, 7)
motor1 = Motor("Vario 160", "Honda", 2023, 115, "Skuter Matic")
motor2 = Motor("CBR 250RR", "Honda", 2021, 175, "Sport Fairing")

if __name__ == "__main__":
    print("=" * 45)
    print("     SISTEM RENTAL KENDARAAN (KASUS 02)    ")
    print("=" * 45)
    
    armada = [mobil1, mobil2, motor1, motor2]
    for unit in armada:
        unit.cek_spesifikasi()
    print("=" * 45)

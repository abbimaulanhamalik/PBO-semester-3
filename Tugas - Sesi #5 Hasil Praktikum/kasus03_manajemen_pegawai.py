# ==========================================
# KASUS 03: MULTIPLE INHERITANCE
# Sistem Manajemen Pegawai & Project Manager
# Pemrograman Berorientasi Objek - Python
# Mahasiswa: Abbi Maulanha Malik (NIM: 2595114007)
# ==========================================

class Pegawai:
    def __init__(self, id_pegawai, nama):
        self.id_pegawai = id_pegawai
        self.nama = nama

    def info_pegawai(self):
        print(f"ID Pegawai   : {self.id_pegawai}")
        print(f"Nama Pegawai : {self.nama}")

class Gaji:
    def __init__(self, gaji_pokok, tunjangan=0):
        self.gaji_pokok = gaji_pokok
        self.tunjangan = tunjangan

    def hitung_total_gaji(self):
        return self.gaji_pokok + self.tunjangan

    def info_gaji(self):
        print(f"Gaji Pokok   : Rp {self.gaji_pokok:,.0f}")
        print(f"Tunjangan    : Rp {self.tunjangan:,.0f}")
        print(f"Total Gaji   : Rp {self.hitung_total_gaji():,.0f}")

class PegawaiProyek:
    def __init__(self, nama_proyek, peran_proyek="Team Member"):
        self.nama_proyek = nama_proyek
        self.peran_proyek = peran_proyek

    def info_proyek(self):
        print(f"Nama Proyek  : {self.nama_proyek}")
        print(f"Peran        : {self.peran_proyek}")

class ProjectManager(Pegawai, Gaji, PegawaiProyek):
    def __init__(self, id_pegawai, nama, gaji_pokok, tunjangan, nama_proyek, departemen="IT Application"):
        Pegawai.__init__(self, id_pegawai, nama)
        Gaji.__init__(self, gaji_pokok, tunjangan)
        PegawaiProyek.__init__(self, nama_proyek, peran_proyek="Project Manager Lead")
        self.departemen = departemen

    def cetak_profil_lengkap(self):
        print("-" * 45)
        print(f"PROFIL PROJECT MANAGER: {self.nama.upper()}")
        print("-" * 45)
        self.info_pegawai()
        print(f"Departemen   : {self.departemen}")
        self.info_proyek()
        self.info_gaji()
        print("-" * 45)

# Instansiasi Objek Project Manager
pm1 = ProjectManager("PM-001", "Abbi Maulanha Malik", 12000000, 4500000, "Enterprise Resource Planning Modernization")
pm2 = ProjectManager("PM-002", "Dian Sastro", 11000000, 3500000, "Mobile Smart Campus Portal")

if __name__ == "__main__":
    print("=" * 45)
    print("   SISTEM MANAJEMEN PEGAWAI (KASUS 03)     ")
    print("=" * 45)
    pm1.cetak_profil_lengkap()
    pm2.cetak_profil_lengkap()

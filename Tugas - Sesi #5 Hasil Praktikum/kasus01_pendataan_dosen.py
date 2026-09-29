# ==========================================
# KASUS 01: CLASS & OBJECTS
# Sistem Pendataan Dosen
# Pemrograman Berorientasi Objek - Python
# Mahasiswa: Abbi Maulanha Malik (NIM: 2595114007)
# ==========================================

class Dosen:
    def __init__(self, nidn, nama, prodi, fakultas):
        self.nidn = nidn
        self.nama = nama
        self.prodi = prodi
        self.fakultas = fakultas

    def cek_profil(self):
        print(f"NIDN     : {self.nidn}")
        print(f"Nama     : {self.nama}")
        print(f"Prodi    : {self.prodi}")
        print(f"Fakultas : {self.fakultas}")
        print("-" * 40)

    def cek_prodi(self, target_prodi="Teknik Informatika"):
        if self.prodi.lower() == target_prodi.lower():
            print(f"Validasi: {self.nama} TERDAFTAR aktif di program studi {target_prodi}.")
        else:
            print(f"Validasi: {self.nama} BUKAN pengajar utama di program studi {target_prodi} (Homebase: {self.prodi}).")

# Instansiasi Minimal 3 Objek Dosen
dosen1 = Dosen("0712038501", "Dr. Ahmad Fauzi, M.Kom.", "Teknik Informatika", "Teknologi Informasi")
dosen2 = Dosen("0724088902", "Siti Nurhaliza, M.T.", "Sistem Informasi", "Teknologi Informasi")
dosen3 = Dosen("0705119103", "Budi Santoso, M.Kom.", "Teknik Informatika", "Teknologi Informasi")

if __name__ == "__main__":
    print("=" * 45)
    print("     SISTEM PENDATAAN DOSEN (KASUS 01)     ")
    print("=" * 45)
    
    daftar_dosen = [dosen1, dosen2, dosen3]
    for idx, d in enumerate(daftar_dosen, 1):
        print(f"Data Dosen ke-{idx}:")
        d.cek_profil()
        
    print("Pengecekan Validasi Prodi:")
    for d in daftar_dosen:
        d.cek_prodi("Teknik Informatika")
    print("=" * 45)

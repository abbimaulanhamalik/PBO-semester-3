import tkinter as tk
from tkinter import ttk, messagebox

# 1. Membuat jendela berjudul Formulir Identitas Mahasiswa
root = tk.Tk()
root.title("Formulir Identitas Mahasiswa")
root.geometry("460x500")
root.configure(bg="#F4F6F9")  # Warna latar utama yang konsisten

# Konfigurasi grid utama agar rata tengah
root.columnconfigure(0, weight=1)

# Judul Form (Menggunakan layout grid)
judul = tk.Label(
    root,
    text="FORMULIR IDENTITAS MAHASISWA",
    font=("Segoe UI", 14, "bold"),
    bg="#1E3A8A",
    fg="#FFFFFF",
    pady=12
)
judul.grid(row=0, column=0, sticky="ew", pady=(0, 15))

# Frame Utama untuk Input Form
form = tk.Frame(root, bg="#F4F6F9", padx=20, pady=5)
form.grid(row=1, column=0, sticky="ew")
form.columnconfigure(1, weight=1)

# 2 & 3. Label dan Entry untuk Nama
tk.Label(
    form, text="Nama :", font=("Segoe UI", 10, "bold"), bg="#F4F6F9", fg="#1E293B"
).grid(row=0, column=0, sticky="w", pady=6, padx=(0, 10))

nama = tk.Entry(form, width=32, font=("Segoe UI", 10), bg="#FFFFFF", fg="#0F172A")
nama.grid(row=0, column=1, sticky="ew", pady=6)
nama.insert(0, "Abbi Maulanha Malik")

# 2 & 3. Label dan Entry untuk NIM
tk.Label(
    form, text="NIM :", font=("Segoe UI", 10, "bold"), bg="#F4F6F9", fg="#1E293B"
).grid(row=1, column=0, sticky="w", pady=6, padx=(0, 10))

nim = tk.Entry(form, width=32, font=("Segoe UI", 10), bg="#FFFFFF", fg="#0F172A")
nim.grid(row=1, column=1, sticky="ew", pady=6)
nim.insert(0, "2595114007")

# 2 & 4. Label dan Pilihan Program Studi
tk.Label(
    form, text="Program Studi :", font=("Segoe UI", 10, "bold"), bg="#F4F6F9", fg="#1E293B"
).grid(row=2, column=0, sticky="w", pady=6, padx=(0, 10))

prodi = ttk.Combobox(
    form,
    values=["S1 Teknik Informatika", "Informatika", "Manajemen", "Akuntansi"],
    state="readonly",
    font=("Segoe UI", 10),
    width=30
)
prodi.grid(row=2, column=1, sticky="ew", pady=6)
prodi.set("S1 Teknik Informatika")

# Tugas Pengembangan 1: Input Alamat menggunakan widget Text
tk.Label(
    form, text="Alamat :", font=("Segoe UI", 10, "bold"), bg="#F4F6F9", fg="#1E293B"
).grid(row=3, column=0, sticky="nw", pady=6, padx=(0, 10))

alamat = tk.Text(form, width=32, height=4, font=("Segoe UI", 10), bg="#FFFFFF", fg="#0F172A")
alamat.grid(row=3, column=1, sticky="ew", pady=6)

# Fungsi Simpan & Tugas Pengembangan 3 (Validasi Nama dan NIM tidak kosong)
def simpan():
    val_nama = nama.get().strip()
    val_nim = nim.get().strip()
    val_prodi = prodi.get().strip()
    val_alamat = alamat.get("1.0", tk.END).strip()

    if not val_nama or not val_nim:
        messagebox.showwarning("Validasi Gagal", "Kolom Nama dan NIM tidak boleh kosong!")
        hasil.config(
            text="Peringatan: Nama dan NIM wajib diisi!",
            fg="#DC2626"
        )
        return

    hasil.config(
        text=f"DATA MAHASISWA TERSIMPAN\n"
             f"Nama          : {val_nama}\n"
             f"NIM           : {val_nim}\n"
             f"Program Studi : {val_prodi if val_prodi else '-'}\n"
             f"Alamat        : {val_alamat if val_alamat else '-'}",
        fg="#1E3A8A"
    )

# 7. Fungsi Reset untuk mengosongkan formulir
def reset():
    nama.delete(0, tk.END)
    nim.delete(0, tk.END)
    prodi.set("")
    alamat.delete("1.0", tk.END)
    hasil.config(text="")

# Tugas Pengembangan 5: Fungsi Keluar
def keluar():
    root.destroy()

# Frame Tombol dengan layout grid()
tombol_frame = tk.Frame(root, bg="#F4F6F9")
tombol_frame.grid(row=2, column=0, pady=15)

btn_simpan = tk.Button(
    tombol_frame, text="Simpan", command=simpan,
    bg="#2563EB", fg="#FFFFFF", activebackground="#1D4ED8", activeforeground="#FFFFFF",
    font=("Segoe UI", 10, "bold"), width=10, relief="flat", cursor="hand2"
)
btn_simpan.grid(row=0, column=0, padx=6)

btn_reset = tk.Button(
    tombol_frame, text="Reset", command=reset,
    bg="#F59E0B", fg="#FFFFFF", activebackground="#D97706", activeforeground="#FFFFFF",
    font=("Segoe UI", 10, "bold"), width=10, relief="flat", cursor="hand2"
)
btn_reset.grid(row=0, column=1, padx=6)

btn_keluar = tk.Button(
    tombol_frame, text="Keluar", command=keluar,
    bg="#DC2626", fg="#FFFFFF", activebackground="#B91C1C", activeforeground="#FFFFFF",
    font=("Segoe UI", 10, "bold"), width=10, relief="flat", cursor="hand2"
)
btn_keluar.grid(row=0, column=2, padx=6)

# 6. Menampilkan hasil input pada Label menggunakan grid()
hasil = tk.Label(
    root,
    text="",
    font=("Segoe UI", 10),
    bg="#E2E8F0",
    fg="#1E3A8A",
    justify="left",
    anchor="w",
    padx=15,
    pady=10,
    relief="groove"
)
hasil.grid(row=3, column=0, sticky="ew", padx=20, pady=10)

root.mainloop()
import os
import shutil
import tempfile


def main():
    """Mendemonstrasikan operasi direktori dan file dengan aman."""
    current_directory = os.getcwd()
    print(f"Direktori saat ini: {current_directory}")

    # Gunakan direktori sementara agar contoh tidak mengubah file pengguna.
    with tempfile.TemporaryDirectory(prefix="python_file_management_") as temporary_directory:
        original_directory = os.getcwd()
        os.chdir(temporary_directory)

        try:
            print(f"Direktori kerja contoh: {os.getcwd()}")

            # Membuat direktori dan file.
            os.mkdir("test")
            with open(os.path.join("test", "myfile.txt"), "w", encoding="utf-8") as file:
                file.write("Contoh pengelolaan file dan direktori dengan Python.\n")

            print(f"Isi direktori: {os.listdir()}")
            print(f"Isi folder test: {os.listdir('test')}")

            # Mengganti nama direktori.
            os.rename("test", "new_one")
            print(f"Setelah rename: {os.listdir()}")

            # Membaca file yang telah dibuat.
            file_path = os.path.join("new_one", "myfile.txt")
            with open(file_path, "r", encoding="utf-8") as file:
                print(f"Isi file: {file.read().strip()}")

            # Menghapus file, lalu menghapus direktori yang sudah kosong.
            os.remove(file_path)
            os.rmdir("new_one")
            print(f"Setelah penghapusan: {os.listdir()}")

            # Contoh rmtree untuk direktori tidak kosong.
            os.mkdir("mydir")
            with open(os.path.join("mydir", "contoh.txt"), "w", encoding="utf-8") as file:
                file.write("File ini akan dihapus bersama foldernya.\n")
            shutil.rmtree("mydir")
            print(f"Folder mydir berhasil dihapus: {not os.path.exists('mydir')}")
        finally:
            os.chdir(original_directory)


if __name__ == "__main__":
    main()
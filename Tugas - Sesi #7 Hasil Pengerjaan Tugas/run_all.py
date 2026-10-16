# ==============================================================================
# Script Otomasi Eksekusi & Pembuatan Laporan Run Code Sesi #7
# Mahasiswa : Abbi Maulanha Malik
# NIM       : 2595114007
# Kelas     : TI-A / 2025
# Matakuliah: Pemrograman Berorientasi Objek (PBO) - Python
# Dosen     : Edwin Hari Agus Prastyo, S.Kom., M.Kom.
# ==============================================================================

import subprocess
import sys
import os
from datetime import datetime

# Pastikan output terminal mendukung UTF-8 pada Windows console
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

SCRIPTS = [
    ("01_python_datetime_module.py", "Python datetime Module", "https://www.programiz.com/python-programming/datetime"),
    ("02_python_datetime_strftime.py", "Python datetime.strftime()", "https://www.programiz.com/python-programming/datetime/strftime"),
    ("03_python_datetime_strptime.py", "Python datetime.strptime()", "https://www.programiz.com/python-programming/datetime/strptime"),
    ("04_python_current_date_and_time.py", "Python Current Date and Time", "https://www.programiz.com/python-programming/datetime/current-datetime"),
    ("05_python_current_time.py", "Python Current Time", "https://www.programiz.com/python-programming/datetime/current-time"),
    ("06_python_timestamp_to_datetime.py", "Python Timestamp to Datetime and Vice-Versa", "https://www.programiz.com/python-programming/datetime/timestamp-datetime"),
    ("07_python_time_module.py", "Python time Module", "https://www.programiz.com/python-programming/time"),
    ("08_python_time_sleep.py", "Python time.sleep()", "https://www.programiz.com/python-programming/time/sleep"),
]

def run_script(script_name: str) -> tuple[int, str]:
    cmd = [sys.executable, script_name]
    proc = subprocess.run(
        cmd,
        cwd=os.path.dirname(os.path.abspath(__file__)),
        capture_output=True,
        text=True
    )
    output = proc.stdout
    if proc.stderr:
        output += "\n[STDERR]\n" + proc.stderr
    return proc.returncode, output

def main():
    print("=" * 70)
    print("   MEMULAI EKSEKUSI SELURUH CODE PRAKTIKUM SESI #7 (8 MODUL)   ")
    print("=" * 70)

    results = []

    for idx, (filename, title, url) in enumerate(SCRIPTS, 1):
        print(f"\n[{idx}/8] Menjalankan {filename} ({title})...")
        code, out = run_script(filename)
        status = "SUCCESS" if code == 0 else f"FAILED (Code {code})"
        print(f"Status: {status}")
        results.append({
            "index": idx,
            "filename": filename,
            "title": title,
            "url": url,
            "exit_code": code,
            "output": out
        })
        print(out.strip())

    # Bangun Laporan Markdown
    report_filename = "Laporan_Hasil_Run_Code_Sesi_7.md"
    current_time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    md_lines = [
        "# 📄 LAPORAN HASIL RUN CODE — PRAKTIKUM SESI #7",
        "## Pemrograman Berorientasi Objek (PBO) — Modul `datetime` & `time` Python",
        "",
        "---",
        "",
        "### 👨‍🎓 Identitas Mahasiswa",
        "",
        "| Informasi | Keterangan |",
        "| :--- | :--- |",
        "| **Nama Lengkap** | **Abbi Maulanha Malik** |",
        "| **NIM** | **2595114007** |",
        "| **Kelas / Angkatan** | **TI-A / 2025** |",
        "| **Program Studi** | S1 Teknik Informatika |",
        "| **Fakultas** | Fakultas Teknologi Informasi (FTI) |",
        "| **Perguruan Tinggi** | Universitas Hasyim Asy'ari (UNHASY) Tebuireng Jombang |",
        "| **Dosen Pengampu** | **Edwin Hari Agus Prastyo, S.Kom., M.Kom.** |",
        "| **Waktu Eksekusi** | " + current_time_str + " |",
        "| **Link Repositori Git** | [GitHub: abbimaulanhamalik/PBO-semester-3](https://github.com/abbimaulanhamalik/PBO-semester-3) |",
        "",
        "---",
        "",
        "## 📌 Ringkasan Materi & URL Sumber (Programiz)",
        "",
        "Seluruh kode sumber pada tugas ini diimplementasikan secara komprehensif dari 8 modul resmi Programiz:",
        "",
        "| No | Topik Modul | Berkas Program | URL Sumber Programiz | Status Run |",
        "|:--:|:---|:---|:---|:---:|",
    ]

    for item in results:
        status_icon = "✅ Sukses" if item["exit_code"] == 0 else "❌ Gagal"
        md_lines.append(f"| {item['index']:02d} | **{item['title']}** | [`{item['filename']}`]({item['filename']}) | [{item['url']}]({item['url']}) | {status_icon} |")

    md_lines.extend([
        "",
        "---",
        "",
        "## 🖥️ Detail Laporan Hasil Run Code Tiap Modul",
        ""
    ])

    for item in results:
        md_lines.append(f"### {item['index']}. {item['title']}")
        md_lines.append(f"- **Berkas Kode**: [`{item['filename']}`]({item['filename']})")
        md_lines.append(f"- **Sumber Tutorial**: [{item['url']}]({item['url']})")
        md_lines.append(f"- **Exit Code**: `{item['exit_code']}`")
        md_lines.append("")
        md_lines.append("```text")
        md_lines.append(item["output"].strip())
        md_lines.append("```")
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

    md_lines.append("<div align=\"center\">")
    md_lines.append("  <sub>Laporan ini digenerate secara otomatis dari output eksekusi Python asli pada sistem.</sub><br>")
    md_lines.append("  <sub><b>Teknik Informatika — Universitas Hasyim Asy'ari Tebuireng Jombang</b></sub>")
    md_lines.append("</div>")

    report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), report_filename)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    print("\n" + "=" * 70)
    print(f"✅ Seluruh program selesai dijalankan!")
    print(f"📄 Laporan hasil run berhasil disimpan di: {report_filename}")
    print("=" * 70)

if __name__ == "__main__":
    main()

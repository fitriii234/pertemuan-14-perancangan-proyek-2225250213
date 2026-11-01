from pathlib import Path
from .analisis import validasi_nilai


def baca_data(path):
    """Format file: nama,nilai. Baris yang tidak valid dilaporkan dan dilewati."""
    path = Path(path)
    data_valid = []
    if not path.exists():
        raise FileNotFoundError(f"File tidak ditemukan: {path}")

    with path.open("r", encoding="utf-8") as file:
        for nomor, baris in enumerate(file, start=1):
            teks = baris.strip()
            if not teks:
                continue
            bagian = teks.split(",")
            if len(bagian) != 2:
                print(f"Baris {nomor} dilewati: format harus nama,nilai.")
                continue
            nama = bagian[0].strip()
            if not nama:
                print(f"Baris {nomor} dilewati: nama kosong.")
                continue
            try:
                nilai = float(bagian[1].strip())
            except ValueError:
                print(f"Baris {nomor} dilewati: nilai bukan angka.")
                continue
            if not validasi_nilai(nilai):
                print(f"Baris {nomor} dilewati: nilai harus 0-100.")
                continue
            data_valid.append({"nama": nama, "nilai": nilai})
    return data_valid


def simpan_laporan(teks, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(teks, encoding="utf-8")
    return path

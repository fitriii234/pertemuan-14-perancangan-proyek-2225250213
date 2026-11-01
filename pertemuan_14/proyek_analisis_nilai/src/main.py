from pathlib import Path
from .data_io import baca_data, simpan_laporan
from .analisis import hitung_statistik, hitung_ketuntasan
from .utilitas import buat_laporan

ROOT = Path(__file__).resolve().parents[1]
FILE_INPUT = ROOT / "data" / "nilai_contoh.txt"
FILE_OUTPUT = ROOT / "output" / "laporan_nilai.txt"
KKM = 60


def main():
    try:
        data = baca_data(FILE_INPUT)
        if not data:
            print("Tidak ada data valid. Program selesai.")
            return

        statistik = hitung_statistik(data)
        ketuntasan = hitung_ketuntasan(data, KKM)
        laporan = buat_laporan(data, statistik, ketuntasan, KKM)
        print(laporan)
        simpan_laporan(laporan, FILE_OUTPUT)
        print(f"Laporan tersimpan di: {FILE_OUTPUT}")
    except FileNotFoundError as error:
        print(error)
    except (OSError, ValueError) as error:
        print(f"Terjadi kesalahan: {error}")


if __name__ == "__main__":
    main()

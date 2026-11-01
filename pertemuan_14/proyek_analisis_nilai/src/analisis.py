def validasi_nilai(nilai):
    """Mengembalikan True jika nilai numerik berada pada rentang 0-100."""
    return isinstance(nilai, (int, float)) and not isinstance(nilai, bool) and 0 <= nilai <= 100


def hitung_statistik(data):
    """Menghitung jumlah data, rata-rata, minimum, dan maksimum."""
    if not data:
        raise ValueError("Tidak ada data nilai valid untuk dihitung.")
    nilai = [item["nilai"] for item in data]
    return {
        "jumlah_data": len(nilai),
        "rata_rata": sum(nilai) / len(nilai),
        "minimum": min(nilai),
        "maksimum": max(nilai),
    }


def tentukan_status(nilai, kkm=60):
    if not validasi_nilai(nilai):
        raise ValueError("Nilai harus berupa angka 0-100.")
    return "Tuntas" if nilai >= kkm else "Belum tuntas"


def hitung_ketuntasan(data, kkm=60):
    tuntas = sum(1 for item in data if tentukan_status(item["nilai"], kkm) == "Tuntas")
    return {"tuntas": tuntas, "belum_tuntas": len(data) - tuntas}

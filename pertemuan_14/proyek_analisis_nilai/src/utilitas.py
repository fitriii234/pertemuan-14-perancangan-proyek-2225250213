def buat_laporan(data, statistik, ketuntasan, kkm=60):
    baris = [
        "LAPORAN ANALISIS NILAI MATEMATIKA",
        "=" * 36,
        f"Jumlah siswa : {statistik['jumlah_data']}",
        f"Rata-rata    : {statistik['rata_rata']:.2f}",
        f"Nilai minimum: {statistik['minimum']:.2f}",
        f"Nilai maksimum: {statistik['maksimum']:.2f}",
        f"KKM          : {kkm}",
        f"Tuntas       : {ketuntasan['tuntas']}",
        f"Belum tuntas : {ketuntasan['belum_tuntas']}",
        "",
        "RINCIAN SISWA",
    ]
    for item in data:
        status = "Tuntas" if item["nilai"] >= kkm else "Belum tuntas"
        baris.append(f"- {item['nama']}: {item['nilai']:g} ({status})")
    return "\n".join(baris) + "\n"

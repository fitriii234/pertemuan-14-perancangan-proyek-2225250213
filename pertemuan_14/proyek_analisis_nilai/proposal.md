# Proposal Proyek: Program Rekap dan Analisis Nilai Matematika Kelas

## Latar Belakang
Guru memerlukan program sederhana untuk membaca data nilai, memvalidasi isi, menghitung statistik,
menentukan ketuntasan, dan menyimpan laporan.

## Pengguna dan Tujuan
Pengguna utama adalah guru matematika. Program membantu rekap nilai dilakukan lebih cepat dan konsisten.

## Ruang Lingkup
Fitur wajib:
1. Membaca file nilai.
2. Memvalidasi nilai 0-100.
3. Menghitung rata-rata, minimum, dan maksimum.
4. Menghitung jumlah tuntas/belum tuntas berdasarkan KKM.
5. Menyimpan laporan ke file teks.

## IPO
- Input: file berisi nama dan nilai.
- Proses: baca file, validasi, hitung statistik, klasifikasi ketuntasan.
- Output: ringkasan statistik di terminal dan laporan teks.

## Struktur Program
- `src/data_io.py`: membaca data dan menyimpan laporan.
- `src/analisis.py`: validasi, statistik, dan ketuntasan.
- `src/utilitas.py`: membentuk teks laporan.
- `src/main.py`: mengatur alur program.

## Struktur Data
List berisi dictionary dengan key `nama` dan `nilai`.

## Test Case
Lihat `tests/test_case.md` dan `tests/test_analisis.py`.

## Batasan
Program berjalan melalui terminal/console Python.

# pertemuan-14-perancangan-proyek-2225250213# Proyek Analisis Nilai Kelas

## Persyaratan
Python 3.9 atau lebih baru.

## Menjalankan program
Dari folder `proyek_analisis_nilai`, jalankan:

```bash
python -m src.main
```

Program membaca `data/nilai_contoh.txt`, menampilkan statistik, lalu menyimpan
laporan ke `output/laporan_nilai.txt`.

## Menjalankan pengujian
```bash
python -m unittest discover -s tests -v
```

Format file input adalah satu siswa per baris:
```text
Nama,Nilai
Ayu,85
Budi,78
```
Nilai di luar rentang 0-100, nama kosong, dan format yang salah akan dilewati
dengan pesan yang menjelaskan masalahnya.
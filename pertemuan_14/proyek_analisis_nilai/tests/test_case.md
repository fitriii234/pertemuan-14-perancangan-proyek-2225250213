# Test Case Awal

| ID | Kategori | Input/Kondisi | Expected Result |
|---|---|---|---|
| TC01 | Normal | Nilai 80, 70, 90 | Rata-rata 80 |
| TC02 | Batas | Nilai 0 | Diterima sebagai nilai valid |
| TC03 | Batas | Nilai 100 | Diterima sebagai nilai valid |
| TC04 | Invalid | Nilai 105 | Ditolak dengan validasi |
| TC05 | Invalid | File tidak ada | FileNotFoundError ditangani |
| TC06 | Normal | Semua nilai >= KKM | Jumlah tuntas = jumlah data |

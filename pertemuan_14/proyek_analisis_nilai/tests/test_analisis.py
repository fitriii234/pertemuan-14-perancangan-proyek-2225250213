import unittest
from src.analisis import validasi_nilai, hitung_statistik, tentukan_status, hitung_ketuntasan


class TestAnalisisNilai(unittest.TestCase):
    def setUp(self):
        self.data = [
            {"nama": "Ayu", "nilai": 80},
            {"nama": "Budi", "nilai": 70},
            {"nama": "Citra", "nilai": 90},
        ]

    def test_validasi_batas(self):
        self.assertTrue(validasi_nilai(0))
        self.assertTrue(validasi_nilai(100))
        self.assertFalse(validasi_nilai(-1))
        self.assertFalse(validasi_nilai(101))
        self.assertFalse(validasi_nilai("abc"))

    def test_statistik(self):
        hasil = hitung_statistik(self.data)
        self.assertEqual(hasil["jumlah_data"], 3)
        self.assertEqual(hasil["rata_rata"], 80)
        self.assertEqual(hasil["minimum"], 70)
        self.assertEqual(hasil["maksimum"], 90)

    def test_statistik_kosong(self):
        with self.assertRaises(ValueError):
            hitung_statistik([])

    def test_status_batas_kkm(self):
        self.assertEqual(tentukan_status(60), "Tuntas")
        self.assertEqual(tentukan_status(59), "Belum tuntas")

    def test_ketuntasan(self):
        hasil = hitung_ketuntasan(self.data, 80)
        self.assertEqual(hasil, {"tuntas": 2, "belum_tuntas": 1})


if __name__ == "__main__":
    unittest.main()

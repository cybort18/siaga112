# SIAGA 112 - AI Innovation Challenge COMPFEST 17

Proyek ini adalah sistem pintar untuk panggilan darurat 112 di Jakarta.

## Fitur
- **Speech-to-Text**: Mengubah suara jadi teks menggunakan Google Cloud.
- **Klasifikasi Darurat**: Mengenali jenis darurat (kecelakaan, kebakaran, medis, banjir).
- **NER**: Mendeteksi lokasi insiden.
- **Deteksi Klaster**: Mengidentifikasi insiden besar berdasarkan lokasi.

## Cara Menjalankan
1. Aktifkan virtual environment: `.\siaga112_env\Scripts\Activate.ps1`
2. Setel kredensial Google Cloud: `$env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\HP\Documents\Secure\siaga112-87b4ed06926e.json"`
3. Jalankan: `python src\stt.py`

## Contoh Output
Transkripsi: ada kecelakaan di flyover Cawang

Jenis darurat: kecelakaan

Lokasi: flyover Cawang

Klaster insiden:
Klaster 0: 2 laporan

ada kecelakaan di flyover Cawang
ada kecelakaan di flyover Cawang
Klaster 1: 4 laporan
di Jalan Margonda Raya dekat kampus UI ada orang pingsan
di Jalan Margonda Raya dekat kampus UI ada orang pingsan
di Jalan Margonda Raya dekat kampus UI ada orang pingsan
di Jalan Margonda Raya dekat kampus UI ada orang pingsan
Klaster 2: 3 laporan
ada banjir di daerah Senen
ada banjir di daerah Senen
ada banjir di daerah Senen

## Catatan
- Gunakan file audio WAV mono di `data/`.
- Koordinat simulasi ada di `stt.py` untuk pengujian.
- Pastikan kredensial Google Cloud sudah disiapkan.
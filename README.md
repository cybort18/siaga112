\# SIAGA 112 - AI Innovation Challenge COMPFEST 17



Proyek ini adalah sistem pintar untuk panggilan darurat 112 di Jakarta.



\## Fitur

\- \*\*Speech-to-Text\*\*: Mengubah suara jadi teks menggunakan Google Cloud.

\- \*\*Klasifikasi Darurat\*\*: Mengenali jenis darurat (kecelakaan, kebakaran, medis, banjir).

\- \*\*NER\*\*: Mendeteksi lokasi insiden.

\- \*\*Deteksi Klaster\*\*: Mengidentifikasi insiden besar berdasarkan lokasi.



\## Cara Menjalankan

1\. Aktifkan virtual environment: `.\\siaga112\_env\\Scripts\\Activate.ps1`

2\. Setel kredensial Google Cloud: `$env:GOOGLE\_APPLICATION\_CREDENTIALS="C:\\Users\\HP\\Documents\\Secure\\siaga112-87b4ed06926e.json"`

3\. Jalankan: `python src\\stt.py`



\## Contoh Output
ada kecelakaan di flyover Cawang,6.25,106.85

ada kecelakaan di flyover Cawang,6.26,106.86

ada kecelakaan di flyover Cawang,6.25,106.85

di Jalan Margonda Raya dekat kampus UI ada orang pingsan,6.36,106.83

di Jalan Margonda Raya dekat kampus UI ada orang pingsan,6.36,106.83

di Jalan Margonda Raya dekat kampus UI ada orang pingsan,6.36,106.83

di Jalan Margonda Raya dekat kampus UI ada orang pingsan,6.36,106.83

ada banjir di daerah Senen,6.18,106.84

ada banjir di daerah Senen,6.18,106.84

ada banjir di daerah Senen,6.18,106.84



\## Catatan

\- Gunakan file audio WAV mono di `data/`.

\- Koordinat simulasi ada di `stt.py` untuk pengujian.

\- Pastikan kredensial Google Cloud sudah disiapkan.


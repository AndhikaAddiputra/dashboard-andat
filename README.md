# Dashboard Analisis Spasial & Klastering Risiko Putus Sekolah Jawa Barat 2024

Dashboard interaktif berbasis **Dash (Plotly)** untuk memvisualisasikan hasil analisis klastering risiko putus sekolah di 27 Kabupaten/Kota Jawa Barat tahun 2024.

## Fitur

- **Choropleth Map** — Peta sebaran tingkat kerentanan (Tinggi/Sedang/Rendah) dengan kode warna: Merah (#d9534f), Jingga (#f0ad4e), Hijau (#5cb85c)
- **Klik Peta → Detail Wilayah** — Klik daerah di peta untuk menampilkan card informasi lengkap + insight naratif
- **Scatter Plot** — Korelasi kemiskinan vs angka putus sekolah per 10k penduduk
- **Bar Chart** — Breakdown putus sekolah per jenjang (SD/SMP/SMA/SMK/SLB)
- **Ranking Table** — Peringkat risiko 27 Kabupaten/Kota (sortable)
- **Cluster Summary** — Karakteristik centroid tiap klaster risiko
- **Filter Interaktif** — Pilih wilayah untuk highlight di semua visualisasi

## Dataset

| File | Deskripsi |
|------|-----------|
| `data/dataset_bersih.csv` | Dataset utama (27 baris, 18 kolom) — dari pipeline kelompok |
| `data/jabar_27.geojson` | Batas administrasi 27 Kab/Kota Jawa Barat (gabungan GADM + BIG) |
| `data/ranking_risiko_kabkota.csv` | Peringkat risiko berdasarkan indeks komposit |
| `data/cluster_summary.csv` | Statistik centroid per klaster |
| `data/correlation_matrix.csv` | Matriks korelasi antar variabel |

Sumber data: Buku Profil Perkembangan Kependudukan Jawa Barat 2024 (Kemendikdasmen) & BPS Provinsi Jawa Barat.

## Prasyarat

- Python 3.9+
- pip

## Instalasi

```bash
# Clone repositori
git clone <repo-url>
cd dashboard_dash

# Install dependensi
pip install -r requirements.txt
```

## Menjalankan

```bash
python3 app.py
```

Buka **http://127.0.0.1:8050** di browser.

## Struktur Proyek

```
dashboard_dash/
├── app.py              # Aplikasi Dash utama
├── requirements.txt    # Dependensi Python
├── README.md
├── data/               # Dataset & GeoJSON
│   ├── dataset_bersih.csv
│   ├── jabar_27.geojson
│   ├── ranking_risiko_kabkota.csv
│   ├── cluster_summary.csv
│   └── correlation_matrix.csv
└── assets/             # (opsional) aset statis
```

## Metrik Utama

- **Korelasi Pearson**: r = 0.3944 (p = 0.0418) — signifikan antara kemiskinan dan putus sekolah
- **Klaster**: 3 kelompok (K=3) menggunakan K-Means
  - **Risiko Tinggi**: 12 Kabupaten/Kota
  - **Risiko Sedang**: 11 Kabupaten/Kota
  - **Risiko Rendah**: 4 Kota
- **Silhouette Score**: 0.3409

## Dibuat Dengan

- [Dash](https://dash.plotly.com/) — Framework dashboard Python
- [Plotly](https://plotly.com/python/) — Visualisasi interaktif
- [Pandas](https://pandas.pydata.org/) — Manipulasi data
- GeoJSON: GADM v4.0 & Badan Informasi Geospasial (BIG)

## Lisensi

Hak cipta milik Kelompok 9 — Tugas Besar II4013 Data Analytics.

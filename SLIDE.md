# Slide Presentasi
## Analisis Spasial & Klastering Risiko Putus Sekolah di Jawa Barat 2024

**II4013 Data Analytics — Kelompok 9**

> Panduan: Setiap slide berisi poin-poin narasi. Tambahkan grafik/screenshot dari dashboard atau notebook analisis. Tanda `[]` menandakan placeholder yang perlu diisi.

---

### Slide 1 — Cover

**Judul:**
Analisis Spasial & Klastering Risiko Putus Sekolah
di Jawa Barat Tahun 2024

**Sub-judul:**
II4013 Data Analytics — Kelompok 9

**Anggota:**
- Andhika Maulana
- Arqila Surya Putra
- Muhammad Farhan
- Muhammad Naufal Fathan

**Logo:** `[Logo ITERA / Fakultas]`

---

### Slide 2 — Agenda

1. Latar Belakang & Rumusan Masalah
2. Data & Metodologi (OSEMN)
3. Hasil Analisis: Korelasi
4. Hasil Analisis: Klastering
5. Peta Sebaran Risiko
6. Dashboard Interaktif
7. Kesimpulan & Rekomendasi

---

### Slide 3 — Latar Belakang

**Masalah:**
- Angka putus sekolah Jawa Barat 2024 mencapai **5.940 siswa**
- **87,36%** terjadi di jenjang SD
- Disparitas antar wilayah sangat lebar:
  - Kab. Bogor: 621 siswa putus
  - Kota Bandung: 141 siswa putus
- Diperlukan pemetaan risiko untuk intervensi tepat sasaran

**Pertanyaan:**
- Wilayah mana yang paling rentan?
- Faktor apa yang berkorelasi?
- Bagaimana pengelompokan risikonya?

**Visual:** `[Grafik batang total putus per Kab/Kota — top 10]`

---

### Slide 4 — Data (Obtain)

**Sumber Data:**

| Sumber | Data |
|--------|------|
| Kemendikdasmen 2024 | Putus sekolah per jenjang (SD/SMP/SMA/SMK/SLB) |
| BPS Jabar 2024 | IPM, Kemiskinan, Proyeksi Penduduk |
| GADM + BIG | GeoJSON batas administrasi 27 Kab/Kota |

**18 variabel** — 27 Kabupaten/Kota — **0 missing value**

**Visual:** `[Tabel rangkuman variabel]`

---

### Slide 5 — Data Preparation (Scrub)

**Masalah & Penanganan:**

| Masalah | Tindakan |
|---------|----------|
| Data kemiskinan September kosong | Dihapus, hanya pakai Maret |
| Nama daerah tidak seragam | Diselaraskan ke format baku |
| Tipe data numerik salah | Dikonversi ke float/int |
| Outlier | IQR — tidak ada outlier signifikan |

**Hasil:** Dataset bersih, 27 baris × 18 kolom, siap analisis.

---

### Slide 6 — Analisis Deskriptif (Explore)

**Statistik Utama:**

| Variabel | Mean | Min | Max |
|----------|:----:|:---:|:---:|
| Total Putus Sekolah | 220 | 27 | 621 |
| Persentase Kemiskinan | 8,01% | 2,34% | 11,93% |
| IPM | 74,68 | 68,89 | 83,75 |
| Putus Sekolah per 10k | 1,13 | 0,33 | 1,99 |

**Dominasi Jenjang:** SD (87,36%) > SMK (5,64%) > SMP (3,87%)

**Visual:** `[Bar chart breakdown jenjang]`

---

### Slide 7 — Korelasi

**Temuan Utama:**

| Hubungan | r | Interpretasi |
|----------|:-:|--------------|
| Kemiskinan ↔ Putus Sekolah | **0,39** | Positif signifikan (p=0,04) |
| IPM ↔ Risk Index | **-0,96** | Negatif sangat kuat |
| Kemiskinan ↔ Risk Index | **0,81** | Positif kuat |
| RLS ↔ Risk Index | **-0,91** | Negatif sangat kuat |

**Insight:**
> "Wilayah dengan IPM dan tingkat pendidikan lebih rendah **secara signifikan** memiliki risiko putus sekolah lebih tinggi. Kemiskinan menjadi pendorong utama."

**Visual:** `[Scatter plot kemiskinan vs putus sekolah — dashboard screenshot]`

---

### Slide 8 — Klastering — Metode (Model)

**Algoritma:** K-Means

**Penentuan k optimal:**
- **Metode Elbow:** Titik siku di k=3
- **Silhouette Score:** 0,3409 (struktur wajar)

![Grafik Elbow + Silhouette][] *\*placeholder*

---

### Slide 9 — Klastering — Hasil

| Klaster | Wilayah | IPM | Kemiskinan | Putus/10k |
|---------|:-------:|:---:|:----------:|:---------:|
| 🔴 **Tinggi** (12) | 11 Kab + 1 Kota | 71,46 | 10,12% | 1,43 |
| 🟡 **Sedang** (11) | 7 Kab + 4 Kota | 75,28 | 7,30% | 1,04 |
| 🟢 **Rendah** (4) | 4 Kota Besar | 82,66 | 3,65% | 0,51 |

**Pola:** Kabupaten agraris = risiko tinggi, kota besar = risiko rendah.

**Visual:** `[Tabel karakteristik klaster]`

---

### Slide 10 — Peta Sebaran Risiko

**Choropleth Map — 27 Kabupaten/Kota Jawa Barat**

- **Merah (#d9534f):** Risiko Tinggi
- **Jingga (#f0ad4e):** Risiko Sedang
- **Hijau (#5cb85c):** Risiko Rendah

**Pola Spasial:**
- Risiko Tinggi → **Selatan & Timur** (pegunungan, agraris)
- Risiko Rendah → **Bandung Raya & Jakarta satelit**

**Visual:** `[Screenshot choropleth map dari dashboard]`

---

### Slide 11 — Peringkat Wilayah

**Top 5 Risiko Tertinggi:**

| # | Wilayah | Risk Index | Kemiskinan |
|:-:|---------|:----------:|:----------:|
| 1 | Kab. Tasikmalaya | 89,43 | 10,23% |
| 2 | Kab. Cianjur | 84,49 | 10,14% |
| 3 | Kab. Indramayu | 76,49 | 11,93% |
| 4 | Kab. Sukabumi | 73,83 | 6,87% |
| 5 | Kab. Bandung Barat | 73,28 | 10,49% |

**Bottom 5 (Terendah):**

| # | Wilayah | Risk Index | Kemiskinan |
|:-:|---------|:----------:|:----------:|
| 27 | Kota Bandung | 4,71 | 3,87% |
| 26 | Kota Depok | 9,00 | 2,34% |
| 25 | Kota Bekasi | 13,06 | 4,01% |

**Rasio** Kab. Tasikmalaya : Kota Bandung = **19:1**

**Visual:** `[Screenshot ranking table dashboard]`

---

### Slide 12 — Dashboard Interaktif

**Teknologi:** Dash (Plotly) + Pandas

**5 Komponen:**
1. 🗺️ **Choropleth Map** — klik wilayah → detail card
2. 📈 **Scatter Plot** — korelasi kemiskinan vs putus sekolah
3. 📊 **Bar Chart** — breakdown per jenjang
4. 🏆 **Ranking Table** — sortable, 10 per halaman
5. 📋 **Cluster Summary** — karakteristik centroid

**Fitur:**
- Filter dropdown sinkron ke semua grafik
- Klik peta update dropdown & detail card
- Warna sesuai tingkat risiko

**Cara menjalankan:**
```bash
git clone [repo-url]
cd dashboard-andat
pip install -r requirements.txt
python3 app.py
# Buka http://localhost:8050
```

**Visual:** `[Screenshot penuh dashboard atau screencast singkat]`

---

### Slide 13 — Kesimpulan

1. **12 wilayah** (44%) masuk klaster **Risiko Tinggi** — mayoritas kabupaten agraris di selatan/timur
2. **Kemiskinan** berkorelasi signifikan dengan putus sekolah (r=0,39; p=0,04)
3. **SD** menyumbang **87,36%** dari total putus sekolah — prioritas utama
4. **IPM** dan **RLS** menjadi proksi terkuat risiko putus sekolah (r < -0,9)
5. **Jurang lebar** antar wilayah: rasio 19:1 antara tertinggi dan terendah

---

### Slide 14 — Rekomendasi Kebijakan

| Prioritas | Target | Intervensi |
|-----------|--------|------------|
| 🥇 **Sangat Tinggi** | 12 Kab/Kota Risiko Tinggi | BOS afirmatif, beasiswa, program kejar paket |
| 🥈 **Tinggi** | 11 Kab/Kota Risiko Sedang | Penguatan kapasitas sekolah, pelatihan guru |
| 🥉 **Sedang** | 4 Kota Risiko Rendah | Program pencegahan, pendidikan inklusif |

**Fokus khusus:**
- **SD** — early warning system deteksi risiko putus
- **SMK** — reformasi kurikulum, perluas program magang
- **SLB** — perluasan akses pendidikan inklusif

---

### Slide 15 — Penutup

**Terima Kasih**

Kelompok 9 — II4013 Data Analytics

**Kontak:** `[]`

**Repositori:** `[URL GitHub]`

---

## 📋 Catatan Persiapan Presentasi

| Poin | Saran |
|------|-------|
| **Durasi** | 4-5 menit untuk 14 slide (≈20 detik/slide) |
| **Pembagian** | Masing-masing anggota presentasi 3-4 slide |
| **Demo Dashboard** | Siapkan `python3 app.py` berjalan di lokal, atau siapkan screenshot cadangan jika jaringan bermasalah |
| **Grafik** | Gunakan screenshot dari dashboard untuk grafik di slide — tidak perlu plot ulang |
| **Backup** | Siapkan PDF laporan + screenshot di USB drive |
| **Peta** | Pastikan GeoJSON termuat sempurna sebelum demo |

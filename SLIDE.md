# Slide Presentasi
## Analisis Spasial & Klastering Risiko Putus Sekolah di Jawa Barat 2024

**II4013 Data Analytics — Kelompok 9**

> Panduan: Setiap slide berisi poin-poin narasi. Tanda `[]` menandakan placeholder yang perlu diisi.

---

### Slide 1 — Cover

**Judul:**
Analisis Spasial & Klastering Risiko Putus Sekolah
di Jawa Barat Tahun 2024

**Sub-judul:**
II4013 Data Analytics — Kelompok 9

**Anggota:**
- Andhika Maulana — Dashboard Developer
- Arqila Surya Putra — Data Analyst / Modeler
- Muhammad Farhan — Data Engineer & Presentation Support
- Muhammad Naufal Fathan — Documentation & Insight Lead

**Logo:** `[Logo ITERA / Fakultas]`

---

### Slide 2 — Agenda (OSEMN)

1. **Pendahuluan**
2. **O**btain — Akuisisi & Dokumentasi Data
3. **S**crub — Pembersihan & Integrasi Data
4. **E**xplore — Mempelajari & Analisis Data
5. **M**odel — Pemodelan & Analisis Lanjutan
6. i**N**terpret — Hasil & Visualisasi
7. **Kesimpulan** & Rekomendasi

---

### Slide 3 — Pendahuluan

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

### Slide 4 — Akuisisi Data (Obtain)

**Sumber Data:**

| Sumber | Data |
|--------|------|
| Kemendikdasmen 2024 | Putus sekolah per jenjang (SD/SMP/SMA/SMK/SLB) |
| BPS Jabar 2024 | IPM, Kemiskinan, Proyeksi Penduduk |
| GADM + BIG | GeoJSON batas administrasi 27 Kab/Kota |

**18 variabel** — 27 Kabupaten/Kota — **0 missing value**

**GeoJSON:** Gabungan GADM v4.0 (26 wilayah) + BIG (Kab. Pangandaran).

**Visual:** `[Tabel variabel lengkap]`

---

### Slide 5 — Pembersihan Data (Preprocessing)

**Masalah & Penanganan:**

| Masalah | Tindakan |
|---------|----------|
| Data kemiskinan September kosong | Dihapus, hanya pakai Maret |
| Nama daerah tidak seragam | Diselaraskan ke format baku |
| Tipe data numerik salah | Dikonversi ke float/int |
| Outlier | IQR — tidak ada outlier signifikan |

**Hasil:** Dataset bersih, 27 baris × 18 kolom, siap analisis.

---

### Slide 6 — Eksplorasi Data (Explore)

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

### Slide 7 — Korelasi (Explore)

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

### Slide 8 — Pemodelan K-Means (Modelling)

**Algoritma:** K-Means Clustering

**Variabel pemodelan:**
Persentase Kemiskinan, IPM, RLS, HLS, Pengeluaran per Kapita, Total Putus, Putus per 10k

**Penentuan k optimal:**
- **Metode Elbow:** Titik siku di **k=3**
- **Silhouette Score:** **0,3409** (struktur wajar)

| k | Silhouette |
|:-:|:----------:|
| 2 | 0,3120 |
| **3** | **0,3409** |
| 4 | 0,2981 |

**Kesimpulan:** k=3 optimal.

**Visual:** `[Grafik Elbow + Silhouette]`

---

### Slide 9 — Hasil Klastering

| Klaster | Wilayah | IPM | Kemiskinan | Putus/10k |
|---------|:-------:|:---:|:----------:|:---------:|
| 🔴 **Tinggi** (12) | 11 Kab + 1 Kota | 71,46 | 10,12% | 1,43 |
| 🟡 **Sedang** (11) | 7 Kab + 4 Kota | 75,28 | 7,30% | 1,04 |
| 🟢 **Rendah** (4) | 4 Kota Besar | 82,66 | 3,65% | 0,51 |

**Karakteristik Centroid:**

| Klaster | Rata-rata Putus | Rata-rata RLS |
|---------|:---------------:|:-------------:|
| Prioritas Rendah | 115,25 | 11,49 thn |
| Prioritas Sedang | 295,95 | 8,38 thn |
| Prioritas Tinggi | 385,33 | 9,03 thn |

**Visual:** `[Tabel karakteristik klaster]`

---

### Slide 10 — Peta Sebaran Risiko

**Choropleth Map — 27 Kabupaten/Kota Jawa Barat**

- **Merah (#d9534f):** Risiko Tinggi
- **Jingga (#f0ad4e):** Risiko Sedang
- **Hijau (#5cb85c):** Risiko Rendah

**Pola Spasial:**
- Risiko Tinggi → **Selatan & Timur** (Priangan Timur, Ciayumajakuning — agraris)
- Risiko Sedang → **Zona transisi** (penyangga ibu kota)
- Risiko Rendah → **Bandung Raya & Jakarta satelit** (perkotaan)

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
| 24 | Kota Cimahi | 21,96 | 4,39% |
| 23 | Kota Bogor | 36,04 | 6,53% |

**Rasio** Kab. Tasikmalaya : Kota Bandung = **19:1**

**Visual:** `[Screenshot ranking table dashboard]`

---

### Slide 12 — Dashboard Interaktif

**Teknologi:** Dash (Plotly) + Pandas

**5 Komponen:**
1. 🗺️ **Choropleth Map** — klik wilayah → detail card + insight naratif
2. 📈 **Scatter Plot** — korelasi kemiskinan vs putus sekolah
3. 📊 **Bar Chart** — breakdown per jenjang (SD/SMP/SMA/SMK/SLB)
4. 🏆 **Ranking Table** — sortable, 10 per halaman
5. 📋 **Cluster Summary** — karakteristik centroid tiap klaster

**Fitur:**
- Filter dropdown sinkron ke semua grafik
- Klik peta → filter dropdown & detail card terupdate
- Warna sesuai tingkat risiko (merah/jingga/hijau)

**Cara menjalankan:**
```bash
git clone https://github.com/AndhikaAddiputra/dashboard-andat.git
cd dashboard-andat
pip install -r requirements.txt
python3 app.py
# Buka http://localhost:8050
```

**Visual:** `[Screenshot penuh dashboard]`

---

### Slide 13 — Detail Klaster & Insight

**Risiko Tinggi (12 Wilayah):**
- IPM 71,46 | Kemiskinan 10,12% | Putus/10k 1,43
- 11 kabupaten + 1 kota (Kota Tasikmalaya)
- Terkonsentrasi di selatan & timur Jabar

**Risiko Sedang (11 Wilayah):**
- IPM 75,28 | Kemiskinan 7,30% | Putus/10k 1,04
- Zona transisi, termasuk penyangga ibu kota

**Risiko Rendah (4 Wilayah):**
- IPM 82,66 | Kemiskinan 3,65% | Putus/10k 0,51
- Kota besar: Bandung, Bekasi, Depok, Cimahi

---

### Slide 14 — Kesimpulan

1. **12 wilayah** (44%) masuk klaster **Risiko Tinggi** — didominasi kabupaten agraris di selatan/timur Jabar
2. **Kemiskinan** berkorelasi signifikan dengan putus sekolah (r=0,39; p=0,04)
3. **SD** menyumbang **87,36%** dari total putus sekolah (5.940 siswa) — prioritas utama
4. **IPM** dan **RLS** menjadi proksi terkuat risiko putus sekolah (r < -0,9)
5. **Jurang lebar** antar wilayah: rasio 19:1 antara tertinggi dan terendah

---

### Slide 15 — Rekomendasi Kebijakan

| Prioritas | Target | Intervensi |
|-----------|--------|------------|
| 🥇 **Sangat Tinggi** | 12 Kab/Kota Risiko Tinggi | BOS afirmatif, beasiswa, program kejar paket |
| 🥈 **Tinggi** | 11 Kab/Kota Risiko Sedang | Penguatan kapasitas sekolah, pelatihan guru |
| 🥉 **Sedang** | 4 Kota Risiko Rendah | Program pencegahan, pendidikan inklusif |

**Fokus khusus:**
- **SD** — early warning system deteksi risiko putus
- **SMK** — reformasi kurikulum berbasis industri, perluas magang
- **SLB** — perluasan akses pendidikan inklusif di kabupaten

---

### Slide 16 — Penutup

**Terima Kasih**

Kelompok 9 — II4013 Data Analytics

**Kontak:** `[]`

**Repositori:** https://github.com/AndhikaAddiputra/dashboard-andat

---

## 📋 Catatan Persiapan Presentasi

| Poin | Saran |
|------|-------|
| **Durasi** | 4-6 menit untuk 16 slide (≈20-25 detik/slide) |
| **Pembagian** | Masing-masing anggota presentasi 3-4 slide |
| **Demo Dashboard** | Siapkan `python3 app.py` berjalan di lokal, atau siapkan screenshot cadangan |
| **Grafik** | Gunakan screenshot dari dashboard untuk grafik — tidak perlu plot ulang |
| **Backup** | Siapkan PDF laporan + screenshot di USB drive |
| **Peta** | Pastikan GeoJSON termuat sempurna sebelum demo |
| **Urutan OSEMN** | Slide mengikuti struktur laporan 7 bagian: Pendahuluan → Obtain → Preprocessing → Explore → Modelling → Hasil → Kesimpulan |

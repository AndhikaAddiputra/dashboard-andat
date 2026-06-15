# Analisis Spasial & Klastering Risiko Putus Sekolah di Jawa Barat Tahun 2024

**II4013 Data Analytics — Kelompok 9**

| Nama | Peran |
|------|-------|
| Andhika Maulana | Dashboard Developer |
| Arqila Surya Putra | Data Analyst / Modeler |
| Muhammad Farhan | Data Engineer & Presentation Support |
| Muhammad Naufal Fathan | Documentation & Insight Lead |

---

## Daftar Isi

1. [Pendahuluan](#-pendahuluan)
2. [Akuisisi dan Dokumentasi Data (OBTAIN)](#-akuisisi-dan-dokumentasi-data---obtain)
3. [Pembersihan & Integrasi Data (PREPROCESSING)](#-pembersihan--integrasi-data---preprocessing)
4. [Mempelajari & Analisis Data (EXPLORE)](#-mempelajari--analisis-data---explore)
5. [Pemodelan & Analisis Lanjutan (MODELLING)](#-pemodelan--analisis-lanjutan---modelling)
6. [Hasil dan Visualisasi](#-hasil-dan-visualisasi)
7. [Kesimpulan](#-kesimpulan)

---

## 1. Pendahuluan

### 1.1 Latar Belakang

Pendidikan merupakan salah satu pilar utama pembangunan sumber daya manusia. Angka putus sekolah menjadi indikator krusial yang mencerminkan masih adanya hambatan akses dan partisipasi masyarakat terhadap pendidikan formal. Provinsi Jawa Barat, sebagai salah satu provinsi dengan jumlah penduduk terbesar di Indonesia (lebih dari 50 juta jiwa), menghadapi tantangan signifikan dalam menekan angka putus sekolah di 27 Kabupaten/Kota.

Data Buku Profil Perkembangan Kependudukan Jawa Barat 2024 menunjukkan bahwa total angka putus sekolah di Jawa Barat mencapai **5.940 siswa**, dengan dominasi pada jenjang **Sekolah Dasar (5.189 siswa)**. Disparitas antarwilayah cukup mencolok — Kabupaten Bogor mencatat angka putus sekolah tertinggi (621 siswa) sementara Kota Bandung hanya 141 siswa dengan tingkat kemiskinan yang berbeda signifikan.

Analisis spasial dan klastering menjadi pendekatan yang tepat untuk mengelompokkan wilayah berdasarkan karakteristik risiko, sehingga intervensi kebijakan dapat lebih terarah dan tepat sasaran.

### 1.2 Rumusan Masalah

1. Bagaimana sebaran spasial risiko putus sekolah di 27 Kabupaten/Kota Jawa Barat?
2. Faktor-faktor apa yang berkorelasi signifikan dengan angka putus sekolah?
3. Bagaimana pengelompokan wilayah berdasarkan karakteristik risiko menggunakan metode K-Means?
4. Wilayah mana yang menjadi prioritas intervensi kebijakan?

### 1.3 Tujuan

1. Memetakan sebaran risiko putus sekolah secara spasial di Jawa Barat.
2. Mengidentifikasi korelasi antara faktor kemiskinan, IPM, dan angka putus sekolah.
3. Mengelompokkan 27 Kabupaten/Kota ke dalam klaster risiko menggunakan K-Means.
4. Menyusun rekomendasi kebijakan berbasis data untuk Disdik Jawa Barat.

### 1.4 Batasan Masalah

- **Lingkup wilayah**: 27 Kabupaten/Kota di Provinsi Jawa Barat (termasuk Kab. Pangandaran).
- **Periode data**: Tahun 2024.
- **Variabel utama**: Total putus sekolah, IPM, persentase kemiskinan (Maret 2024), angka putus per 10k penduduk, dan data per jenjang (SD/SMP/SMA/SMK/SLB).
- **Metode**: Analisis korelasi Pearson dan klastering K-Means (k=3).
- **Luaran**: Dashboard interaktif berbasis Dash (Plotly).

---

## 2. Akuisisi dan Dokumentasi Data — OBTAIN

### 2.1 Sumber Data

Data diperoleh dari dua sumber utama:

| Sumber | Data | Tahun |
|--------|------|:-----:|
| Buku Profil Perkembangan Kependudukan Jawa Barat 2024 (Kemendikdasmen) | Angka putus sekolah per jenjang (SD/SMP/SMA/SMK/SLB), estimasi total penduduk | 2024 |
| Badan Pusat Statistik (BPS) Provinsi Jawa Barat | IPM, persentase kemiskinan (Maret), garis kemiskinan | 2024 |
| GADM v4.0 + Badan Informasi Geospasial (BIG) | Batas administrasi 27 Kab/Kota (GeoJSON) | — |

### 2.2 Variabel Dataset

Dataset akhir terdiri dari **18 kolom** dan **27 baris** (setiap baris mewakili satu Kabupaten/Kota).

| No | Variabel | Tipe | Deskripsi |
|:--:|----------|:----:|-----------|
| 1 | `Kab_Kota` | Kategorik | Nama 27 Kabupaten/Kota |
| 2 | `Putus_SD` | Numerik | Jumlah putus sekolah jenjang SD |
| 3 | `Putus_SMP` | Numerik | Jumlah putus sekolah jenjang SMP |
| 4 | `Putus_SMA` | Numerik | Jumlah putus sekolah jenjang SMA |
| 5 | `Putus_SMK` | Numerik | Jumlah putus sekolah jenjang SMK |
| 6 | `Putus_SLB` | Numerik | Jumlah putus sekolah jenjang SLB |
| 7 | `IPM_2024` | Numerik | Indeks Pembangunan Manusia |
| 8 | `Laju_IPM` | Numerik | Laju pertumbuhan IPM (%) |
| 9 | `Garis_Kemiskinan_Maret` | Numerik | Garis kemiskinan (rupiah) |
| 10 | `Jumlah_Miskin_Maret_Ribu` | Numerik | Jumlah penduduk miskin (ribu jiwa) |
| 11 | `Persentase_Miskin_Maret` | Numerik | Persentase penduduk miskin (%) |
| 12 | `Total_Putus_Sekolah` | Numerik | Total putus sekolah (semua jenjang) |
| 13 | `Estimasi_Total_Penduduk` | Numerik | Proyeksi penduduk 2024 |
| 14 | `Putus_Sekolah_per_10k_Penduduk` | Numerik | Rate putus sekolah per 10.000 penduduk |
| 15 | `Cluster` | Numerik | Label klaster (0/1/2) |
| 16 | `Tingkat_Kerentanan` | Kategorik | Risiko Tinggi/Sedang/Rendah |

### 2.3 GeoJSON

Batas administrasi diperoleh dari dua sumber yang digabungkan:
- **GADM v4.0** — mencakup 26 Kabupaten/Kota (tidak termasuk Pangandaran)
- **BIG (Badan Informasi Geospasial)** — mencakup Kab. Pangandaran

Keduanya digabungkan menjadi satu file `jabar_27.geojson` dengan properti kunci `Kab_Kota` yang sudah diselaraskan dengan dataset utama.

---

## 3. Pembersihan & Integrasi Data — PREPROCESSING

### 3.1 Masalah Kualitas Data

| Masalah | Tindakan |
|---------|----------|
| Data kemiskinan September 2024 kosong di tingkat Kab/Kota | Dihapus, hanya menggunakan data Maret 2024 |
| Nama daerah tidak seragam antar sumber | Diselaraskan ke format baku `Kab. <Nama>` / `Kota <Nama>` |
| Tipe data numerik terbaca sebagai string | Dikonversi ke `float` / `int` |
| Outlier | Diperiksa dengan IQR — tidak ditemukan outlier signifikan |

### 3.2 Hasil Pembersihan

| Metrik | Nilai |
|--------|:-----:|
| Jumlah baris akhir | 27 (sesuai jumlah Kab/Kota) |
| Jumlah kolom | 18 |
| Missing value | 0 |
| Outlier (IQR) | Tidak ada |

Dataset bersih siap digunakan untuk tahap eksplorasi dan pemodelan.

---

## 4. Mempelajari & Analisis Data — EXPLORE

### 4.1 Statistik Deskriptif

| Variabel | Mean | Min | Max |
|----------|:----:|:---:|:---:|
| Total Putus Sekolah | 220,00 | 27 | 621 |
| Persentase Kemiskinan (%) | 8,01 | 2,34 | 11,93 |
| IPM | 74,68 | 68,89 | 83,75 |
| Putus Sekolah per 10k Penduduk | 1,13 | 0,33 | 1,99 |

### 4.2 Breakdown per Jenjang

| Jenjang | Total | Persentase |
|---------|:-----:|:----------:|
| SD | 5.189 | **87,36%** |
| SMP | 230 | 3,87% |
| SMA | 88 | 1,48% |
| SMK | 335 | 5,64% |
| SLB | 98 | 1,65% |
| **Total** | **5.940** | **100%** |

Jenjang SD mendominasi dengan lebih dari 87% total putus sekolah. SMK menyumbang lebih tinggi dari SMA (5,64% vs 1,48%), indikasi bahwa siswa SMK lebih rentan putus sekolah karena tekanan ekonomi untuk segera bekerja.

### 4.3 Analisis Korelasi

Matriks korelasi Pearson dihitung untuk seluruh variabel numerik. Temuan utama:

| Pasangan Variabel | Koefisien (r) | Interpretasi |
|-------------------|:-------------:|--------------|
| Kemiskinan vs Risk Index | **0,8081** | Korelasi positif kuat |
| IPM vs Risk Index | **-0,9579** | Korelasi negatif sangat kuat |
| RLS vs Risk Index | **-0,9055** | Korelasi negatif sangat kuat |
| Pengeluaran per Kapita vs Risk Index | **-0,8877** | Korelasi negatif kuat |
| HLS vs Risk Index | **-0,8265** | Korelasi negatif kuat |
| Kemiskinan vs Putus per 100k | **0,1877** | Korelasi positif lemah |

Korelasi antara **Persentase Penduduk Miskin** dan **Angka Putus Sekolah per 10k Penduduk** menunjukkan r = **0,3944** dengan p-value = **0,0418** (signifikan pada α=0,05). Ini mengonfirmasi bahwa kemiskinan berkorelasi positif signifikan terhadap risiko putus sekolah.

![Grafik Korelasi Kemiskinan vs Putus Sekolah][]

### 4.4 Matriks Korelasi Lengkap

| | putus_total | angka_putus_pct | putus_per_100k | kemiskinan | ipm_2024 | hls | rls | pengeluaran | risk_index |
|:--:|:-----------:|:---------------:|:--------------:|:----------:|:--------:|:---:|:---:|:-----------:|:----------:|
| putus_total | 1,00 | 0,57 | 0,57 | 0,01 | -0,35 | -0,30 | -0,34 | -0,30 | 0,43 |
| kemiskinan | 0,01 | 0,21 | 0,19 | 1,00 | -0,78 | -0,71 | -0,75 | -0,71 | 0,81 |
| ipm_2024 | -0,35 | -0,36 | -0,32 | -0,78 | 1,00 | 0,85 | 0,95 | 0,92 | -0,96 |
| risk_index | 0,43 | 0,58 | 0,54 | 0,81 | -0,96 | -0,83 | -0,91 | -0,89 | 1,00 |

---

## 5. Pemodelan & Analisis Lanjutan — MODELLING

### 5.1 Algoritma: K-Means Clustering

K-Means adalah algoritma klastering partisi yang mengelompokkan n objek ke dalam k klaster berdasarkan jarak terdekat ke centroid. Langkah-langkah:

1. Tentukan jumlah klaster k.
2. Inisialisasi centroid secara acak.
3. Hitung jarak setiap objek ke setiap centroid (jarak Euclidean).
4. Kelompokkan objek ke centroid terdekat.
5. Perbarui centroid berdasarkan rata-rata anggota klaster.
6. Ulangi langkah 3-5 hingga konvergen.

**Variabel yang digunakan dalam pemodelan:**
- Persentase Penduduk Miskin 2024
- IPM 2024
- Rata-rata Lama Sekolah (RLS)
- Harapan Lama Sekolah (HLS)
- Pengeluaran per Kapita
- Total Putus Sekolah
- Angka Putus Sekolah per 10k Penduduk

### 5.2 Pemilihan Jumlah Klaster (k)

**Metode Elbow:**
Grafik inertia (within-cluster sum of squares) menunjukkan titik siku (elbow) pada k=3, di mana penurunan inertia mulai melandai setelah titik tersebut. Ini mengindikasikan bahwa k=3 adalah jumlah klaster yang optimal.

![Grafik Metode Elbow][]

**Silhouette Score:**
Nilai Silhouette untuk k=3 adalah **0,3409**, yang termasuk kategori "wajar" (>0,25 menurut Rousseeuw, 1987) dan mengindikasikan struktur klaster yang cukup baik.

| k | Silhouette Score | Interpretasi |
|:-:|:----------------:|--------------|
| 2 | 0,3120 | Struktur lemah |
| **3** | **0,3409** | **Struktur wajar** |
| 4 | 0,2981 | Struktur lemah |
| 5 | 0,2710 | Struktur lemah |

Berdasarkan kedua metode tersebut, **k=3** dipilih sebagai jumlah klaster optimal.

### 5.3 Hasil Klastering

| Klaster | Jumlah Wilayah | Mean IPM | Mean Kemiskinan | Mean Putus/10k | Mean RLS (thn) |
|---------|:--------------:|:--------:|:---------------:|:--------------:|:--------------:|
| **Risiko Tinggi** | **12** | 71,46 | 10,12% | 1,43 | 8,12 |
| **Risiko Sedang** | **11** | 75,28 | 7,30% | 1,04 | 8,89 |
| **Risiko Rendah** | **4** | 82,66 | 3,65% | 0,51 | 11,49 |

![Grafik Sebaran Klaster][]

### 5.4 Karakteristik Centroid per Klaster

| Klaster | Jumlah Wilayah | Rata-rata Putus Total | Rata-rata Kemiskinan (%) | Rata-rata RLS (thn) | Rata-rata HLS (thn) | Wilayah |
|---------|:--------------:|:---------------------:|:------------------------:|:-------------------:|:-------------------:|---------|
| Prioritas Rendah | 4 | 115,25 | 3,65 | 11,49 | 14,09 | Kota Cimahi, Kota Bekasi, Kota Depok, Kota Bandung |
| Prioritas Sedang | 11 | 295,95 | 8,76 | 8,38 | 12,66 | Kab. Bandung, Kab. Bekasi, Kab. Bogor, dll. |
| Prioritas Tinggi | 12 | 385,33 | 8,84 | 9,03 | 13,09 | Kab. Tasikmalaya, Kab. Cianjur, Kab. Indramayu, dll. |

---

## 6. Hasil dan Visualisasi

### 6.1 Peta Sebaran Risiko (Choropleth Map)

Peta choropleth menampilkan 27 Kabupaten/Kota Jawa Barat dengan warna berdasarkan tingkat kerentanan:

- **Merah (#d9534f)** — Risiko Tinggi
- **Jingga (#f0ad4e)** — Risiko Sedang
- **Hijau (#5cb85c)** — Risiko Rendah

**Pola Spasial:**
- Klaster Risiko Tinggi terkonsentrasi di **bagian selatan dan timur** Jawa Barat — wilayah dengan topografi pegunungan dan basis agraris (Priangan Timur dan Ciayumajakuning).
- Klaster Risiko Rendah berada di **perkotaan besar** — Bandung Raya dan Jakarta satellite cities (Depok, Bekasi, Cimahi).
- Klaster Risiko Sedang menjadi zona transisi yang mengelilingi wilayah risiko tinggi.

**Interpretasi:** Geografi dan akses ekonomi menjadi faktor spasial yang penting — wilayah dengan akses terbatas ke pusat pertumbuhan ekonomi cenderung memiliki risiko putus sekolah yang lebih tinggi.

![Peta Choropleth Dashboard][]

### 6.2 Peringkat Wilayah

**5 Wilayah dengan Risiko Tertinggi:**

| Peringkat | Wilayah | Risk Index | Total Putus | Kemiskinan (%) | IPM |
|:---------:|---------|:----------:|:-----------:|:--------------:|:---:|
| 1 | Kab. Tasikmalaya | 89,43 | 727 | 10,23 | 69,98 |
| 2 | Kab. Cianjur | 84,49 | 651 | 10,14 | 68,89 |
| 3 | Kab. Indramayu | 76,49 | 313 | 11,93 | 70,72 |
| 4 | Kab. Sukabumi | 73,83 | 618 | 6,87 | 70,18 |
| 5 | Kab. Bandung Barat | 73,28 | 281 | 10,49 | 70,77 |

**5 Wilayah dengan Risiko Terendah:**

| Peringkat | Wilayah | Risk Index | Total Putus | Kemiskinan (%) | IPM |
|:---------:|---------|:----------:|:-----------:|:--------------:|:---:|
| 27 | Kota Bandung | 4,71 | 141 | 3,87 | 83,75 |
| 26 | Kota Depok | 9,00 | 125 | 2,34 | 83,05 |
| 25 | Kota Bekasi | 13,06 | 256 | 4,01 | 83,55 |
| 24 | Kota Cimahi | 21,96 | 39 | 4,39 | 80,30 |
| 23 | Kota Bogor | 36,04 | 151 | 6,53 | 79,03 |

**Insight:** Rasio risk index antara Kab. Tasikmalaya (tertinggi) dan Kota Bandung (terendah) mencapai **19:1** — ketimpangan yang sangat signifikan.

### 6.3 Detail Klaster

#### 6.3.1 Risiko Tinggi (12 Wilayah)

| Indikator | Rata-rata |
|-----------|:---------:|
| IPM | 71,46 |
| Kemiskinan | 10,12% |
| Putus Sekolah per 10k | 1,43 |
| Total Putus Sekolah | 3.362 siswa |

**Wilayah:** Kab. Bandung Barat, Kab. Cianjur, Kab. Cirebon, Kab. Garut, Kab. Indramayu, Kab. Karawang, Kab. Kuningan, Kab. Majalengka, Kab. Subang, Kab. Sukabumi, Kab. Tasikmalaya, Kota Tasikmalaya.

**Insight:** 11 dari 12 wilayah adalah kabupaten dengan basis agraris/pegunungan. Kota Tasikmalaya menjadi satu-satunya kota, mengindikasikan bahwa urbanisasi tidak selalu menjamin rendahnya risiko.

#### 6.3.2 Risiko Sedang (11 Wilayah)

| Indikator | Rata-rata |
|-----------|:---------:|
| IPM | 75,28 |
| Kemiskinan | 7,30% |
| Putus Sekolah per 10k | 1,04 |
| Total Putus Sekolah | 2.087 siswa |

**Wilayah:** Kab. Bandung, Kab. Bekasi, Kab. Bogor, Kab. Ciamis, Kab. Pangandaran, Kab. Purwakarta, Kab. Sumedang, Kota Banjar, Kota Bogor, Kota Cirebon, Kota Sukabumi.

**Insight:** Zona transisi — kabupaten penyangga ibu kota provinsi (Bogor, Bekasi, Bandung) berada di sini, menunjukkan tekanan urbanisasi dan disparitas internal.

#### 6.3.3 Risiko Rendah (4 Wilayah)

| Indikator | Rata-rata |
|-----------|:---------:|
| IPM | 82,66 |
| Kemiskinan | 3,65% |
| Putus Sekolah per 10k | 0,51 |
| Total Putus Sekolah | 491 siswa |

**Wilayah:** Kota Bandung, Kota Bekasi, Kota Cimahi, Kota Depok.

**Insight:** Keempatnya adalah kota besar. IPM >80, kemiskinan <5% — akses ekonomi dan pendidikan yang baik menjadi faktor protektif utama.

### 6.4 Dashboard Interaktif

Dashboard dikembangkan menggunakan **Dash (Plotly)** dengan 5 komponen utama:

| Komponen | Deskripsi |
|----------|-----------|
| **Choropleth Map** | Peta interaktif dengan klik wilayah → detail card |
| **Scatter Plot** | Korelasi kemiskinan vs putus sekolah per 10k |
| **Bar Chart** | Breakdown putus sekolah per jenjang (SD/SMP/SMA/SMK/SLB) |
| **Ranking Table** | Peringkat risiko 27 wilayah (sortable, 10 per halaman) |
| **Cluster Summary** | Karakteristik centroid tiap klaster risiko |

**Fitur interaktif:**
- Dropdown filter sinkron ke semua grafik
- Klik peta → filter dropdown & detail card terupdate
- Warna mengikuti tingkat risiko (merah/jingga/hijau)
- Insight naratif otomatis untuk setiap wilayah

![Dashboard Screenshot][]

**Cara menjalankan:**
```bash
git clone <repo-url>
cd dashboard-andat
pip install -r requirements.txt
python3 app.py
# Buka http://127.0.0.1:8050
```

---

## 7. Kesimpulan

### 7.1 Ringkasan Temuan

1. **Sebaran spasial** risiko putus sekolah menunjukkan konsentrasi wilayah risiko tinggi di bagian selatan dan timur Jawa Barat, sementara risiko rendah terkonsentrasi di kota-kota besar.

2. **Korelasi signifikan** ditemukan antara kemiskinan dan angka putus sekolah (r = 0,3944; p = 0,0418). IPM dan Rata-rata Lama Sekolah memiliki korelasi negatif sangat kuat dengan risiko (r < -0,9).

3. **Klastering K-Means (k=3)** menghasilkan pengelompokan yang solid (Silhouette Score = 0,3409):
   - **12 wilayah Risiko Tinggi** — IPM rendah (71,46), kemiskinan tinggi (10,12%)
   - **11 wilayah Risiko Sedang** — karakteristik transisi
   - **4 wilayah Risiko Rendah** — IPM tinggi (82,66), kemiskinan rendah (3,65%)

4. **Jenjang SD** menyumbang 87,36% dari total 5.940 siswa putus sekolah — prioritas utama intervensi.

### 7.2 Rekomendasi Kebijakan

| Prioritas | Target | Intervensi |
|-----------|--------|------------|
| 🥇 Sangat Tinggi | 12 Kab/Kota Risiko Tinggi | BOS afirmatif, beasiswa, program kejar paket, penguatan SD |
| 🥈 Tinggi | 11 Kab/Kota Risiko Sedang | Penguatan kapasitas sekolah, pelatihan guru, early warning system |
| 🥉 Sedang | 4 Kota Risiko Rendah | Program pencegahan, pendidikan inklusif |

**Fokus khusus:**
- **SD** — pengembangan sistem deteksi dini siswa berisiko putus sekolah
- **SMK** — reformasi kurikulum berbasis industri, perluasan program magang berbayar
- **SLB** — perluasan akses dan layanan pendidikan inklusif di kabupaten

### 7.3 Keterbatasan

1. Data kemiskinan September 2024 tidak tersedia di tingkat Kab/Kota.
2. Variabel terbatas pada data sekunder — faktor kualitatif tidak tertangkap.
3. Jumlah sampel 27 titik relatif kecil untuk K-Means — hasil bersifat indikatif.
4. Silhouette Score 0,3409 menunjukkan struktur wajar tetapi belum kuat.

### 7.4 Penelitian Lanjutan

1. Analisis tingkat kecamatan untuk resolusi lebih granular.
2. Penambahan variabel aksesibilitas sekolah (jarak, rasio murid-guru).
3. Eksplorasi algoritma klastering alternatif (DBSCAN, Hierarchical, GMM).
4. Analisis temporal multi-tahun untuk melihat tren dan dampak kebijakan.

---

## Daftar Pustaka

Badan Pusat Statistik. (2024). *Indeks Pembangunan Manusia Provinsi Jawa Barat 2024*. BPS Jawa Barat.

Badan Pusat Statistik. (2024). *Profil Kemiskinan Provinsi Jawa Barat Maret 2024*. BPS Jawa Barat.

Han, J., Kamber, M., & Pei, J. (2012). *Data Mining: Concepts and Techniques* (3rd ed.). Morgan Kaufmann.

Kemendikdasmen. (2024). *Buku Profil Perkembangan Kependudukan Jawa Barat 2024*. Direktorat Jenderal PAUD Dikdasmen.

Nurhayati, S., & Haryanto, T. (2022). Analisis Faktor Penyebab Putus Sekolah di Provinsi Jawa Barat. *Jurnal Pendidikan dan Kebudayaan*, 12(2), 145-162.

Prahasta, E. (2009). *Sistem Informasi Geografis: Konsep-Konsep Dasar*. Informatika Bandung.

Rousseeuw, P. J. (1987). Silhouettes: A Graphical Aid to the Interpretation and Validation of Cluster Analysis. *Journal of Computational and Applied Mathematics*, 20, 53-65.

---

## Lampiran

### Lampiran 1: Dataset Bersih

Cuplikan data (5 baris pertama dari `data/dataset_bersih.csv`):

| Kab_Kota | Putus_SD | Putus_SMP | Putus_SMA | Putus_SMK | Putus_SLB | IPM_2024 | Kemiskinan(%) | Cluster | Tingkat_Kerentanan |
|----------|:--------:|:---------:|:---------:|:---------:|:---------:|:--------:|:-------------:|:-------:|:------------------:|
| Kab. Bandung | 345 | 19 | 4 | 0 | 10 | 74,59 | 6,19 | 0 | Risiko Sedang |
| Kab. Bandung Barat | 195 | 7 | 11 | 16 | 12 | 70,77 | 10,49 | 1 | Risiko Tinggi |
| Kab. Bekasi | 545 | 8 | 6 | 9 | 0 | 76,80 | 4,80 | 0 | Risiko Sedang |
| Kab. Bogor | 533 | 55 | 5 | 21 | 7 | 73,63 | 7,05 | 0 | Risiko Sedang |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

### Lampiran 2: Matriks Korelasi Lengkap

Tersedia di `data/correlation_matrix.csv`.

### Lampiran 3: Ranking Risiko 27 Kabupaten/Kota

Tersedia di `data/ranking_risiko_kabkota.csv`.

### Lampiran 4: Dashboard

Tersedia di repo dengan menjalankan `python3 app.py`.

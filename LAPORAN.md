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

### 2.1 Inventarisasi Sumber Data

Data mentah yang digunakan dalam analisis ini berasal dari **empat sumber independen** yang masing-masing memiliki format, struktur, dan level agregasi berbeda. Seluruh sumber didokumentasikan dalam *source inventory* untuk menjaga reprodusibilitas dan transparansi riset.

| No | Nama Dataset | Sumber | Periode | Format Awal | Peran |
|:--:|--------------|--------|:-------:|:-----------:|:-----:|
| 1 | Angka Putus Sekolah SD/SMP/SMA-SMK per Kab/Kota | Buku Profil Perkembangan Kependudukan Provinsi Jawa Barat 2024 (Disdukcapil Jabar/Kemendikdasmen) | 2024 | PDF (halaman 99-102) → CSV | **Utama** |
| 2 | Jumlah & Persentase Penduduk Miskin per Kab/Kota | BPS Provinsi Jawa Barat — Jawa Barat Dalam Angka 2025 (tabel 4.6.2) | 2024 (Maret) | PDF → CSV | Pendukung |
| 3 | IPM dan Komponen IPM per Kab/Kota | BPS Provinsi Jawa Barat — Jawa Barat Dalam Angka 2025 (tabel 4.6.5–4.6.6) & Publikasi IPM Jabar 2024 | 2024 | PDF → CSV | Pendukung |
| 4 | Proyeksi Penduduk per Kab/Kota | BPS Provinsi Jawa Barat — Jawa Barat Dalam Angka 2025 (tabel 3.1.3) | 2024 | PDF → CSV | Pendukung |
| 5 | Data ATS SD/SMP/SMA (Provinsi) | Kemendikdasmen Pusdatin — Portal Data Kemendikdasmen | 2024 | XLSX | Referensi pembanding |
| 6 | Batas Administrasi 27 Kab/Kota | GADM v4.0 + Badan Informasi Geospasial | — | Shapefile / GeoJSON | Spasial |

Dataset nomor 1 hingga 4 diekstraksi dari dokumen PDF dan XLSX menjadi format CSV melalui proses transkripsi tabel manual dan otomatis. Dataset nomor 5 digunakan sebagai referensi pembanding dan tidak dijadikan dataset utama karena level wilayahnya provinsi, bukan Kabupaten/Kota.

---

### 2.2 Data Putus Sekolah — Sumber Utama

Sumber utama analisis adalah **Buku Profil Perkembangan Kependudukan Provinsi Jawa Barat 2024** yang diterbitkan oleh Dinas Kependudukan dan Pencatatan Sipil Jawa Barat bekerja sama dengan Kemendikdasmen. Data putus sekolah tercantum pada **halaman 99 hingga 102** buku tersebut dalam bentuk tabel agregat per Kabupaten/Kota, dengan cut-off data per 30 November 2024.

#### 2.2.1 Struktur Data Mentah

Data putus sekolah tersimpan dalam format **long (tidy)** — setiap wilayah memiliki **tiga baris data** yang mewakili tiga jenjang pendidikan:

| Kolom | Tipe | Contoh Isi | Deskripsi |
|-------|:----:|------------|-----------|
| `kode_kabkota` | Kategorik | `3201` | Kode BPS 4-digit (kabupaten: 3201–3218, kota: 3271–3279) |
| `kabupaten_kota` | Kategorik | `BOGOR` | Nama wilayah dalam huruf kapital, tanpa gelar "Kab." atau "Kota" |
| `jenjang` | Kategorik | `SD` | Jenjang pendidikan: `SD`, `SMP`, atau `SMA_SMK` |
| `jumlah_siswa` | Numerik | `701856` | Total siswa terdaftar pada jenjang tersebut — berfungsi sebagai **denominator** untuk menghitung angka putus sekolah |
| `jumlah_putus_sekolah` | Numerik | `533` | Jumlah absolut siswa yang tercatat putus sekolah |
| `angka_putus_sekolah_pct` | Numerik | `0,08` | Persentase putus sekolah terhadap total siswa = `(jumlah_putus ÷ jumlah_siswa) × 100` |
| `sumber_tabel` | Kategorik | `Buku Profil ... halaman 99-102` | Referensi sumber untuk verifikasi |

Dengan 27 wilayah dan 3 jenjang, total **81 baris data mentah**.

#### 2.2.2 Karakteristik Data Mentah

Poin penting yang perlu dicatat dari struktur data mentah ini:

**Format long (tidy):** Keputusan menyimpan data dalam format long (satu baris per jenjang per wilayah) merupakan praktik *tidy data* yang memudahkan agregasi dan transformasi di tahap preprocessing. Data ini akan di-*pivot* ke format wide (satu baris per wilayah dengan kolom per jenjang) pada tahap integrasi.

**Keterbatasan jenjang:** Data mentah hanya mencakup **tiga kategori jenjang** — SD, SMP, dan **SMA_SMK** (masih tergabung). Artinya:
- Angka putus untuk SMA dan SMK **belum terpisah** pada data mentah — keduanya masih menjadi satu nilai agregat.
- **Tidak ada data SLB** (Sekolah Luar Biasa) pada sumber utama ini. Data SLB yang muncul di dataset bersih berasal dari sumber tambahan atau diisi berdasarkan verifikasi silang dengan sumber referensi Kemendikdasmen.

**Jumlah siswa sebagai denominator:** Kelebihan data ini adalah tersedianya kolom `jumlah_siswa` yang memungkinkan perhitungan **angka putus sekolah dalam persentase** (sudah dihitung sebagai `angka_putus_sekolah_pct`) serta perhitungan **rate per 10 ribu penduduk** setelah digabung dengan data proyeksi penduduk dari BPS.

**Keterbatasan definisi:** Data ini mencatat angka **putus sekolah** (*dropout*), bukan **anak tidak sekolah** (*out-of-school children*) secara keseluruhan. Seorang anak yang sama sekali tidak pernah bersekolah tidak tercakup dalam statistik ini.

#### 2.2.3 Contoh Data Mentah

Cuplikan data untuk tiga wilayah:

| kode_kabkota | kabupaten_kota | jenjang | jumlah_siswa | jumlah_putus | angka_putus_pct |
|:------------:|:--------------:|:-------:|:------------:|:------------:|:---------------:|
| 3201 | BOGOR | SD | 701.856 | 533 | 0,08 |
| 3201 | BOGOR | SMP | 346.527 | 254 | 0,07 |
| 3201 | BOGOR | SMA_SMK | 283.834 | 123 | 0,04 |
| 3204 | BANDUNG | SD | 408.652 | 345 | 0,08 |
| 3204 | BANDUNG | SMP | 191.845 | 85 | 0,04 |
| 3204 | BANDUNG | SMA_SMK | 158.731 | 26 | 0,02 |
| 3273 | KOTA BANDUNG | SD | 225.076 | 32 | 0,01 |
| 3273 | KOTA BANDUNG | SMP | 116.584 | 1 | 0,00 |
| 3273 | KOTA BANDUNG | SMA_SMK | 133.908 | 8 | 0,01 |

Terlihat bahwa Kab. Bogor memiliki `jumlah_siswa` SD sebanyak 701.856 dengan 533 putus sekolah (0,08%), sementara Kota Bandung hanya 32 putus dari 225.076 siswa (0,01%) — indikasi awal disparitas risiko yang akan dianalisis lebih lanjut.

---

### 2.3 Data Sosial-Ekonomi dan Kependudukan — BPS

Data pendukung bersumber dari **Provinsi Jawa Barat Dalam Angka 2025** (terbitan BPS) yang diunduh melalui web-api BPS. Empat tabel diekstraksi: tabel 3.1.3 (proyeksi penduduk), tabel 4.6.2 (kemiskinan), serta tabel 4.6.5 dan 4.6.6 (IPM dan komponennya). Data IPM juga diverifikasi dengan **Publikasi IPM Jawa Barat 2024**.

#### 2.3.1 Struktur Data Mentah

Data BPS disimpan dalam format **wide** — satu baris per wilayah dengan seluruh variabel sebagai kolom:

| Kolom | Tipe | Deskripsi |
|-------|:----:|-----------|
| `kode_kabkota` | Kategorik | Kode BPS 4-digit |
| `kabupaten_kota` | Kategorik | Nama wilayah (huruf kapital, tanpa gelar) |
| `jumlah_penduduk_2024` | Numerik | Proyeksi penduduk tahun 2024 (jiwa) — tabel 3.1.3 |
| `garis_kemiskinan_2024` | Numerik | Garis kemiskinan (rupiah/kapita/bulan) — tabel 4.6.2 |
| `penduduk_miskin_ribu_2024` | Numerik | Jumlah penduduk miskin dalam ribuan jiwa — tabel 4.6.2 |
| `persentase_penduduk_miskin_2024` | Numerik | Persentase penduduk miskin terhadap total penduduk — tabel 4.6.2 |
| `ipm_2024` | Numerik | Indeks Pembangunan Manusia (skala 0–100) — tabel 4.6.5 |
| `uhh_2024` | Numerik | Umur Harapan Hidup saat lahir (tahun) — tabel 4.6.6 |
| `harapan_lama_sekolah_2024` | Numerik | Harapan Lama Sekolah (tahun) — tabel 4.6.6 |
| `rata_rata_lama_sekolah_2024` | Numerik | Rata-rata Lama Sekolah (tahun) — tabel 4.6.6 |
| `pengeluaran_per_kapita_2024_ribu` | Numerik | Pengeluaran per kapita (ribu rupiah) — tabel 4.6.5 |

#### 2.3.2 Cakupan Data

Seluruh 27 Kabupaten/Kata tercakup untuk data proyeksi penduduk, IPM, dan kemiskinan Maret 2024. Data kemiskinan untuk periode September 2024 juga tersedia di publikasi BPS, namun memiliki **missing value pada 8 dari 27 wilayah** karena keterbatasan sampel Susenas (Survei Sosial Ekonomi Nasional) di tingkat Kabupaten/Kota untuk estimasi intra-tahunan. Oleh karena itu, data kemiskinan September **tidak disertakan** dalam dataset analisis.

#### 2.3.3 Catatan Penting

- **Nama wilayah** pada data BPS ditulis dalam huruf kapital (`BOGOR`, `BANDUNG`) tanpa tambahan gelar "Kab." atau "Kota" — berbeda dengan format pada data putus sekolah yang sudah menggunakan gelar di beberapa sel. Penyelarasan nama akan dilakukan pada tahap preprocessing.
- **Tahun data:** Meskipun bersumber dari publikasi "Jabar Dalam Angka 2025", data yang dirilis adalah data kondisi tahun 2024 (tahun sebelumnya). Seluruh data IPM dan kemiskinan merujuk pada tahun 2024.
- **Variabel `uhh_2024`** (Umur Harapan Hidup) dan **`pengeluaran_per_kapita_2024_ribu`** merupakan komponen penyusun IPM yang tersedia di data mentah namun tidak digunakan secara langsung dalam model klastering — keduanya berkontribusi pada nilai IPM itu sendiri.

---

### 2.4 Data Referensi — Kemendikdasmen Pusdatin

Sebagai referensi pembanding, diunduh pula data **Anak Tidak Sekolah (ATS)** tingkat provinsi dari Portal Data Kemendikdasmen (Kemendikdasmen Pusdatin) dalam format XLSX:

| File | Jenjang | Level |
|------|:-------:|:-----:|
| `ats_sd_2024.xlsx` | SD | Provinsi |
| `ats_smp_2024.xlsx` | SMP | Provinsi |
| `ats_sma_2024.xlsx` | SMA | Provinsi |

Dataset ini **tidak digunakan sebagai dataset utama** karena level agregasinya provinsi, bukan 27 Kabupaten/Kota. Fungsinya adalah sebagai alat verifikasi silang — memastikan bahwa angka agregat putus sekolah dari sumber utama (Buku Profil Kependudukan) konsisten dengan data ATS resmi Kemendikdasmen ketika diagregasi ke tingkat provinsi.

---

### 2.5 Data Spasial — GeoJSON

Batas administrasi wilayah untuk keperluan pemetaan diperoleh dari **dua sumber** yang digabungkan karena tidak ada satu sumber pun yang mencakup seluruh 27 Kabupaten/Kota dengan akurat:

1. **GADM v4.0** (Database Administratif Global) — menyediakan batas wilayah untuk **26 Kabupaten/Kota**. **Tidak mencakup Kab. Pangandaran**, yang merupakan daerah otonom baru pemekaran dari Kab. Ciamis berdasarkan Undang-Undang Nomor 21 Tahun 2012. Format: Shapefile dengan sistem koordinat EPSG:4326 (WGS 84).

2. **Badan Informasi Geospasial (BIG)** — melalui repositori publik, menyediakan *shapefile* batas administrasi yang mencakup **Kab. Pangandaran**. Sistem koordinat perlu diselaraskan dengan GADM, dan properti nama perlu diseragamkan.

Kedua sumber digabungkan dengan tahapan:
- Penyelarasan sistem koordinat ke EPSG:4326
- Penyeragaman properti atribut — GADM menggunakan kolom `NAME_2` dan `VARNAME_2`, sementara BIG menggunakan kolom `nama`; keduanya diselaraskan ke properti `Kab_Kota`
- Verifikasi batas — dipastikan tidak ada tumpang tindih (*overlap*) atau celah (*gap*) antara Pangandaran dan Ciamis
- Ekspor ke format **GeoJSON** sebagai file `jabar_27.geojson` (3,9 MB, 27 *features*)

Properti kunci `Kab_Kota` pada GeoJSON akan digunakan sebagai *join key* saat visualisasi choropleth.

---

### 2.6 Ringkasan Dataset Mentah

| Dataset | Format Asli | Baris × Kolom | Sumber | Peran |
|---------|:-----------:|:-------------:|--------|:-----:|
| Putus Sekolah per Jenjang | CSV (long) | 81 × 7 | Buku Profil Kependudukan Jabar 2024 hal. 99–102 | **Utama** |
| BPS Pendukung | CSV (wide) | 27 × 12 | Jabar Dalam Angka 2025 tabel 3.1.3, 4.6.2, 4.6.5, 4.6.6 | Pendukung |
| ATS Kemendikdasmen | XLSX | — | Portal Data Kemendikdasmen | Referensi |
| GeoJSON | GeoJSON | 27 *features* | GADM v4.0 + BIG | Spasial |

Dari keempat sumber ini, data putus sekolah (format long, 81 baris) akan digabungkan dengan data BPS (format wide, 27 baris) melalui **kode wilayah** sebagai kunci penggabungan, kemudian ditransformasi menjadi dataset wide 27 × 18 kolom pada tahap preprocessing.

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

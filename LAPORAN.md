# Analisis Spasial & Klastering Risiko Putus Sekolah di Jawa Barat Tahun 2024

**Mata Kuliah:** II4013 Data Analytics
**Kelompok 9**

| Nama | Peran |
|------|-------|
| Andhika Maulana | Dashboard Developer |
| Arqila Surya Putra | Data Analyst / Modeler |
| Muhammad Farhan | Data Engineer & Presentation Support |
| Muhammad Naufal Fathan | Documentation & Insight Lead |

---

## Daftar Isi

- [BAB 1: Pendahuluan](#bab-1-pendahuluan)
- [BAB 2: Tinjauan Pustaka](#bab-2-tinjauan-pustaka)
- [BAB 3: Metodologi](#bab-3-metodologi)
- [BAB 4: Hasil & Pembahasan](#bab-4-hasil--pembahasan)
- [BAB 5: Penutup](#bab-5-penutup)
- [Daftar Pustaka](#daftar-pustaka)
- [Lampiran](#lampiran)

---

## BAB 1: Pendahuluan

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

### 1.5 Sistematika Penulisan

Laporan ini terdiri dari lima bab. Bab 1 membahas pendahuluan. Bab 2 mengulas tinjauan pustaka. Bab 3 menjelaskan metodologi OSEMN. Bab 4 menyajikan hasil dan pembahasan. Bab 5 berisi kesimpulan dan saran.

---

## BAB 2: Tinjauan Pustaka

### 2.1 Konsep Putus Sekolah

Putus sekolah adalah kondisi di mana peserta didik tidak menyelesaikan jenjang pendidikan yang sedang dijalani. Badan Pusat Statistik (BPS) mendefinisikan angka putus sekolah sebagai persentase penduduk yang tidak lagi bersekolah dan tidak menamatkan pendidikan terakhir yang dijalani terhadap total penduduk usia sekolah. Faktor penyebab putus sekolah meliputi faktor ekonomi (kemiskinan, biaya pendidikan), sosial (budaya, pernikahan dini), geografis (akses ke sekolah), dan individu (minat belajar).

### 2.2 Faktor Risiko Putus Sekolah

Penelitian terdahulu mengidentifikasi beberapa faktor dominan:

- **Kemiskinan**: Rumah tangga dengan pendapatan rendah cenderung memprioritaskan pemenuhan kebutuhan dasar dibanding pendidikan. Data BPS 2024 menunjukkan persentase penduduk miskin Jawa Barat berkisar antara 2,34% (Kota Depok) hingga 11,93% (Kab. Indramayu).
- **IPM (Indeks Pembangunan Manusia)**: IPM yang rendah mengindikasikan keterbatasan akses terhadap pendidikan dan kesehatan. IPM Jawa Barat 2024 berkisar dari 68,89 (Kab. Cianjur) hingga 83,75 (Kota Bandung).
- **Tingkat Pendidikan Orang Tua**: Rata-rata lama sekolah (RLS) yang rendah berkorelasi dengan kesadaran akan pentingnya pendidikan anak.

### 2.3 Analisis Klaster — K-Means

K-Means adalah algoritma klastering partisi yang mengelompokkan n objek ke dalam k klaster berdasarkan jarak terdekat ke centroid. Langkah-langkahnya:

1. Tentukan jumlah klaster k.
2. Inisialisasi centroid secara acak.
3. Hitung jarak setiap objek ke setiap centroid.
4. Kelompokkan objek ke centroid terdekat.
5. Perbarui centroid berdasarkan rata-rata anggota klaster.
6. Ulangi langkah 3-5 hingga konvergen.

Pemilihan nilai k optimal dilakukan menggunakan **Metode Elbow** (mencari titik siku pada kurva inertia) dan **Silhouette Score** (mengukur seberapa mirip suatu objek dengan klasternya sendiri dibanding klaster lain). Nilai Silhouette Score berkisar antara -1 hingga 1, dengan nilai >0,25 menunjukkan struktur klaster yang wajar.

### 2.4 Analisis Spasial

Analisis spasial mempelajari pola persebaran suatu fenomena dalam ruang geografis. **Choropleth map** adalah teknik visualisasi yang mewarnai area geografis berdasarkan nilai suatu variabel, memudahkan identifikasi pola konsentrasi risiko secara visual.

### 2.5 Penelitian Terdahulu

- [Nurhayati & Haryanto, 2022]: Analisis faktor penyebab putus sekolah di Jawa Barat menggunakan regresi logistik — menemukan kemiskinan sebagai faktor paling signifikan.
- [Prahasta, 2009]: Konsep Sistem Informasi Geografis untuk analisis spasial.
- [Han & Kamber, 2012]: Data Mining — penjelasan komprehensif algoritma K-Means dan evaluasi klaster.

---

## BAB 3: Metodologi

Penelitian ini mengikuti kerangka kerja **OSEMN** (Obtain, Scrub, Explore, Model, iNterpret).

### 3.1 Obtain — Pengumpulan Data

Data diperoleh dari dua sumber utama:

| Sumber | Data | Tahun |
|--------|------|:-----:|
| Buku Profil Perkembangan Kependudukan Jawa Barat 2024 (Kemendikdasmen) | Angka putus sekolah per jenjang (SD/SMP/SMA/SMK/SLB), estimasi total penduduk | 2024 |
| Badan Pusat Statistik (BPS) Provinsi Jawa Barat | IPM, persentase kemiskinan (Maret), garis kemiskinan | 2024 |
| GADM v4.0 + Badan Informasi Geospasial (BIG) | Batas administrasi 27 Kab/Kota (GeoJSON) | — |

**Variabel yang digunakan:**

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
| 13 | `Putus_Sekolah_per_10k_Penduduk` | Numerik | Rate putus sekolah per 10.000 penduduk |
| 14 | `Cluster` | Numerik | Label klaster (0/1/2) |
| 15 | `Tingkat_Kerentanan` | Kategorik | Risiko Tinggi/Sedang/Rendah |

### 3.2 Scrub — Pembersihan Data

Tahapan pembersihan data meliputi:

1. **Handling Missing Value**: Data kemiskinan bulan September 2024 dari BPS memiliki banyak kekosongan di tingkat Kabupaten/Kota, sehingga dihapus. Data kemiskinan yang digunakan adalah data Maret 2024 yang lengkap untuk 27 wilayah.

2. **Penyelarasan Nama Daerah**: Terdapat perbedaan penamaan antar sumber data (contoh: "Kab. Bandung Barat" vs "Kabupaten Bandung Barat"). Semua nama diselaraskan dengan format baku `Kab. <Nama>` dan `Kota <Nama>`.

3. **Konversi Tipe Data**: Beberapa kolom numerik terbaca sebagai string karena terdapat separator ribuan atau karakter non-numerik. Semua dikonversi ke tipe `float` atau `int`.

4. **Deteksi Outlier**: Menggunakan metode IQR (Interquartile Range), tidak ditemukan outlier matematis yang signifikan pada variabel utama. Distribusi data cukup homogen karena seluruhnya adalah data agregat Kabupaten/Kota.

**Ringkasan data setelah pembersihan:**

| Metrik | Nilai |
|--------|:-----:|
| Jumlah baris | 27 (sesuai jumlah Kab/Kota) |
| Jumlah kolom | 18 |
| Missing value | 0 |
| Outlier (IQR) | Tidak ada |

### 3.3 Explore — Eksplorasi Data

**Statistik Deskriptif:**

| Variabel | Mean | Min | Max |
|----------|:----:|:---:|:---:|
| Total Putus Sekolah | 220,00 | 27 | 621 |
| Persentase Kemiskinan (%) | 8,01 | 2,34 | 11,93 |
| IPM | 74,68 | 68,89 | 83,75 |
| Putus Sekolah per 10k Penduduk | 1,13 | 0,33 | 1,99 |

**Analisis Korelasi:**

Matriks korelasi Pearson dihitung untuk mengidentifikasi hubungan antar variabel. Temuan utama:

| Pasangan Variabel | Koefisien Korelasi (r) | Interpretasi |
|-------------------|:----------------------:|--------------|
| Kemiskinan vs Risk Index | **0,8081** | Korelasi positif kuat |
| IPM vs Risk Index | **-0,9579** | Korelasi negatif sangat kuat |
| Kemiskinan vs IPM | **-0,7841** | Korelasi negatif kuat |
| Kemiskinan vs Putus per 100k | **0,1877** | Korelasi positif lemah |

Korelasi antara **Persentase Penduduk Miskin** dan **Angka Putus Sekolah per 10k Penduduk** menunjukkan r = **0,3944** dengan p-value = **0,0418** (signifikan pada α=0,05). Ini mengonfirmasi hipotesis bahwa kemiskinan berkorelasi positif signifikan terhadap risiko putus sekolah, meskipun kekuatan korelasinya tergolong sedang.

![Grafik Korelasi Kemiskinan vs Putus Sekolah][]

### 3.4 Model — Klastering K-Means

**Pemilihan Jumlah Klaster (k):**

1. **Metode Elbow**: Grafik inertia menunjukkan titik siku (elbow) pada k=3, di mana penurunan inertia mulai melandai setelah titik tersebut.

![Grafik Metode Elbow][]

2. **Silhouette Score**: Nilai Silhouette untuk k=3 adalah **0,3409**, yang termasuk kategori "wajar" (>0,25) dan mengindikasikan struktur klaster yang cukup baik.

Berdasarkan kedua metode tersebut, **k=3** dipilih sebagai jumlah klaster optimal.

**Hasil Klastering:**

| Klaster | Jumlah Wilayah | Karakteristik |
|---------|:--------------:|---------------|
| **Risiko Tinggi** (Merah) | **12** | IPM rendah (71,46), kemiskinan tinggi (10,12%), putus/10k tinggi (1,43) |
| **Risiko Sedang** (Jingga) | **11** | IPM sedang (75,28), kemiskinan sedang (7,30%), putus/10k sedang (1,04) |
| **Risiko Rendah** (Hijau) | **4** | IPM tinggi (82,66), kemiskinan rendah (3,65%), putus/10k rendah (0,51) |

![Grafik Sebaran Klaster][]

### 3.5 Interpretasi — Dashboard

Hasil analisis divisualisasikan dalam **dashboard interaktif** berbasis Dash (Plotly) dengan 5 komponen utama:

1. **Choropleth Map** — peta sebaran risiko
2. **Scatter Plot** — korelasi kemiskinan vs putus sekolah
3. **Bar Chart** — breakdown per jenjang
4. **Ranking Table** — peringkat risiko 27 wilayah
5. **Cluster Summary** — karakteristik centroid

![Tampilan Dashboard][]

---

## BAB 4: Hasil & Pembahasan

### 4.1 Analisis Korelasi

Matriks korelasi (Lampiran 3) menunjukkan pola yang konsisten dengan teori:

- **IPM** berkorelasi negatif sangat kuat dengan **Risk Index** (r = -0,96) — semakin tinggi IPM suatu wilayah, semakin rendah risiko putus sekolah.
- **Persentase Kemiskinan** berkorelasi positif kuat dengan **Risk Index** (r = 0,81) — kemiskinan menjadi pendorong utama risiko putus sekolah.
- **Pengeluaran per Kapita** berkorelasi negatif kuat dengan **Risk Index** (r = -0,89) — daya beli masyarakat berbanding terbalik dengan risiko.
- **Rata-rata Lama Sekolah (RLS)** berkorelasi negatif sangat kuat dengan **Risk Index** (r = -0,91) — tingkat pendidikan orang dewasa di suatu wilayah menjadi proksi kesadaran akan pendidikan anak.

Korelasi langsung antara kemiskinan dan angka putus sekolah (r=0,39, p=0,04) mengonfirmasi secara statistik bahwa wilayah dengan tingkat kemiskinan lebih tinggi cenderung memiliki angka putus sekolah yang lebih tinggi. Meskipun korelasinya tidak terlalu kuat (r < 0,5), hal ini wajar karena putus sekolah merupakan fenomena multidimensi yang dipengaruhi banyak faktor.

![Scatter Plot: Kemiskinan vs Putus Sekolah]()

### 4.2 Klaster Risiko

#### 4.2.1 Risiko Tinggi (12 Wilayah)

Wilayah dalam klaster ini didominasi oleh **kabupaten** (11 kabupaten, 1 kota) dengan karakteristik:

| Indikator | Rata-rata Klaster |
|-----------|:-----------------:|
| IPM | 71,46 |
| Kemiskinan | 10,12% |
| Putus Sekolah per 10k | 1,43 |
| Total Putus Sekolah | 3.362 siswa |

**Daftar Wilayah:**
Kab. Bandung Barat, Kab. Cianjur, Kab. Cirebon, Kab. Garut, Kab. Indramayu, Kab. Karawang, Kab. Kuningan, Kab. Majalengka, Kab. Subang, Kab. Sukabumi, Kab. Tasikmalaya, Kota Tasikmalaya.

**Insight:** Kabupaten-kabupaten ini umumnya memiliki IPM di bawah rata-rata provinsi (74,68) dan tingkat kemiskinan di atas rata-rata (8,01%). Kota Tasikmalaya menjadi satu-satunya kota dalam klaster ini, menunjukkan urbanisasi tidak selalu menjamin rendahnya risiko putus sekolah.

#### 4.2.2 Risiko Sedang (11 Wilayah)

| Indikator | Rata-rata Klaster |
|-----------|:-----------------:|
| IPM | 75,28 |
| Kemiskinan | 7,30% |
| Putus Sekolah per 10k | 1,04 |
| Total Putus Sekolah | 2.087 siswa |

**Daftar Wilayah:**
Kab. Bandung, Kab. Bekasi, Kab. Bogor, Kab. Ciamis, Kab. Pangandaran, Kab. Purwakarta, Kab. Sumedang, Kota Banjar, Kota Bogor, Kota Cirebon, Kota Sukabumi.

**Insight:** Klaster ini merupakan kelompok transisi — beberapa kabupaten penyangga ibu kota (Bogor, Bekasi, Bandung) masuk kategori ini, menunjukkan tekanan urbanisasi dan disparitas internal yang cukup tinggi.

#### 4.2.3 Risiko Rendah (4 Wilayah)

| Indikator | Rata-rata Klaster |
|-----------|:-----------------:|
| IPM | 82,66 |
| Kemiskinan | 3,65% |
| Putus Sekolah per 10k | 0,51 |
| Total Putus Sekolah | 491 siswa |

**Daftar Wilayah:**
Kota Bandung, Kota Bekasi, Kota Cimahi, Kota Depok.

**Insight:** Keempat wilayah adalah **kota besar** di sekitar Jakarta dan Bandung dengan IPM tinggi (>80) serta tingkat kemiskinan sangat rendah (<5%). Ini menegaskan bahwa urbanisasi dan akses ekonomi yang baik berkorelasi dengan rendahnya risiko putus sekolah.

### 4.3 Peringkat Wilayah

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

**Insight:** Terdapat jurang pemisah yang lebar antara Kab. Tasikmalaya (skor 89,43) dengan Kota Bandung (skor 4,71) — rasio hampir **19:1**. Ini menunjukkan ketimpangan yang sangat signifikan dalam risiko putus sekolah antar wilayah di Jawa Barat.

### 4.4 Breakdown Jenjang

| Jenjang | Total | Persentase |
|---------|:-----:|:----------:|
| SD | 5.189 | **87,36%** |
| SMP | 230 | 3,87% |
| SMA | 88 | 1,48% |
| SMK | 335 | 5,64% |
| SLB | 98 | 1,65% |
| **Total** | **5.940** | **100%** |

**Insight:**
- **SD mendominasi** dengan 87,36% dari total putus sekolah. Ini konsisten dengan data nasional di mana angka putus sekolah tertinggi terjadi di jenjang dasar.
- **SMK** menyumbang 5,64% — lebih tinggi dari SMA (1,48%). Ini mengindikasikan bahwa siswa SMK lebih rentan putus sekolah, mungkin karena tekanan untuk segera bekerja.
- **SLB** memiliki 98 siswa (1,65%), yang relatif kecil namun tetap penting mengingat keterbatasan akses pendidikan khusus.

### 4.5 Peta Sebaran Spasial

Peta choropleth (Lampiran 1) menunjukkan pola spasial yang jelas:

- **Klaster Merah (Tinggi)** terkonsentrasi di **bagian selatan dan timur** Jawa Barat — wilayah dengan topografi pegunungan dan basis agraris.
- **Klaster Hijau (Rendah)** berada di **perkotaan besar** — Bandung Raya dan Jakarta satellite cities (Depok, Bekasi, Cimahi).
- **Klaster Jingga (Sedang)** menjadi zona transisi yang mengelilingi wilayah risiko tinggi.

Pola ini mengindikasikan bahwa **geografi dan akses ekonomi** menjadi faktor spasial yang penting — wilayah dengan akses terbatas ke pusat pertumbuhan ekonomi cenderung memiliki risiko putus sekolah yang lebih tinggi.

---

## BAB 5: Penutup

### 5.1 Kesimpulan

1. **Sebaran spasial** risiko putus sekolah di Jawa Barat menunjukkan konsentrasi wilayah risiko tinggi di bagian selatan dan timur (kabupaten agraris), sementara risiko rendah terkonsentrasi di kota-kota besar (Bandung, Bekasi, Depok, Cimahi).

2. **Korelasi signifikan** ditemukan antara kemiskinan dan angka putus sekolah (r = 0,3944; p = 0,0418). IPM memiliki korelasi negatif sangat kuat dengan risiko (r = -0,96).

3. **Klastering K-Means (k=3)** menghasilkan pengelompokan yang solid (Silhouette Score = 0,3409):
   - **12 wilayah Risiko Tinggi** — IPM rendah, kemiskinan tinggi
   - **11 wilayah Risiko Sedang** — karakteristik transisi
   - **4 wilayah Risiko Rendah** — IPM tinggi, kemiskinan rendah

4. **Jenjang pendidikan SD** menyumbang 87,36% dari total putus sekolah, menjadikannya prioritas utama intervensi kebijakan.

### 5.2 Saran Kebijakan

**Untuk Disdik Provinsi Jawa Barat:**

1. **Intervensi Terarah ke 12 Wilayah Prioritas**: Alokasi Bantuan Operasional Sekolah (BOS) afirmatif dan program beasiswa diprioritaskan untuk Kab. Tasikmalaya, Kab. Cianjur, Kab. Indramayu, dan 9 wilayah risiko tinggi lainnya.

2. **Fokus pada Jenjang SD**: 87,36% putus sekolah terjadi di SD. Program wajib belajar 12 tahun harus diperkuat dengan mekanisme *early warning system* untuk mendeteksi siswa berisiko putus sekolah sejak dini.

3. **Program Pengentasan Kemiskinan Terintegrasi**: Karena kemiskinan berkorelasi signifikan dengan putus sekolah, kolaborasi dengan Dinas Sosial dan Dinas Pemberdayaan Masyarakat diperlukan untuk intervensi yang holistik.

4. **Pengembangan SMK Vokasi Inklusif**: Tingginya angka putus sekolah di SMK (5,64%) dibanding SMA (1,48%) mengindikasikan perlunya reformasi kurikulum dan program magang yang lebih adaptif.

5. **Pendidikan Khusus dan Inklusif**: Meskipun jumlahnya kecil, 98 siswa SLB putus sekolah memerlukan perhatian khusus mengingat keterbatasan akses pendidikan inklusif di kabupaten.

### 5.3 Keterbatasan

1. Data kemiskinan September 2024 tidak tersedia di tingkat Kabupaten/Kota, sehingga hanya menggunakan data Maret.
2. Variabel terbatas pada data sekunder yang dipublikasikan — faktor kualitatif seperti budaya, motivasi, dan akses geografis tidak tertangkap.
3. Klastering dengan 27 titik data relatif kecil untuk analisis K-Means, sehingga hasil klaster bersifat indikatif.
4. Silhouette Score 0,3409 menunjukkan struktur klaster yang wajar tetapi tidak kuat — eksplorasi dengan algoritma lain (DBSCAN, Hierarchical) dapat dipertimbangkan.

### 5.4 Penelitian Lanjutan

1. Analisis dengan data tingkat **kecamatan** untuk resolusi yang lebih granular.
2. Penambahan variabel **aksesibilitas sekolah** (jarak, rasio murid-guru, ketersediaan transportasi).
3. Eksplorasi metode klastering alternatif (DBSCAN, Gaussian Mixture).
4. Analisis **temporal** dengan data multi-tahun untuk melihat tren dan efektivitas kebijakan.

---

## Daftar Pustaka

Badan Pusat Statistik. (2024). *Indeks Pembangunan Manusia Provinsi Jawa Barat 2024*. BPS Jawa Barat.

Badan Pusat Statistik. (2024). *Profil Kemiskinan Provinsi Jawa Barat Maret 2024*. BPS Jawa Barat.

Han, J., Kamber, M., & Pei, J. (2012). *Data Mining: Concepts and Techniques* (3rd ed.). Morgan Kaufmann.

Kemendikdasmen. (2024). *Buku Profil Perkembangan Kependudukan Jawa Barat 2024*. Direktorat Jenderal Pendidikan Anak Usia Dini, Pendidikan Dasar, dan Pendidikan Menengah.

Nurhayati, S., & Haryanto, T. (2022). Analisis Faktor Penyebab Putus Sekolah di Provinsi Jawa Barat. *Jurnal Pendidikan dan Kebudayaan*, 12(2), 145-162.

Prahasta, E. (2009). *Sistem Informasi Geografis: Konsep-Konsep Dasar*. Informatika Bandung.

Rousseeuw, P. J. (1987). Silhouettes: A Graphical Aid to the Interpretation and Validation of Cluster Analysis. *Journal of Computational and Applied Mathematics*, 20, 53-65.

---

## Lampiran

### Lampiran 1: Peta Sebaran Risiko Putus Sekolah

![Peta Choropleth Dashboard]()

### Lampiran 2: Dataset Bersih

**dataset_bersih.csv** — 27 baris × 18 kolom.

| Kab_Kota | Putus_SD | Putus_SMP | Putus_SMA | Putus_SMK | Putus_SLB | IPM_2024 | Persentase_Miskin_Maret | Cluster | Tingkat_Kerentanan |
|----------|:--------:|:---------:|:---------:|:---------:|:---------:|:--------:|:-----------------------:|:-------:|:------------------:|
| Kab. Bandung | 345 | 19 | 4 | 0 | 10 | 74,59 | 6,19 | 0 | Risiko Sedang |
| Kab. Bandung Barat | 195 | 7 | 11 | 16 | 12 | 70,77 | 10,49 | 1 | Risiko Tinggi |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| Kota Tasikmalaya | 90 | 0 | 0 | 1 | 1 | 76,03 | 11,10 | 1 | Risiko Tinggi |

*(dataset lengkap tersedia di `data/dataset_bersih.csv`)*

### Lampiran 3: Matriks Korelasi

| | putus_total | angka_putus_total_pct | putus_per_100k | kemiskinan | ipm_2024 | hls | rls | pengeluaran | risk_index |
|:--:|:-----------:|:---------------------:|:--------------:|:----------:|:--------:|:---:|:---:|:-----------:|:----------:|
| putus_total | 1,00 | 0,57 | 0,57 | 0,01 | -0,35 | -0,30 | -0,34 | -0,30 | 0,43 |
| kemiskinan | 0,01 | 0,21 | 0,19 | 1,00 | -0,78 | -0,71 | -0,75 | -0,71 | 0,81 |
| ipm_2024 | -0,35 | -0,36 | -0,32 | -0,78 | 1,00 | 0,85 | 0,95 | 0,92 | -0,96 |
| risk_index | 0,43 | 0,58 | 0,54 | 0,81 | -0,96 | -0,83 | -0,91 | -0,89 | 1,00 |

### Lampiran 4: Cluster Summary

| Klaster | Jumlah Wilayah | Rata-rata Putus Total | Rata-rata Kemiskinan (%) | Rata-rata RLS (thn) | Rata-rata HLS (thn) |
|---------|:--------------:|:---------------------:|:------------------------:|:-------------------:|:-------------------:|
| Prioritas Rendah | 4 | 115,25 | 3,65 | 11,49 | 14,09 |
| Prioritas Sedang | 11 | 295,95 | 8,76 | 8,38 | 12,66 |
| Prioritas Tinggi | 12 | 385,33 | 8,84 | 9,03 | 13,09 |

### Lampiran 5: Ranking Risiko 27 Kabupaten/Kota

| Peringkat | Wilayah | Risk Index |
|:---------:|---------|:----------:|
| 1 | Kab. Tasikmalaya | 89,43 |
| 2 | Kab. Cianjur | 84,49 |
| 3 | Kab. Indramayu | 76,49 |
| 4 | Kab. Sukabumi | 73,83 |
| 5 | Kab. Bandung Barat | 73,28 |
| ... | ... | ... |
| 27 | Kota Bandung | 4,71 |

*(ranking lengkap tersedia di `data/ranking_risiko_kabkota.csv`)*

### Lampiran 6: Dashboard Interaktif

Dashboard dapat diakses secara lokal dengan menjalankan:

```bash
python3 app.py
# Buka http://127.0.0.1:8050
```

![Screenshot Dashboard]()

### Lampiran 7: Kode Sumber

Seluruh kode sumber tersedia di repositori: `[]`

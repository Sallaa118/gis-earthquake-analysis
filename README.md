# GIS Earthquake Map — Pemetaan Gempa Bumi Indonesia

## 📌 Deskripsi Proyek

**GIS Earthquake Map** adalah proyek Sistem Informasi Geografis (GIS) sederhana menggunakan Python untuk memvisualisasikan persebaran titik gempa bumi di wilayah Indonesia pada peta interaktif.

Proyek ini menggunakan data gempa bumi dalam format CSV, kemudian membersihkan data koordinat, magnitudo, kedalaman, dan waktu kejadian. Data difilter berdasarkan rentang koordinat perkiraan wilayah Indonesia, lalu ditampilkan menggunakan peta interaktif yang dibuat dengan library Folium.

Setiap titik gempa ditampilkan sebagai lingkaran pada peta. Ukuran lingkaran menyesuaikan magnitudo gempa, sedangkan informasi lokasi, magnitudo, kedalaman, dan waktu dapat dilihat dengan mengeklik titik tersebut.

## 🎯 Tujuan Proyek

- Memvisualisasikan persebaran gempa bumi di wilayah Indonesia.
- Menerapkan konsep dasar Sistem Informasi Geografis menggunakan Python.
- Membersihkan dan memvalidasi data geografis sebelum divisualisasikan.
- Menampilkan informasi gempa melalui peta interaktif.
- Menghasilkan data gempa hasil filter untuk analisis lebih lanjut.

## 🛠️ Teknologi yang Digunakan

| Teknologi | Fungsi |
|---|---|
| Python | Bahasa pemrograman utama |
| Pandas | Membaca, membersihkan, memfilter, dan mengekspor data |
| Folium | Membuat peta interaktif berbasis Leaflet |
| pathlib | Membuat direktori keluaran jika belum tersedia |
| HTML | Format keluaran peta interaktif |

## 📂 Struktur Proyek

```text
gis-earthquake-map/
├── data/
│   └── earthquakes.csv
├── outputs/
│   ├── peta_gempa.html
│   └── gempa_indonesia.csv
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

**Keterangan:**
- `data/earthquakes.csv`: Dataset gempa bumi yang digunakan sebagai input.
- `outputs/peta_gempa.html`: Peta interaktif yang dihasilkan.
- `outputs/gempa_indonesia.csv`: Dataset gempa setelah difilter berdasarkan rentang koordinat Indonesia.
- `main.py`: Program utama untuk pemrosesan data dan pembuatan peta.
- `requirements.txt`: Daftar library Python yang diperlukan.
- `.gitignore`: Daftar file atau folder yang tidak perlu dimasukkan ke Git.

## 📊 Dataset

Program menggunakan dataset gempa bumi dalam format CSV dengan nama `earthquakes.csv`.

Kolom yang digunakan meliputi:

| Kolom | Keterangan |
|---|---|
| `time` | Waktu terjadinya gempa |
| `latitude` | Garis lintang lokasi gempa |
| `longitude` | Garis bujur lokasi gempa |
| `mag` | Magnitudo gempa |
| `depth` | Kedalaman gempa dalam kilometer |
| `place` | Deskripsi lokasi gempa |

Kolom `place` digunakan untuk informasi pada popup jika tersedia. Kolom `depth` juga ditampilkan pada popup, dengan nilai `N/A` jika tidak tersedia.

**Catatan:** Dataset harus memiliki kolom `time`, `latitude`, `longitude`, dan `mag`. Data perlu ditempatkan pada direktori `data/` dengan nama `earthquakes.csv`. Sumber dan periode dataset sebaiknya dicantumkan sesuai sumber data yang benar-benar digunakan.

## ⚙️ Alur Kerja Program

### 1. Membaca Dataset

Program membaca file CSV menggunakan Pandas:

```python
df = pd.read_csv("data/earthquakes.csv")
```

### 2. Membersihkan Data

Program mengubah kolom waktu menjadi format tanggal dan waktu serta mengonversi kolom koordinat, magnitudo, dan kedalaman menjadi numerik.

Data yang tidak memiliki nilai valid pada kolom `latitude`, `longitude`, atau `mag` akan dihapus agar tidak mengganggu proses pemetaan.

### 3. Memfilter Wilayah Indonesia

Program menggunakan rentang koordinat berikut:

- Latitude: -11 sampai 6
- Longitude: 95 sampai 141

Data yang berada di luar rentang tersebut tidak dimasukkan ke peta.

Rentang ini merupakan **filter kotak koordinat perkiraan**, bukan batas wilayah resmi Indonesia. Oleh karena itu, hasilnya tidak selalu sama dengan batas administratif atau geografis resmi.

### 4. Membuat Peta Interaktif

Peta dibuat menggunakan Folium dengan titik awal di sekitar tengah wilayah Indonesia:

- Koordinat pusat: `[-2.5, 118]`
- Zoom awal: `5`

Setiap kejadian gempa ditampilkan menggunakan `CircleMarker`.

Ukuran lingkaran dihitung berdasarkan magnitudo:

```python
radius = max(3, min(12, magnitudo * 2))
```

Dengan rumus tersebut, ukuran lingkaran dibatasi antara 3 dan 12 agar titik gempa tetap dapat dilihat dengan jelas.

### 5. Menampilkan Informasi Gempa

Ketika titik gempa diklik, popup menampilkan informasi berupa:

- Lokasi gempa
- Magnitudo
- Kedalaman
- Waktu kejadian

### 6. Menyimpan Hasil

Program menghasilkan dua file:

1. `outputs/peta_gempa.html` — peta interaktif yang dapat dibuka menggunakan browser.
2. `outputs/gempa_indonesia.csv` — data gempa yang telah melalui proses filter wilayah.

Jika tidak ditemukan data dalam rentang koordinat yang ditentukan, program akan menghentikan proses dan menampilkan pesan kesalahan agar tidak menghasilkan peta kosong.

## 💻 Instalasi dan Cara Menjalankan

### Prasyarat

Pastikan Python telah terpasang pada komputer.

### 1. Clone repositori

```bash
git clone URL_REPOSITORY_KAMU
cd gis-earthquake-map
```

Ganti `URL_REPOSITORY_KAMU` dengan URL repositori GitHub milikmu.

### 2. Buat virtual environment

```bash
python -m venv .venv
```

Aktifkan virtual environment pada Windows:

```bash
.venv\Scripts\activate
```

### 3. Instal dependensi

Buat file `requirements.txt` dengan isi:

```text
pandas
folium
```

Kemudian jalankan:

```bash
python -m pip install -r requirements.txt
```

### 4. Siapkan dataset

Pastikan dataset tersedia di lokasi:

```text
data/earthquakes.csv
```

### 5. Jalankan program

Jika file utama bernama `main.py`, jalankan:

```bash
python main.py
```

### 6. Buka hasil peta

Setelah program berhasil dijalankan, buka file berikut menggunakan browser:

```text
outputs/peta_gempa.html
```

File CSV hasil filter dapat diperiksa melalui Excel, LibreOffice Calc, atau editor data lainnya.

## 📈 Output Program

### Peta Gempa Interaktif

Peta menampilkan lokasi gempa yang masuk dalam rentang koordinat filter Indonesia. Pengguna dapat memperbesar atau memperkecil peta, menggeser tampilan, dan mengeklik titik gempa untuk melihat informasi detail.

### Data Gempa Hasil Filter

File `gempa_indonesia.csv` berisi data gempa yang memenuhi rentang koordinat filter dan memiliki nilai valid pada kolom latitude, longitude, serta magnitudo.

Program juga mencetak jumlah data gempa yang valid secara global setelah pembersihan dan jumlah data yang masuk ke filter wilayah.

## ⚠️ Batasan Proyek

- Filter wilayah Indonesia menggunakan rentang koordinat berbentuk kotak, bukan poligon batas resmi.
- Ukuran lingkaran hanya menunjukkan magnitudo secara relatif, bukan skala peta yang presisi.
- Akurasi visualisasi bergantung pada kualitas dan kelengkapan dataset.
- Program tidak memprediksi gempa bumi maupun menentukan tingkat risiko bencana.
- Jumlah gempa yang ditampilkan bergantung pada isi dan periode dataset yang digunakan.

## 🚀 Pengembangan Selanjutnya

Beberapa pengembangan yang dapat dilakukan:

- Menggunakan poligon batas wilayah Indonesia agar filter geografis lebih akurat.
- Menambahkan legenda magnitudo untuk membantu interpretasi peta.
- Menambahkan filter berdasarkan periode waktu atau rentang magnitudo.
- Menggunakan warna berbeda untuk mengelompokkan magnitudo gempa.
- Menambahkan ringkasan statistik berdasarkan wilayah, kedalaman, atau magnitudo.
- Membuat dashboard GIS berbasis web.

## 👤 Penulis

Nama: **[Nama Kamu]**

Program Studi: **Informatika**

Proyek: **GIS — Pemetaan Gempa Bumi Indonesia**

---

*Proyek ini dibuat sebagai latihan penerapan Python, pengolahan data geografis, dan visualisasi GIS menggunakan peta interaktif.*

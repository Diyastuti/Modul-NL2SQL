# BAB 1: PENDAHULUAN

## 1.1. Latar Belakang

Di era digital seperti sekarang, hampir semua kegiatan menghasilkan data. Contohnya adalah data siswa di sekolah, data penjualan di toko, data karyawan di perusahaan, hingga data peminjaman buku di perpustakaan. Semua data tersebut biasanya disimpan dalam sebuah **database** atau basis data agar lebih rapi, aman, dan mudah dicari.

Namun, untuk mengambil informasi dari database, seseorang harus menggunakan bahasa khusus yang disebut **SQL (Structured Query Language)**. SQL digunakan untuk memberikan perintah kepada database, misalnya untuk menampilkan data, mencari data tertentu, atau menghitung jumlah data.

Masalahnya, tidak semua orang memahami cara menulis SQL. Banyak pengguna hanya mengetahui apa yang ingin dicari, tetapi tidak tahu bagaimana membuat perintah SQL yang benar. Akibatnya, mereka harus meminta bantuan programmer atau bagian IT hanya untuk mengambil data sederhana.

Untuk mengatasi masalah tersebut, dikembangkan teknologi **NL2SQL (Natural Language to SQL)**. Teknologi ini memungkinkan pengguna menulis pertanyaan menggunakan bahasa sehari-hari, kemudian sistem AI akan menerjemahkannya menjadi perintah SQL secara otomatis.

Sebagai contoh:

- Pertanyaan pengguna:  
  *"Tampilkan semua data dosen"*

- Diubah oleh sistem menjadi SQL:

```sql
SELECT * FROM dosen;
```

Dengan adanya NL2SQL, proses pengambilan data menjadi lebih mudah, cepat, dan dapat digunakan oleh orang yang tidak memiliki kemampuan pemrograman.

---

## 1.2. Apa Itu NL2SQL?

**NL2SQL (Natural Language to Structured Query Language)** adalah teknologi yang digunakan untuk mengubah bahasa manusia (bahasa sehari-hari) menjadi bahasa SQL yang dapat dipahami oleh database.

Teknologi ini memanfaatkan **Artificial Intelligence (AI)** atau kecerdasan buatan untuk memahami maksud pertanyaan pengguna.

### Penjelasan Istilah

| Istilah | Penjelasan |
|---|---|
| Natural Language | Bahasa sehari-hari yang biasa digunakan manusia, seperti “Tampilkan semua siswa kelas 10” |
| SQL | Bahasa khusus yang digunakan untuk mengakses dan mengelola database |

### Contoh NL2SQL

| Bahasa Manusia | SQL |
|---|---|
| “Tampilkan semua dosen” | `SELECT * FROM dosen;` |
| “Cari siswa yang berumur 16 tahun” | `SELECT * FROM siswa WHERE umur = 16;` |
| “Hitung jumlah buku” | `SELECT COUNT(*) FROM buku;` |

Dengan NL2SQL, pengguna tidak perlu lagi menghafal sintaks SQL karena sistem akan membuatkannya secara otomatis.

---

## 1.3. Manfaat NL2SQL

Penggunaan teknologi NL2SQL memiliki banyak manfaat, terutama bagi pengguna yang tidak memahami bahasa pemrograman.

| Manfaat | Penjelasan |
|---|---|
| Mempermudah akses data | Pengguna dapat mengambil data hanya dengan mengetik pertanyaan biasa |
| Menghemat waktu | Tidak perlu menulis query SQL secara manual |
| Membantu pengguna non-teknis | Orang awam tetap bisa menggunakan database |
| Meningkatkan efisiensi kerja | Proses pencarian data menjadi lebih cepat |
| Mengurangi kesalahan SQL | Query dibuat otomatis oleh AI sehingga kesalahan penulisan dapat dikurangi |

---

## 1.4. Teknologi Pendukung

Dalam pembuatan aplikasi NL2SQL ini digunakan beberapa teknologi pendukung sebagai berikut:

### 1.4.1. Python

Python adalah bahasa pemrograman utama yang digunakan dalam proyek ini. Python dipilih karena mudah dipelajari, memiliki banyak library, dan sangat cocok untuk pengembangan AI serta aplikasi data.

### 1.4.2. Streamlit

Streamlit adalah library Python yang digunakan untuk membuat aplikasi web dengan cepat dan sederhana. Dengan Streamlit, tampilan aplikasi dapat dibuat tanpa harus menggunakan HTML atau CSS yang rumit.

### 1.4.3. Google Gemini AI

Google Gemini AI digunakan sebagai model kecerdasan buatan yang bertugas menerjemahkan pertanyaan bahasa Indonesia menjadi query SQL secara otomatis.

### 1.4.4. MySQL / SQLite

MySQL dan SQLite adalah sistem database yang digunakan untuk menyimpan data. Database ini nantinya akan menerima perintah SQL dari aplikasi.

### 1.4.5. Pandas

Pandas adalah library Python yang digunakan untuk mengolah dan menampilkan data dalam bentuk tabel agar lebih mudah dibaca.

### 1.4.6. Matplotlib

Matplotlib digunakan untuk membuat grafik atau visualisasi data seperti grafik batang, grafik garis, dan diagram lingkaran.

### 1.4.7. JSON dan Regex

- **JSON (JavaScript Object Notation)** digunakan sebagai format pertukaran data antara aplikasi dan AI.
- **Regex (Regular Expression)** digunakan untuk membersihkan teks atau memfilter karakter yang tidak diperlukan.

### 1.4.8. Dotenv dan OS

- **Dotenv** digunakan untuk menyimpan API key dan password database secara aman.
- **OS** digunakan untuk mengakses sistem operasi dan file lingkungan aplikasi.

---

## 1.5. Cara Kerja NL2SQL

Berikut adalah proses kerja sistem NL2SQL dari awal sampai akhir:

| Langkah | Penjelasan |
|---|---|
| 1 | Pengguna mengetik pertanyaan menggunakan bahasa Indonesia |
| 2 | Sistem AI membaca dan memahami pertanyaan tersebut |
| 3 | AI menerjemahkan pertanyaan menjadi perintah SQL |
| 4 | Query SQL dikirim ke database |
| 5 | Database menjalankan query dan mencari data |
| 6 | Hasil data ditampilkan kembali kepada pengguna |

### Contoh Proses

1. User mengetik:

> “Tampilkan semua siswa kelas 11”

2. AI mengubah menjadi:

```sql
SELECT * FROM siswa WHERE kelas = 11;
```

3. Database menjalankan query tersebut.

4. Data siswa kelas 11 ditampilkan di aplikasi.

Dengan proses ini, pengguna dapat mengambil data dengan lebih mudah tanpa perlu memahami SQL secara mendalam.
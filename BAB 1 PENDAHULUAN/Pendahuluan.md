# BAB 1: PENDAHULUAN

## 1.1. Latar Belakang

Di era digital saat ini, data menjadi aset yang sangat penting. Hampir setiap aktivitas manusia menghasilkan data, mulai dari data penjualan, data siswa, data karyawan, hingga data peminjaman buku. Data-data ini biasanya disimpan dalam sebuah **database** (basis data).

Masalahnya, untuk mengambil informasi dari database, seseorang harus menguasai **bahasa SQL (Structured Query Language)**. SQL adalah bahasa khusus yang digunakan untuk berkomunikasi dengan database. Sayangnya, tidak semua orang bisa menulis SQL.

Untuk mengatasi masalah ini, muncullah konsep **NL2SQL** (Natural Language to SQL). NL2SQL adalah teknologi yang dapat mengubah pertanyaan dalam **bahasa sehari-hari** menjadi **perintah SQL**.

---

## 1.2. Apa Itu NL2SQL?

**NL2SQL** adalah singkatan dari **Natural Language to Structured Query Language**.

| Kata | Artinya |
|------|---------|
| Natural Language | Bahasa sehari-hari, seperti "Tampilkan semua dosen" |
| SQL | Bahasa khusus database, seperti `SELECT * FROM dosen` |

**Ilustrasi sederhana:**
User bertanya: "Tampilkan semua dosen"
↓
[NL2SQL]
↓
SQL: SELECT * FROM dosen
↓
Database menjalankan SQL
↓
Hasil data ditampilkan ke user


---

## 1.3. Manfaat NL2SQL

| Manfaat | Penjelasan |
|---------|------------|
| Mempermudah akses data | Orang non-teknis bisa ambil data sendiri |
| Menghemat waktu | Tidak perlu tunggu bagian IT |
| Meningkatkan efisiensi | Staf fokus ke pekerjaan lain |

---

## 1.4. Teknologi Pendukung

Berikut teknologi yang akan digunakan:

### 1.4.1. Python
Bahasa pemrograman utama. Mudah dipelajari dan banyak library-nya.

### 1.4.2. Streamlit
Library untuk membuat aplikasi web dengan cepat. Tidak perlu HTML/CSS.

### 1.4.3. Google Gemini AI
Model AI dari Google yang menerjemahkan bahasa Indonesia ke SQL.

### 1.4.4. MySQL / SQLite
Tempat penyimpanan data (database).

### 1.4.5. Pandas
Library untuk mengolah dan menampilkan data dalam bentuk tabel.

### 1.4.6. Matplotlib
Library untuk membuat grafik (batang, garis, lingkaran).

### 1.4.7. JSON & Regex
- JSON: Format data komunikasi dengan AI
- Regex: Membersihkan teks dari karakter aneh

### 1.4.8. Dotenv & OS
Menyembunyikan API key dan password database (untuk keamanan).

---

## 1.5. Cara Kerja NL2SQL

| Langkah | Penjelasan |
|---------|------------|
| 1 | User mengetik pertanyaan dalam bahasa Indonesia |
| 2 | AI menerjemahkan pertanyaan menjadi SQL |
| 3 | Aplikasi menjalankan SQL ke database |
| 4 | Hasil data ditampilkan ke user |

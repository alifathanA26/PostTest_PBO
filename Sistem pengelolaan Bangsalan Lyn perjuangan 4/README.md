# Sistem Pengelolaan Bangsalan LYN Perjuangan 4

## Deskripsi Singkat

Program ini merupakan sistem sederhana untuk mengelola data Bangsalan LYN Perjuangan 4. Program dibuat menggunakan Python dengan menerapkan konsep PBO.

Program memiliki tiga class utama, yaitu `Kamar`, `Penghuni`, dan `Pembayaran`. Data yang dikelola meliputi informasi kamar, data penghuni, serta pembayaran sewa kamar.

## Tujuan Program

Program ini dibuat untuk:
- Mengelola data kamar pada Bangsalan LYN Perjuangan 4.
- Mengelola data penghuni kamar.
- Mengelola data pembayaran sewa.
- Menerapkan konsep dasar PBO menggunakan Python.

## Class yang Digunakan

Program ini memiliki tiga class utama:

### 1. Kamar
Digunakan untuk menyimpan dan menampilkan informasi kamar, seperti nomor kamar, gedung, harga sewa, jumlah penghuni, dan status kamar.

### 2. Penghuni
Digunakan untuk menyimpan data penghuni, seperti nama, nomor KTP, pekerjaan, dan nomor kamar.

### 3. Pembayaran
Digunakan untuk menyimpan data pembayaran, seperti ID pembayaran, nama penghuni, nomor kamar, jumlah pembayaran, dan status pembayaran.

## Konsep PBO yang Diterapkan

Program ini menerapkan beberapa konsep dasar PBO, yaitu:

### 1. Class dan Object
Class digunakan sebagai cetakan untuk membuat object. Program memiliki tiga class, yaitu `Kamar`, `Penghuni`, dan `Pembayaran`.

Object dibuat dari masing-masing class untuk menyimpan data yang berbeda.

### 2. Attribute
Attribute digunakan untuk menyimpan data pada class dan object. Contohnya seperti `nomor_kamar`, `harga_sewa`, `nama`, dan `status`.

### 3. Method
Method digunakan untuk menjalankan fungsi tertentu pada object. Contohnya `tampilkan_info()`, `tampilkan_data()`, dan `tampilkan_pembayaran()`.

### 4. Class Method
Class method digunakan untuk mengakses data yang dimiliki bersama oleh class. Contohnya adalah `info_bangsalan()` pada class `Kamar`.

### 5. Static Method
Static method digunakan untuk menjalankan fungsi yang tidak bergantung pada data object tertentu. Contohnya adalah `cek_status()` pada class `Pembayaran`.

### 6. Encapsulation
Encapsulation diterapkan pada attribute `__nama` pada class `Penghuni`. Attribute tersebut bersifat private dan diakses melalui getter dan setter.

### 7. Getter dan Setter
Getter digunakan untuk mengambil nilai `nama`, sedangkan setter digunakan untuk mengubah nilai `nama`. Setter juga melakukan validasi agar nama tidak boleh kosong.
## Cara Menjalankan Program


1. Buka folder project di Visual Studio Code.
2. Buka file `2509106026_Ali Fathan_Posttest1PBO`.
3. Jalankan program ( **Run**) atau menjalankan perintah:
   open terminal dengan ctrl + ` (jika tombol run ga muncul)
   ```bash
   python "2509106026_Ali Fathan_Posttest1PBO.py" 

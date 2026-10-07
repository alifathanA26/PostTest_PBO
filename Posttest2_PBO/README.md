# Sistem Pengelolaan Bangsalan LYN Perjuangan 4

## Deskripsi Singkat

Program ini merupakan pengembangan dari sistem pengelolaan Bangsalan LYN Perjuangan 4 pada posttest sebelumnya. Program dibuat menggunakan Python dengan menerapkan konsep PBO, dan pada posttest ini ditambahkan **relasi antar-class (UML)** serta **inheritance (pewarisan)**.

Program memiliki enam class, yaitu `Orang`, `Penghuni`, `Pengelola`, `Kamar`, `Bangsalan`, dan `Pembayaran`. Data yang dikelola meliputi informasi bangsalan, kamar, penghuni, pengelola, serta pembayaran sewa kamar.

## Tujuan Program

Program ini dibuat untuk:
- Mengelola data bangsalan, kamar, penghuni, pengelola, dan pembayaran sewa.
- Menerapkan relasi UML (asosiasi, agregasi, dan komposisi) antar-class.
- Menerapkan inheritance dengan superclass dan subclass.
- Menerapkan tingkat akses protected dan private pada pewarisan.

## Class yang Digunakan

Program ini memiliki enam class:

### 1. Orang (Superclass)
Class induk yang menyimpan data umum seorang manusia, yaitu nama dan nomor KTP. Memiliki method `tampilkan_data()` serta property `nama` beserta setter.

### 2. Penghuni (Subclass dari Orang)
Mewarisi `Orang` dan menambahkan atribut `pekerjaan` dan `nomor_kamar`.

### 3. Pengelola (Subclass dari Orang)
Mewarisi `Orang` dan menambahkan atribut `jabatan` dan `shift`.

### 4. Kamar
Menyimpan informasi kamar, yaitu nomor kamar, gedung, harga sewa, dan daftar penghuni. Jumlah penghuni dan status kamar dihitung otomatis dari daftar penghuni.

### 5. Bangsalan
Menyimpan nama bangsalan dan daftar kamar. Kamar dibuat melalui method `buat_kamar()`.

### 6. Pembayaran
Menyimpan data pembayaran, yaitu ID pembayaran, penghuni, kamar, jumlah bayar, dan status.

## Konsep PBO yang Diterapkan

### 1. Inheritance (Pewarisan)

**Superclass dan Subclass**
Terdapat satu superclass, yaitu `Orang`, dan dua subclass, yaitu `Penghuni` dan `Pengelola`.

**Penggunaan `super()`**
Kedua subclass memanggil konstruktor superclass dengan `super().__init__(nama, no_ktp)`, sehingga atribut `nama` dan `no_ktp` tidak perlu ditulis ulang.

**Atribut Tambahan**
- `Penghuni`: `pekerjaan` dan `nomor_kamar`.
- `Pengelola`: `jabatan` dan `shift`.

**Method Overriding**
Method `tampilkan_data()` pada superclass `Orang` di-override pada subclass `Penghuni`. Versi di `Penghuni` memanggil `super().tampilkan_data()` terlebih dahulu, lalu menambahkan tampilan pekerjaan dan nomor kamar.

**Tingkat Akses (Protected dan Private)**
- `_nama` (protected): dipakai langsung oleh subclass, contohnya pada method `info_tugas()` di `Pengelola`.
- `__no_ktp` (private): hanya bisa diakses di dalam class `Orang`. Subclass hanya bisa melihatnya melalui method `tampilkan_data()`, yang menampilkan nomor KTP dalam bentuk tersensor (contoh: `***001`).

### 2. Relasi UML

**Komposisi: `Bangsalan` dengan `Kamar`**
Objek `Kamar` dibuat di dalam class `Bangsalan` melalui method `buat_kamar()`. Kamar tidak berdiri sendiri, sehingga jika bangsalan tidak ada, kamar juga ikut hilang.

**Agregasi: `Kamar` dengan `Penghuni`**
Objek `Penghuni` dibuat di luar, lalu dimasukkan ke `daftar_penghuni` pada `Kamar` melalui method `tambah_penghuni()`. Jika kamar dikosongkan, objek penghuni tetap ada.

**Asosiasi: `Pembayaran` dengan `Penghuni` dan `Kamar`**
Class `Pembayaran` menyimpan referensi ke objek `Penghuni` dan `Kamar`. Ketiga class berdiri sendiri dan hanya saling berhubungan.

### 3. Konsep dari Posttest Sebelumnya

- **Class dan Object**: class sebagai cetakan, object sebagai data yang dibuat dari class.
- **Attribute dan Method**: menyimpan data dan menjalankan fungsi pada object.
- **Static Method**: `cek_status()` pada class `Pembayaran`, yang tidak bergantung pada object tertentu.
- **Encapsulation, Getter, dan Setter**: property `nama` pada class `Orang` dengan setter yang menolak nama kosong.

## Diagram UML
Gambar diagram:
![Diagram UML](screenshot/UML%20PBO.png)

Keterangan garis:
- Panah segitiga kosong: pewarisan
- Belah ketupat terisi: komposisi
- Belah ketupat kosong: agregasi
- Panah biasa: asosiasi

## Screenshot Kode

### Class Orang (Superclass)
![class Orang](screenshot/class%20Orang.png)

### Class Penghuni (Subclass)
![class Penghuni](screenshot/class%20Penghuni.png)

### Class Pengelola (Subclass)
![class Pengelola](screenshot/class%20Pengelola.png)

### Class Kamar
![class Kamar](screenshot/class%20Kamar.png)

### Class Bangsalan
![class Bangsalan](screenshot/class%20Bangsalan.png)

### Class Pembayaran
![class Pembayaran](screenshot/class%20Pembayaran.png)

### Program Utama
![Program utama](screenshot/Program%20utama.png)

## Hasil Output

![Output program](screenshot/Output%20program.png)

Penjelasan output:
- INFO BANGSALAN (KOMPOSISI): jumlah kamar bernilai 2 karena dua kamar dibuat melalui `buat_kamar()`.
- INFO KAMAR (AGREGASI): kamar 101 memiliki 2 penghuni dan berstatus Terisi, dihitung dari `daftar_penghuni`.
- DATA PENGHUNI (OVERRIDING): menampilkan nama, KTP tersensor, pekerjaan, dan nomor kamar dari method yang di-override.
- DATA PENGELOLA**: menampilkan tugas pengelola dengan memakai atribut protected `_nama`.
- PEMBAYARAN (ASOSIASI): nama penghuni dan nomor kamar diambil langsung dari objek yang dirujuk.
- TESTING SETTER: nama berhasil diubah, sedangkan nama kosong ditolak.

## Cara Menjalankan Program

1. Buka folder project di Visual Studio Code.
2. Buka file `2509106026_Ali Fathan_Posttest2PBO.py`.
3. Jalankan program (**Run**) atau menjalankan perintah:
   open terminal dengan ctrl + ` (jika tombol run ga muncul)
   ```bash
   python "2509106026_Ali Fathan_Posttest2PBO.py"
   ```
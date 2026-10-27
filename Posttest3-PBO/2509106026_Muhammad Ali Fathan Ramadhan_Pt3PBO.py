from abc import ABC, abstractmethod


class Kamar:
    def __init__(self, nomor_kamar, gedung, harga_sewa):
        self.nomor_kamar = nomor_kamar
        self.gedung = gedung
        self.harga_sewa = harga_sewa
        self.daftar_penghuni = []   # AGREGASI

    def tambah_penghuni(self, penghuni):
        self.daftar_penghuni.append(penghuni)

    @property
    def jumlah_penghuni(self):
        return len(self.daftar_penghuni)

    @property
    def status(self):
        return "Terisi" if self.jumlah_penghuni > 0 else "Kosong"

    def tampilkan_info(self):
        print(f"Kamar {self.nomor_kamar} - Gedung {self.gedung}")
        print(f"Harga sewa: Rp{self.harga_sewa}")
        print(f"Jumlah penghuni: {self.jumlah_penghuni}")
        print(f"Status: {self.status}")

    def ringkasan(self):
        return f"Kamar {self.nomor_kamar} ({self.status}, {len(self)} penghuni)"

    def __len__(self):
        return self.jumlah_penghuni

    def __str__(self):
        return f"Kamar {self.nomor_kamar} - Gedung {self.gedung}"


class Bangsalan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_kamar = []

    def buat_kamar(self, nomor_kamar, gedung, harga_sewa):
        # KOMPOSISI:
        kamar = Kamar(nomor_kamar, gedung, harga_sewa)
        self.daftar_kamar.append(kamar)
        return kamar

    def info_bangsalan(self):
        print(f"Nama bangsalan: {self.nama}")
        print(f"Jumlah kamar: {len(self.daftar_kamar)}")


class Orang(ABC):
    """Kelas dasar, tidak bisa dibuat objeknya secara langsung."""

    def __init__(self, nama, no_ktp):
        self._nama = nama          
        self.__no_ktp = no_ktp     

    @abstractmethod
    def peran(self):
        pass

    @abstractmethod
    def tanggung_jawab(self):
        pass

    def cetak_profil(self):
        print(f"[{self.peran()}]")
        self.tampilkan_data()
        print(f"Tanggung jawab: {self.tanggung_jawab()}")

    def tampilkan_data(self):
        print(f"Nama: {self._nama}")
        print(f"No. KTP: {self.__sensor_ktp()}")

    def __sensor_ktp(self):
        return "*" * (len(self.__no_ktp) - 3) + self.__no_ktp[-3:]

    @property
    def nama(self):
        return self._nama

    @nama.setter
    def nama(self, nama_baru):
        if nama_baru == "":
            print("Nama tidak boleh kosong.")
        else:
            self._nama = nama_baru


class Penghuni(Orang):
    def __init__(self, nama, no_ktp, pekerjaan, nomor_kamar):
        super().__init__(nama, no_ktp)
        self.pekerjaan = pekerjaan
        self.nomor_kamar = nomor_kamar

    def peran(self):
        return "Penghuni"

    def tanggung_jawab(self):
        return "Membayar sewa dan menjaga kebersihan kamar"

    def tampilkan_data(self):
        super().tampilkan_data()
        print(f"Pekerjaan: {self.pekerjaan}")
        print(f"Nomor kamar: {self.nomor_kamar}")


class Pengelola(Orang):
    def __init__(self, nama, no_ktp, jabatan, shift):
        super().__init__(nama, no_ktp)
        self.jabatan = jabatan          
        self.shift = shift              

    def peran(self):
        return "Pengelola"

    def tanggung_jawab(self):
        return "Mengawasi bangsalan dan mencatat pembayaran"

    def tampilkan_data(self):
        super().tampilkan_data()
        print(f"Jabatan: {self.jabatan} (shift {self.shift})")

    def info_tugas(self):
        print(f"{self._nama} bertugas sebagai {self.jabatan} (shift {self.shift})")


class Tamu(Orang):
    """Tamu bangsalan."""

    def __init__(self, nama, no_ktp, tujuan):
        super().__init__(nama, no_ktp)
        self.tujuan = tujuan

    def peran(self):
        return "Tamu"

    def tanggung_jawab(self):
        return "Lapor ke pengelola dan keluar sebelum jam malam"

    def tampilkan_data(self):
        super().tampilkan_data()
        print(f"Tujuan kunjungan: {self.tujuan}")


class Pembayaran:
    biaya_bulanan = 2000000

    def __init__(self, id_pembayaran, penghuni, kamar, jumlah_bayar, status):
        self.id_pembayaran = id_pembayaran
        self.penghuni = penghuni    
        self.kamar = kamar          
        self.jumlah_bayar = jumlah_bayar
        self.status = status

    def tampilkan_pembayaran(self):
        print(f"ID pembayaran: {self.id_pembayaran}")
        print(f"Nama penghuni: {self.penghuni.nama}")
        print(f"Nomor kamar: {self.kamar.nomor_kamar}")
        print(f"Jumlah bayar: Rp{self.jumlah_bayar}")
        print(f"Status: {self.status}")

    @staticmethod
    def cek_status(status):
        if status == "Lunas":
            print("Pembayaran sudah lunas.")
        else:
            print("Pembayaran belum lunas.")

    def ringkasan(self):
        return f"Pembayaran {self.id_pembayaran} oleh {self.penghuni.nama}: Rp{self.jumlah_bayar} ({self.status})"

    def __add__(self, other):
        return self.jumlah_bayar + other.jumlah_bayar

    def __radd__(self, other):      
        return other + self.jumlah_bayar


def cetak_ringkasan(objek):
    """Menampilkan ringkasan objek apa pun yang punya ringkasan()."""
    print(objek.ringkasan())


print("Sistem Pengelolaan Bangsalan LYN Perjuangan 4")

bangsalan = Bangsalan("Bangsalan LYN Perjuangan 4")

# Komposisi
kamar1 = bangsalan.buat_kamar(101, 1, 2000000)
kamar2 = bangsalan.buat_kamar(106, 2, 2000000)


penghuni1 = Penghuni("Andi", "KTP001", "Mahasiswa", 101)
penghuni2 = Penghuni("Budi", "KTP002", "Mahasiswa", 101)
pengelola1 = Pengelola("Rina", "KTP900", "Penjaga", "Pagi")
tamu1 = Tamu("Citra", "KTP777", "Mengunjungi Andi")

# Agregasi
kamar1.tambah_penghuni(penghuni1)
kamar1.tambah_penghuni(penghuni2)

# Asosiasi
pembayaran1 = Pembayaran("BYR001", penghuni1, kamar1, 1000000, "Lunas")
pembayaran2 = Pembayaran("BYR002", penghuni2, kamar1, 1000000, "Lunas")

print("\n--- Data Bangsalan ---")
bangsalan.info_bangsalan()

print("\n--- Data Kamar ---")
kamar1.tampilkan_info()

print("\n--- Data Pembayaran ---")
pembayaran1.tampilkan_pembayaran()
Pembayaran.cek_status(pembayaran1.status)

print("\n--- Ganti Nama Penghuni ---")
penghuni1.nama = "Emann"
print("Nama sekarang:", penghuni1.nama)
penghuni1.nama = ""

print("\n--- Coba Daftarkan Orang Tanpa Peran ---")
try:
    orang = Orang("Test", "KTP000")
except TypeError as e:
    print("Gagal:", e)

print("\n--- Profil Semua Orang di Bangsalan ---")
for orang in [penghuni1, pengelola1, tamu1]:
    orang.cetak_profil()
    print("-" * 40)

print("--- Ringkasan Kamar dan Pembayaran ---")
for objek in [kamar1, pembayaran1]:
    cetak_ringkasan(objek)

print("\n--- Rekap ---")
print("Kamar        :", kamar1)
print("Penghuni     :", len(kamar1), "orang")
print("Total bayar  : Rp", pembayaran1 + pembayaran2)
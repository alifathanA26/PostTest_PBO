class Kamar:
    def __init__(self, nomor_kamar, gedung, harga_sewa):
        self.nomor_kamar = nomor_kamar
        self.gedung = gedung
        self.harga_sewa = harga_sewa
        self.daftar_penghuni = []   # AGREGASI: menyimpan Penghuni dari luar

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


class Bangsalan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_kamar = []

    def buat_kamar(self, nomor_kamar, gedung, harga_sewa):
        # KOMPOSISI: objek Kamar dibuat DI DALAM Bangsalan
        kamar = Kamar(nomor_kamar, gedung, harga_sewa)
        self.daftar_kamar.append(kamar)
        return kamar

    def info_bangsalan(self):
        print(f"Nama bangsalan: {self.nama}")
        print(f"Jumlah kamar: {len(self.daftar_kamar)}")

class Orang:
    def __init__(self, nama, no_ktp):
        self._nama = nama          # protected: boleh diakses subclass
        self.__no_ktp = no_ktp     # private: rahasia superclass

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

    
    def tampilkan_data(self):
        super().tampilkan_data()
        print(f"Pekerjaan: {self.pekerjaan}")
        print(f"Nomor kamar: {self.nomor_kamar}")


class Pengelola(Orang):
    def __init__(self, nama, no_ktp, jabatan, shift):
        super().__init__(nama, no_ktp)
        self.jabatan = jabatan          # atribut unik Pengelola
        self.shift = shift              # atribut unik Pengelola

    def info_tugas(self):
        print(f"{self._nama} bertugas sebagai {self.jabatan} (shift {self.shift})")
        
class Pembayaran:
    biaya_bulanan = 2000000

    def __init__(self, id_pembayaran, penghuni, kamar, jumlah_bayar, status):
        self.id_pembayaran = id_pembayaran
        self.penghuni = penghuni    # ASOSIASI: merujuk objek Penghuni
        self.kamar = kamar          # ASOSIASI: merujuk objek Kamar
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

print("Program Sistem Pengelolaan Bangsalan LYN Perjuangan 4")

bangsalan = Bangsalan("Bangsalan LYN Perjuangan 4")

# Komposisi: kamar dibuat di dalam bangsalan
kamar1 = bangsalan.buat_kamar(101, 1, 2000000)
kamar2 = bangsalan.buat_kamar(106, 2, 2000000)

# Penghuni dan pengelola dibuat di luar
penghuni1 = Penghuni("Andi", "KTP001", "Mahasiswa", 101)
penghuni2 = Penghuni("Budi", "KTP002", "Mahasiswa", 101)
pengelola1 = Pengelola("Rina", "KTP900", "Penjaga", "Pagi")

# Agregasi: penghuni dimasukkan ke kamar
kamar1.tambah_penghuni(penghuni1)
kamar1.tambah_penghuni(penghuni2)

# Asosiasi: pembayaran merujuk ke objek
pembayaran1 = Pembayaran("BYR001", penghuni1, kamar1, 1000000, "Lunas")

print("\n== INFO BANGSALAN (KOMPOSISI) ==")
bangsalan.info_bangsalan()

print("\n== INFO KAMAR (AGREGASI) ==")
kamar1.tampilkan_info()

print("\n== DATA PENGHUNI (OVERRIDING) ==")
penghuni1.tampilkan_data()

print("\n== DATA PENGELOLA ==")
pengelola1.info_tugas()

print("\n== PEMBAYARAN (ASOSIASI) ==")
pembayaran1.tampilkan_pembayaran()

print("\n== STATIC METHOD ==")
Pembayaran.cek_status("Lunas")

print("\n== TESTING SETTER ==")
penghuni1.nama = "Emann"
print("Nama setelah diubah:", penghuni1.nama)
penghuni1.nama = ""

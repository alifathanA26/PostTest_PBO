class Kamar:
    nama_bangsalan = "Bangsalan LYN Perjuangan 4"
    total_gedung = 2
    total_kamar = 40

    
    def __init__(self, nomor_kamar, gedung, harga_sewa, jumlah_penghuni, status):
        self.nomor_kamar = nomor_kamar
        self.gedung = gedung
        self.harga_sewa = harga_sewa
        self.jumlah_penghuni = jumlah_penghuni
        self.status = status

    def tampilkan_info(self):
        print(f"Kamar {self.nomor_kamar} - Gedung {self.gedung}")
        print(f"Harga sewa: Rp{self.harga_sewa}")
        print(f"Jumlah penghuni: {self.jumlah_penghuni}")
        print(f"Status: {self.status}")

    @classmethod
    def info_bangsalan(cls):
        print("Nama bangsalan:", cls.nama_bangsalan)
        print("Jumlah gedung:", cls.total_gedung)
        print("Jumlah kamar:", cls.total_kamar)

class Penghuni:
    nama_bangsalan = "Bangsalan LYN Perjuangan 4"
    jatuh_tempo = 4
    metode_pembayaran = "Transfer"

    def __init__(self, nama, no_ktp, pekerjaan, nomor_kamar):
        self.__nama = nama
        self.no_ktp = no_ktp
        self.pekerjaan = pekerjaan
        self.nomor_kamar = nomor_kamar

    def tampilkan_data(self):
        print(f"Nama: {self.__nama}")
        print(f"Pekerjaan: {self.pekerjaan}")
        print(f"Nomor kamar: {self.nomor_kamar}")

    @property
    def nama(self):
        return self.__nama    
        
    @nama.setter
    def nama(self, nama_baru):
        if nama_baru == "":
            print("Nama tidak boleh kosong.")
        else:
            self.__nama = nama_baru    

class Pembayaran:
    nama_bangsalan = "Bangsalan LYN Perjuangan 4"
    jatuh_tempo = 4
    biaya_bulanan = 2000000

    
    def __init__(self, id_pembayaran, nama_penghuni, nomor_kamar, jumlah_bayar, status):
        self.id_pembayaran = id_pembayaran
        self.nama_penghuni = nama_penghuni
        self.nomor_kamar = nomor_kamar
        self.jumlah_bayar = jumlah_bayar
        self.status = status
        
    def tampilkan_pembayaran(self):
        print(f"ID pembayaran: {self.id_pembayaran}")
        print(f"Nama penghuni: {self.nama_penghuni}")
        print(f"Nomor kamar: {self.nomor_kamar}")
        print(f"Jumlah bayar: Rp{self.jumlah_bayar}")
        print(f"Status: {self.status}")

    @staticmethod
    def cek_status(status):
        if status == "Lunas":
            print("Pembayaran sudah lunas.")
        else:
            print("Pembayaran belum lunas.")        

print("Program Sistem Pengelolaan Bangsalan LYN Perjuangan 4")
print("Program berhasil dijalankan.")

#objek kamar
kamar1 = Kamar(101, 1, 2000000, 2, "Terisi")
kamar2 = Kamar(106, 2, 2000000, 1, "Terisi")

#objek penghuni
penghuni1 = Penghuni("Andi", "KTP001", "Mahasiswa", 101)
penghuni2 = Penghuni("Budi", "KTP002", "Mahasiswa", 101)

#objek pembayaran
pembayaran1 = Pembayaran("BYR001", "Andi", 101, 1000000, "Lunas")
pembayaran2 = Pembayaran("BYR002", "Budi", 101, 1000000, "Lunas")

#data objek
print()
print("== DATA KAMAR ==")
print(kamar1.nomor_kamar, kamar1.gedung, kamar1.harga_sewa, kamar1.jumlah_penghuni, kamar1.status)
print(kamar2.nomor_kamar, kamar2.gedung, kamar2.harga_sewa, kamar2.jumlah_penghuni, kamar2.status)

print()
print("== DATA PENGHUNI ==")
print(penghuni1.nama, penghuni1.pekerjaan, penghuni1.nomor_kamar)
print(penghuni2.nama, penghuni2.pekerjaan, penghuni2.nomor_kamar)

print()
print("== DATA PEMBAYARAN ==")
print(pembayaran1.id_pembayaran, pembayaran1.nama_penghuni, pembayaran1.jumlah_bayar, pembayaran1.status)
print(pembayaran2.id_pembayaran, pembayaran2.nama_penghuni, pembayaran2.jumlah_bayar, pembayaran2.status)

print()
print("== METHOD KAMAR ==")
kamar1.tampilkan_info()

print()
print("== METHOD PENGHUNI ==")
penghuni1.tampilkan_data()

print()
print("== METHOD PEMBAYARAN ==")
pembayaran1.tampilkan_pembayaran()

print()
print("== CLASS METHOD ==")
Kamar.info_bangsalan()

print() 
print("== STATIC METHOD ==")
Pembayaran.cek_status("Lunas")

print()
print("== TESTING SETTER ==")

penghuni1.nama = "Emann"
print("Nama setelah diubah:", penghuni1.nama)

penghuni1.nama = ""

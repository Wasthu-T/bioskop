class Film:
    def __init__(self, db):
        self.db = db

    def insert_film(self):
        print("===== Input Film =====")
        Judul = str(input("Masukan Judul Film\t: "))
        Jenis = str(input("Masukan Jenis Film\t: "))
        Produser = str(input("Masukan Produser Film\t: "))
        Sutradara = str(input("Masukan Sutradara Film\t: "))
        Penulis = str(input("Masukan Penulis Film\t: "))
        Produksi = str(input("Masukan Produksi Film\t: "))
        Casts = str(input("Masukan Casts Film\t: "))

        query = """INSERT INTO film(Judul, Jenis, Produser, Sutradara, Penulis, Produksi, Casts) VALUES (%s, %s, %s, %s, %s, %s,%s)"""
        data = (Judul,Jenis, Produser,Sutradara,Penulis,Produksi,Casts)

        self.db.insertValue(query,data)

    def update_film(self):
        print("===== Update Film =====")
        Id_film = int(input("Masukkan ID Film yang akan diupdate: "))

        Judul = str(input("Masukan Judul Film\t: "))
        Jenis = str(input("Masukan Jenis Film\t: "))
        Produser = str(input("Masukan Produser Film\t: "))
        Sutradara = str(input("Masukan Sutradara Film\t: "))
        Penulis = str(input("Masukan Penulis Film\t: "))
        Produksi = str(input("Masukan Produksi Film\t: "))
        Casts = str(input("Masukan Casts Film\t: "))

        query = """UPDATE film SET `Judul`= %s, `Jenis`= %s, `Produser`= %s, `Sutradara`= %s, `Penulis`= %s, `Produksi`=%s, `Casts`= %s WHERE `Id_film` = %s"""
        data = (Judul, Jenis, Produser, Sutradara, Penulis, Produksi, Casts, Id_film)

        self.db.insertValue(query, data)

    def delete_film(self):
        print("===== Delete Film =====")
        Id_film = int(input("Masukkan ID Film yang akan dihapus: "))

        query = """DELETE FROM film WHERE Id_film = %s """
        data = (Id_film,)
        
        self.db.insertValue(query, data)

    def read_film(self):
        print("===== Read Film =====")
        Id_film = int(input("Masukkan ID Film yang akan dilihat: "))
        
        query = """SELECT * FROM film WHERE Id_film = %s """
        data = (Id_film,)

        result = self.db.selectValue(query, data)

        if result:
            film = result[0]
            print(f"ID: {film[0]}")
            print(f"Judul: {film[1]}")
            print(f"Jenis: {film[2]}")
            print(f"Produser: {film[3]}")
            print(f"Sutradara: {film[4]}")
            print(f"Penulis: {film[5]}")
            print(f"Produksi: {film[6]}")
            print(f"Casts: {film[7]}")
        else:
            print("Film dengan ID tersebut tidak ditemukan.")
        
class Penonton() :
    def __init__(self, db):
        self.db = db

    def insert_penonton(self):
        print("=== Input Penonton ===")
        Nama = str(input("Masukan Nama\t: "))
        Email = str(input("Masukan Email\t: "))
        Nomor = str(input("Masukan Nomor\t: "))
        Password = str(input("Masukan Password: "))

        quary = """INSERT INTO penonton(Nama, Email, Nomor, Password) VALUES (%s, %s, %s, %s)"""
        data = (Nama, Email, Nomor, Password)

        self.db.insertValue(quary,data)

    def update_penonton(self):
        print("=== Update Penonton ===")
        Id_penonton = int(input("Masukkan ID Penonton yang akan diupdate: "))

        Nama = str(input("Masukan Nama\t: "))
        Email = str(input("Masukan Email\t: "))
        Nomor = str(input("Masukan Nomor\t: "))
        Password = str(input("Masukan Password: "))

        query = """UPDATE penonton SET `Nama`= %s, `Email`= %s, `Nomor`= %s, `Password`= %s WHERE `Id_penonton` = %s"""
        data = (Nama, Email, Nomor, Password, Id_penonton)

        self.db.insertValue(query, data)

    def delete_penonton(self):
        print("=== Delete Penonton ===")
        Id_penonton = int(input("Masukkan ID Penonton yang akan dihapus: "))

        query = """DELETE FROM penonton WHERE Id_penonton = %s """
        data = (Id_penonton,)
        
        self.db.insertValue(query, data)

    def read_penonton(self):
        print("=== Read Penonton ===")
        Id_penonton = int(input("Masukkan ID Penonton yang akan dilihat: "))

        query = """SELECT * FROM penonton WHERE Id_penonton = %s"""
        data = (Id_penonton,)

        result = self.db.selectValue(query, data)

        if result:
            penonton = result[0]
            print(f"ID Penonton: {penonton[0]}")
            print(f"Email: {penonton[1]}")
            print(f"Nomor: {penonton[2]}")
            print(f"Password: {penonton[3]}")
        else:
            print("Penonton dengan ID tersebut tidak ditemukan.")

class Pegawai() :
    def __init__(self, db):
        self.db = db

    def insert_pegawai(self):
        print("=== Input Pegawai ===")
        Nama = str(input("Masukan Nama\t\t: "))
        Email = str(input("Masukan Email\t\t: "))
        Nomor = str(input("Masukan Nomor\t\t: "))
        Usia = str(input("Masukan Usia\t\t: "))
        Jenis_kelamin = str(input("Masukan Jenis Kelamin\t: "))

        quary = """INSERT INTO pegawai(Nama, Email, Nomor, Usia, Jenis_kelamin) VALUES (%s, %s, %s, %s, %s)"""
        data = (Nama, Email, Nomor, Usia, Jenis_kelamin)

        self.db.insertValue(quary,data)

    def update_pegawai(self):
        print("=== Update Pegawai ===")
        Id_pegawai = int(input("Masukkan ID Pegawai yang akan diupdate: "))

        Nama = str(input("Masukan Nama\t\t: "))
        Email = str(input("Masukan Email\t\t: "))
        Nomor = str(input("Masukan Nomor\t\t: "))
        Usia = str(input("Masukan Usia\t\t: "))
        Jenis_kelamin = str(input("Masukan Jenis Kelamin\t: "))

        query = """UPDATE pegawai SET `Nama`= %s, `Email`= %s, `Nomor`= %s, `Usia`= %s, `Jenis_kelamin`= %s WHERE `Id_pegawai` = %s"""
        data = (Nama, Email, Nomor, Usia, Jenis_kelamin, Id_pegawai)

        self.db.insertValue(query, data)

    def delete_pegawai(self):
        print("=== Delete Pegawai ===")
        Id_pegawai = int(input("Masukkan ID Pegawai yang akan dihapus: "))

        query = """DELETE FROM pegawai WHERE Id_pegawai = %s """
        data = (Id_pegawai,)
        
        self.db.insertValue(query, data)

    def read_pegawai(self):
        print("=== Read Pegawai ===")
        Id_pegawai = int(input("Masukkan ID Pegawai yang akan dilihat: "))

        query = """SELECT * FROM pegawai WHERE Id_pegawai = %s"""
        data = (Id_pegawai,)

        result = self.db.selectValue(query, data)

        if result:
            pegawai = result[0]
            print(f"ID Pegawai: {pegawai[0]}")
            print(f"Nama: {pegawai[1]}")
            print(f"Email: {pegawai[2]}")
            print(f"Nomor: {pegawai[3]}")
            print(f"Usia: {pegawai[4]}")
            print(f"Jenis Kelamin: {pegawai[5]}")
        else:
            print("Pegawai dengan ID tersebut tidak ditemukan.")

class Pesan() :
    def __init__(self, db):
        self.db = db

    def insert_pesan(self):
        print("=== Input Pesan ===")
        Judul = str(input("Masukan Judul Film\t\t: "))
        Nomor_kursi = str(input("Masukan Nomor Kursi\t\t: "))
        Jenis_kursi = str(input("Masukan Jenis Kursi\t\t: "))
        Hari = str(input("Masukan Hari Menonton\t\t: "))
        Jam = str(input("Masukan Jam Menonton\t\t: "))
        Tgl = str(input("Masukan Tanggal Menonton\t\t: "))
        Harga = str(input("Masukan Harga Tiket\t\t: "))

        query = """INSERT INTO pesan(Judul, Nomor_kursi, Jenis_kursi, Hari, Jam, Tgl, Harga) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        data = (Judul, Nomor_kursi, Jenis_kursi, Hari, Jam, Tgl, Harga)

        self.db.insertValue(query,data)

    def update_pesan(self):
        print("=== Update Pesan ===")
        Id_pesan = int(input("Masukkan ID Pesan yang akan diupdate: "))

        Judul = str(input("Masukan Judul Film\t\t: "))
        Nomor_kursi = str(input("Masukan Nomor Kursi\t\t: "))
        Jenis_kursi = str(input("Masukan Jenis Kursi\t\t: "))
        Hari = str(input("Masukan Hari Menonton\t\t: "))
        Jam = str(input("Masukan Jam Menonton\t\t: "))
        Tgl = str(input("Masukan Tanggal Menonton\t: "))
        Harga = str(input("Masukan Harga Tiket\t\t: "))

        query = """UPDATE pesan SET `Judul`= %s, `Nomor_kursi`= %s, `Jenis_kursi`= %s, `Hari`= %s, `Jam`= %s, `Tgl`= %s, `Harga`= %s WHERE `Id_pesan` = %s"""
        data = (Judul, Nomor_kursi, Jenis_kursi, Hari, Jam, Tgl, Harga, Id_pesan)


        self.db.insertValue(query,data)

    def delete_pesan(self):
        print("=== Delete Pesan ===")
        Id_pesan = int(input("Masukkan ID Pesan yang akan dihapus: "))

        query = """DELETE FROM pesan WHERE Id_pesan = %s """
        data = (Id_pesan,)
        
        self.db.insertValue(query, data)

    def read_pesan(self):
        print("=== Read Pesan ===")
        Id_pesan = int(input("Masukkan ID Pesan yang akan dilihat: "))

        query = """SELECT * FROM pesan WHERE Id_pesan = %s"""
        data = (Id_pesan,)

        result = self.db.selectValue(query, data)

        if result:
            pesan = result[0]
            print(f"ID Pesan: {pesan[0]}")
            print(f"Judul: {pesan[1]}")
            print(f"Nomor Kursi: {pesan[2]}")
            print(f"Jenis Kursi: {pesan[3]}")
            print(f"Hari: {pesan[4]}")
            print(f"Jam: {pesan[5]}")
            print(f"Tgl: {pesan[6]}")
            print(f"Harga: {pesan[7]}")
        else:
            print("Pesan dengan ID tersebut tidak ditemukan.")

class Kursi():
    def __init__(self, db):
        self.db = db

    def insert_kursi(self):
        print("=== Input Kursi ===")
        Nomor_kursi = str(input("Masukan Nomor Kursi\t\t: "))
        Jenis_kursi = str(input("Masukan Jenis Kursi\t\t: "))
        Id_Ruangan = str(input("Masukan ID Ruangan\t\t: "))

        query = """INSERT INTO kursi(Nomor_kursi, Jenis_kursi, Id_Ruangan) VALUES (%s, %s, %s)"""
        data = (Nomor_kursi, Jenis_kursi, Id_Ruangan)

        self.db.insertValue(query,data)

    def update_kursi(self):
        print("=== Update Kursi ===")
        Id_kursi = int(input("Masukkan ID Kursi yang akan diupdate: "))

        Nomor_kursi = str(input("Masukan Nomor Kursi\t\t: "))
        Jenis_kursi = str(input("Masukan Jenis Kursi\t\t: "))
        Id_Ruangan = str(input("Masukan ID Ruangan\t\t: "))

        query = """UPDATE kursi SET `Nomor_kursi`= %s, `Jenis_kursi`= %s, `Id_Ruangan`= %s WHERE `Id_kursi` = %s"""
        data = (Nomor_kursi, Jenis_kursi, Id_Ruangan, Id_kursi)

        self.db.insertValue(query,data)

    def delete_kursi(self):
        print("=== Delete Kursi ===")
        Id_kursi = int(input("Masukkan ID Kursi yang akan dihapus: "))

        query = """DELETE FROM kursi WHERE Id_kursi = %s """
        data = (Id_kursi,)
        
        self.db.insertValue(query, data)

    def read_kursi(self):
        print("=== Read Kursi ===")
        Id_kursi = int(input("Masukkan ID Kursi yang akan dilihat: "))

        query = """SELECT * FROM kursi WHERE Id_kursi = %s"""
        data = (Id_kursi,)

        result = self.db.selectValue(query, data)

        if result:
            pesan = result[0]
            print(f"ID Kursi: {pesan[0]}")
            print(f"Nomor Kursi: {pesan[1]}")
            print(f"Jenis Kursi: {pesan[2]}")
            print(f"ID Ruangan: {pesan[3]}")
        else:
            print("Kursi dengan ID tersebut tidak ditemukan.")
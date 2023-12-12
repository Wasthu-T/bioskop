from prettytable import PrettyTable
from email_validator import validate_email, EmailNotValidError
from datetime import datetime
import locale
# set bahasa waktu lokal indonesia
locale.setlocale(locale.LC_TIME, 'id_ID')

# tabel film done
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
        print("=== Anda Berhasil Menambahkan Data Film ===")

    def edit_film(self,result, Id_film) :
        Judul = result[0][1]
        Jenis = result[0][2]
        Produser = result[0][3]
        Sutradara = result[0][4]
        Penulis = result[0][5]
        Produksi = result[0][6]
        Casts = result[0][7]
        while True : 
            print("=== Edit value ===")
            print("1. Judul")
            print("2. Jenis")
            print("3. Produser")
            print("4. Sutradara")
            print("5. Penulis")
            print("6. Produksi")
            print("7. Casts")
            pilih = int(input("Data yang ingin diubah : "))
            if pilih == 1 :
                Judul = str(input("Masukan Judul Film\t: "))
            elif pilih == 2 :
                Jenis = str(input("Masukan Jenis Film\t: "))
            elif pilih == 3 :
                Produser = str(input("Masukan Produser Film\t: "))
            elif pilih == 4 :
                Sutradara = str(input("Masukan Sutradara Film\t: "))
            elif pilih == 5 :
                Penulis = str(input("Masukan Penulis Film\t: "))
            elif pilih == 6 :
                Produksi = str(input("Masukan Produksi Film\t: "))
            elif pilih == 7 :
                Casts = str(input("Masukan Casts Film\t: "))            
            else : 
                print("Pilihan tidak tersedia")
            lanjut = str(input("Ganti data lain (y/n)? "))
            if lanjut == 'y' :
                continue
            else :
                break

        query = """UPDATE film SET `Judul`= %s, `Jenis`= %s, `Produser`= %s, `Sutradara`= %s, `Penulis`= %s, `Produksi`=%s, `Casts`= %s WHERE `Id_film` = %s"""
        data = (Judul, Jenis, Produser, Sutradara, Penulis, Produksi, Casts, Id_film)
        self.db.insertValue(query, data)

    def update_film(self):
        print("===== Update Film =====")
        Id_film = int(input("Masukkan ID Film yang akan diupdate: "))
        query = """SELECT * FROM Film WHERE Id_film = %s"""
        data = (Id_film,)
        self.db.selectValuepretty(query, data)
        result = self.db.selectValue(query, data)


        test = str(input("Apa data ingin diupdate (y/n)? "))
        if test.lower() == 'y' :
            self.edit_film(result, Id_film)
            print("=== Anda Berhasil Meng-update Data Film ===")
            self.db.selectValuepretty(query, data)
        else :
            print("=== Anda Gagal Meng-update Data Film ===")

    def delete_film(self):
        print("===== Delete Film =====")
        Id_film = int(input("Masukkan ID Film yang akan dihapus: "))
        query = """SELECT * FROM film WHERE Id_film = %s"""
        data = (Id_film,)
        self.db.selectValuepretty(query, data)
        test = str(input("Apa data ingin diupdate (y/n)? "))
        if test.lower() == 'y' :
            query = """DELETE FROM film WHERE Id_film = %s """
            data = (Id_film,)
            self.db.insertValue(query, data)
            print("=== Anda Berhasil Menghapus Data Film ===")
        else :
            print("=== Anda Gagal Menghapus Data Film ===")

    def read_film(self):
        print("===== Read Film =====")    
        query = """SELECT * FROM film"""
        self.db.selectValuepretty(query, data=None)
        
# tabel penonton done
class Penonton :
    def __init__(self, db):
        self.db = db

    def check_email(self):
        run = True
        while run :
            try:
                Email = str(input("Masukan Email\t: "))
                validate_email(Email)
                return Email
            except EmailNotValidError as e:
                print(str(e))

    def insert_penonton(self):
        print("=== Input Penonton ===")
        Nama = str(input("Masukan Nama\t: "))
        Email = self.check_email()
        Nomor = "0" + str(int(input("Masukan Nomor\t: ")))
        Password = str(input("Masukan Password: "))

        quary = """INSERT INTO penonton(Nama, Email, Nomor, Password) VALUES (%s, %s, %s, %s)"""
        data = (Nama, Email, Nomor, Password)

        self.db.insertValue(quary,data)
        print("=== Anda Berhasil Menambahkan Data Penonton ===")


    def edit_penonton(self, result, Id_penonton) :
        Nama = result[0][1]
        Email = result[0][2]
        Nomor = result[0][3]
        Password = result[0][4]
        while True : 
            print("=== Edit value ===")
            print("1. Nama")
            print("2. Email")
            print("3. Nomor")
            print("4. Password")
            pilih = int(input("Data yang ingin diubah : "))
            if pilih == 1 :
                Nama = str(input("Masukan Nama\t: "))
            elif pilih == 2 :
                Email = self.check_email()
            elif pilih == 3 :
                Nomor = "0" + str(int(input("Masukan Nomor\t: ")))
            elif pilih == 4 :
                Password = str(input("Masukan Password: "))
            else : 
                print("Pilihan tidak tersedia")
            lanjut = str(input("Ganti data lain (y/n)? "))
            if lanjut == 'y' :
                continue
            else :
                break
        query = """UPDATE penonton SET `Nama`= %s, `Email`= %s, `Nomor`= %s, `Password`= %s WHERE `Id_penonton` = %s"""
        data = (Nama, Email, Nomor, Password, Id_penonton)
        self.db.insertValue(query, data)

    def update_penonton(self):
        print("=== Update Penonton ===")
        Id_penonton = int(input("Masukkan ID Penonton yang akan diupdate: "))
        query = """SELECT * FROM penonton WHERE Id_penonton = %s"""
        data = (Id_penonton,)
        self.db.selectValuepretty(query, data)
        result = self.db.selectValue(query, data)

        test = str(input("Apa data ingin diupdate (y/n)? "))
        if test.lower() == 'y' :
            self.edit_penonton(result, Id_penonton)
            print("=== Anda Berhasil Meng-update Data Penonton ===")
        else :
            print("=== Anda Gagal Meng-update Data Penonton ===")
        self.db.insertValue(query, data)

    def delete_penonton(self):
        print("=== Delete Penonton ===")
        Id_penonton = int(input("Masukkan ID Penonton yang akan dihapus: "))
        query = """SELECT FROM penonton WHERE Id_penonton = %s """
        data = (Id_penonton,)
        self.db.selectValuepretty(query, data)
        test = str(input("Apa data ingin dihapus (y/n)? "))
        if test.lower() == 'y' :
            query = """DELETE FROM penonton WHERE Id_penonton = %s """
            data = (Id_penonton,)
            self.db.insertValue(query, data)
            print("=== Anda Berhasil Menghapus Data penonton ===")
            
        else :
            print("=== Anda Gagal Menghapus Data penonton ===")

    def read_penonton(self):
        print("=== Read Penonton ===")
        query = """SELECT * FROM penonton"""
        self.db.selectValuepretty(query, data=None)

# tabel pegawai done
class Pegawai :
    def __init__(self, db):
        self.db = db

    def jenis_kelamin(self) :
        while True :
            print("=== Jenis Kelamin ===")
            print("1. Laki-laki")
            print("2. Perempuan")
            pilih = int(input("Pilih Jenis Kelamin\t:"))
            if pilih == 1 :
                return "Laki-laki"
            elif pilih == 2 :
                return "Perempuan"
            else :
                print("pilihan tidak tersedia harap pilih yang benar")

    def umur(self) :
        umur = int(input("Masukan Usia\t\t: "))
        if umur >= 18 :
            return umur
        else :
            print("Usia anda dibawah umur")
            return None
        
    def check_email(self):
        run = True
        while run :
            try:
                Email = str(input("Masukan Email\t: "))
                validate_email(Email)
                return Email
            except EmailNotValidError as e:
                print(str(e))   

    def insert_pegawai(self):
        print("=== Input Pegawai ===")
        Nama = str(input("Masukan Nama\t\t: "))
        Email = self.check_email()
        Nomor = "0" + str(int(input("Masukan Nomor\t\t: ")))

        Jenis_kelamin = self.jenis_kelamin()
        Usia = self.umur()
        x = PrettyTable()
        x.field_names = ["Nama", "Email", "Nomor", "Usia", "Jenis_kelamin"]
        x.add_row([Nama, Email, Nomor, Usia, Jenis_kelamin])
        print(x)
        yakin = str(input("Yakin ingin menambah data y/n? "))
        if (yakin == 'y') and (Usia is not None) :
            quary = """INSERT INTO pegawai(Nama, Email, Nomor, Usia, Jenis_kelamin) VALUES (%s, %s, %s, %s, %s)"""
            data = (Nama, Email, Nomor, Usia, Jenis_kelamin)

            self.db.insertValue(quary,data)
            print("=== Anda Berhasil Menambahkan Data Pegawai ===")
        else : 
            print("=== Anda Gagal Menambahkan Data Pegawai ===")

    def edit(self, result, Id_pegawai) :
        Nama = result[0][1]
        Email = result[0][2]
        Nomor = result[0][3]
        Usia = result[0][4]
        while True : 
            print("=== Edit value ===")
            print("1. Nama")
            print("2. Email")
            print("3. Nomor")
            print("4. Usia")
            pilih = int(input("Data yang ingin diubah : "))
            if pilih == 1 :
                Nama = str(input("Masukan Nama\t\t: "))
            elif pilih == 2 :
                Email = self.check_email()
            elif pilih == 3 :
                Nomor = "0" + str(int(input("Masukan Nomor\t\t: ")))
            elif pilih == 4 :
                Usia = self.umur()
                if Usia <= result[0][4] :
                    print("Usia kamu turun?")
                    Usia = result[0][4]
                if Usia is None :
                    Usia = result[0][4]
            else : 
                print("Pilihan tidak tersedia")
            lanjut = str(input("Ganti data lain (y/n)? "))
            if lanjut == 'y' :
                continue
            else :
                break
        query = """UPDATE pegawai SET `Nama`= %s, `Email`= %s, `Nomor`= %s, `Usia`= %s  WHERE Id_pegawai = %s"""
        data = (Nama, Email, Nomor, Usia, Id_pegawai)
        self.db.insertValue(query, data)

    def update_pegawai(self):
        print("=== Update Pegawai ===")
        Id_pegawai = int(input("Masukkan ID Pegawai yang akan diupdate: "))
        query = """SELECT * FROM pegawai WHERE Id_pegawai = %s"""
        data = (Id_pegawai,)
        self.db.selectValuepretty(query, data)
        result = self.db.selectValue(query, data)


        test = str(input("Apa data ingin diupdate (y/n)? "))
        if test.lower() == 'y' :
            self.edit(result, Id_pegawai)
            print("=== Anda Berhasil Meng-update Data Pegawai ===")
        else :
            print("=== Anda Gagal Meng-update Data Pegawai ===")

    def delete_pegawai(self):
        print("=== Delete Pegawai ===")
        Id_pegawai = int(input("Masukkan ID Pegawai yang akan dihapus: "))
        query = """SELECT * FROM pegawai WHERE Id_pegawai = %s"""
        data = (Id_pegawai,)
        self.db.selectValuepretty(query, data)
        test = str(input("Apa data ingin diupdate (y/n)? "))
        if test.lower() == 'y' :
            query = """DELETE FROM pegawai WHERE Id_pegawai = %s """
            data = (Id_pegawai,)
            self.db.insertValue(query, data)
            print("=== Anda Berhasil Menghapus Data Pegawai ===")
            
        else :
            print("=== Anda Gagal Menghapus Data Pegawai ===")

    def read_pegawai(self):
        print("=== Read Pegawai ===")
        query = """SELECT * FROM pegawai"""
        self.db.selectValuepretty(query, data=None)

# done
class Tiket : 
    def __init__(self, db):
        self.db = db

    def set_harga(self,hari) :
        harga = 0 
        if(hari in ('Senin', 'Selasa', 'Rabu', 'Kamis')) :
            harga = 30000
        elif hari == 'Jumat' :
            harga = 35000
        elif(hari in ('Sabtu','Minggu')) :
            harga = 40000
        return harga
            
    def insert_tiket(self) :
        print("=== Input Tiket ===")
        Id_film = int(input("Masukan Id_film\t: "))

        time_str = (input("Masukan jam tayang (format: hh:mm:ss)\t: "))
        date_time = datetime.strptime(time_str, "%H:%M:%S")
        Jam_tayang = date_time.time()

        date_str = input("Masukkan tanggal tayang (format: YYYY-MM-DD)\t: ") #set date
        date = datetime.strptime(date_str, "%Y-%m-%d") #get date
        Tanggal = date.date() #only date
        hari = date.strftime("%A") #only day
        harga = self.set_harga(hari)

        stok = int(input("Masukan stok kursi\t: "))
        quary = """INSERT INTO tiket(Id_film, Jam_tayang, Hari,Tanggal, Harga, Stok_kursi) VALUES (%s, %s, %s, %s,%s,%s)"""
        data = (Id_film, Jam_tayang, hari,Tanggal,harga,stok)

        self.db.insertValue(quary,data)
        print("=== Anda Berhasil Menambahkan Data Tiket ===")

    def edit_tiket(self,result,Id_tiket):
        Id_film = result[0][1]
        Jam_tayang = result[0][2]
        Tanggal = result[0][3] #only date
        hari = result[0][4] #only day
        harga = result[0][5]
        stok = result[0][6]
        while True : 
            print("=== Edit value ===")
            print("1. Id film")
            print("2. Jam tayang")
            print("3. Tanggal tayang")
            print("4. Stok Kursi")
            pilih = int(input("Data yang ingin diubah : "))
            if pilih == 1 :
                Id_film = int(input("Masukan Id_film\t: "))
            elif pilih == 2 :
                time_str = (input("Masukan jam tayang (format: hh:mm:ss)\t: "))
                date_time = datetime.strptime(time_str, "%H:%M:%S")
                Jam_tayang = date_time.time()            
            elif pilih == 3 :
                date_str = input("Masukkan tanggal (format: YYYY-MM-DD)\t: ") #set date
                date = datetime.strptime(date_str, "%Y-%m-%d") #get date
                Tanggal = date.date() #only date
                hari = date.strftime("%A") #only day
                harga = self.set_harga(hari)
            elif pilih == 4 :
                stok = int(input("Masukan stok kursi\t: "))
            else : 
                print("Pilihan tidak tersedia")
            lanjut = str(input("Ganti data lain (y/n)? "))
            if lanjut == 'y' :
                continue
            else :
                break
        # quary = """INSERT INTO tiket(Id_film, Jam_tayang, Hari,Tanggal, Harga, Stok_kursi) VALUES (%s, %s, %s, %s,%s,%s)"""
        query = """UPDATE tiket SET `Id_film`= %s, `Jam_tayang`= %s, `Hari`= %s, `Tanggal`= %s, `Harga`=%s, `Stok_kursi`=%s  WHERE Id_tiket = %s"""
        data = (Id_film, Jam_tayang, hari,Tanggal,harga,stok,Id_tiket)
        self.db.insertValue(query, data)

        
    def update_tiket(self) :
        print("=== Update Tiket ===")
        Id_tiket = int(input("Masukkan ID Tiket yang akan diupdate: "))
        query = """SELECT * FROM tiket WHERE Id_tiket = %s"""
        data = (Id_tiket,)
        self.db.selectValuepretty(query, data)
        result = self.db.selectValue(query, data)
        test = str(input("Apa data ingin diupdate (y/n)? "))
        if test.lower() == 'y' :
            self.edit_tiket(result, Id_tiket)
            print("=== Anda Berhasil Meng-update Data Tiket ===")
        else :
            print("=== Anda Gagal Meng-update Data Tiket ===")

    def delete_tiket(self) :
        print("=== Delete Tiket ===")
        Id_tiket = int(input("Masukkan Id Tiket yang akan dihapus: "))
        query = """SELECT * FROM tiket WHERE Id_tiket = %s """
        data = (Id_tiket,)
        self.db.selectValuepretty(query, data)
        test = str(input("Apa data ingin dihapus (y/n)? "))
        if test.lower() == 'y' :
            query = """DELETE FROM tiket WHERE Id_tiket = %s """
            data = (Id_tiket,)
            self.db.insertValue(query, data)
            print("=== Anda Berhasil Menghapus Data Tiket ===")
            
        else :
            print("=== Anda Gagal Menghapus Data Tiket ===")
    
    def read_tiket(self) :
        print("=== Read Tiket ===")
        query = """SELECT * FROM tiket"""
        self.db.selectValuepretty(query, data=None)
        print("=== Anda Berhasil Menampilkan Data Tiket ===")

# tabel pesan
class Pesan :
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

# tabel kursi
class Kursi:
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
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
        if Judul and Jenis and Produser and Sutradara and Penulis and Produksi and Casts :
            query = """INSERT INTO film(Judul, Jenis, Produser, Sutradara, Penulis, Produksi, Casts) VALUES (%s, %s, %s, %s, %s, %s,%s)"""
            data = (Judul,Jenis, Produser,Sutradara,Penulis,Produksi,Casts)
            self.db.insertValue(query,data)
            print("=== Anda Berhasil Menambahkan Data Film ===")
        else :
            print("=== Anda Gagal Menambahkan Data Film ===")
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

# tabel tiket done
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

# tabel pesan 90%
class Pesan :
    def __init__(self, db):
        self.db = db

    def get_tiket_informasi(self) :
        query = """SELECT * FROM tiket"""
        self.db.selectValuepretty(query, data=None)
        id_tiket = int(input("Masukan Id Tiket\t\t:"))
        return id_tiket
    # done
    def insert_pesan(self):
        print("=== Input Pesan ===")
        id_penonton = int(input("Masukan Id Penonton\t\t: "))

        id_tiket = self.get_tiket_informasi()
        query1 = """SELECT * FROM tiket WHERE Id_tiket = %s"""
        result = self.db.selectValue(query1, (id_tiket,))
        Total_kursi = int(input("Masukan Total Memesan Kursi\t: "))
        harga = result[0][5]
        stok = result[0][6]
        Total_harga = Total_kursi * harga
        sisa_stok_kursi = stok - Total_kursi

        query = """INSERT INTO pesan(id_tiket, id_penonton, Total_kursi, Total_harga) VALUES (%s, %s, %s, %s)"""
        data1 = (id_tiket, id_penonton, Total_kursi, Total_harga)
        self.db.insertValue(query, data1)

        update_stok = """UPDATE tiket SET `Stok_kursi`=%s  WHERE Id_tiket = %s"""
        data2 = (sisa_stok_kursi, id_tiket)
        self.db.insertValue(update_stok,data2)
        print("=== Anda Berhasil Memesan Tiket ===")
    def edit_pesan(self, result, id_pesan) :
        id_tiket = result[0][1]
        id_penonton = result[0][2]
        total_kursi = result[0][3]
        while True : 
            print("=== Edit value ===")
            print("1. Id Tiket")
            print("2. Id Penonton")
            print("3. Total Kursi")
            pilih = int(input("Data yang ingin diubah : "))
            if pilih == 1 :
                id_tiket = int(input("Masukan Id_film\t: "))
            elif pilih == 2 :
                id_penonton= int (input("Masukan Id_film\t: "))      
            elif pilih == 3 :
                total_kursi = int(input("Masukan stok kursi\t: "))
            else : 
                print("Pilihan tidak tersedia")
            lanjut = str(input("Ganti data lain (y/n)? "))
            if lanjut == 'y' :
                continue
            else :
                break
        query = """UPDATE pesan SET `id_tiket`= %s, `id_penonton`= %s, `Total_kursi`= %s  WHERE Id_pesan = %s"""
        data = (id_tiket, id_penonton, total_kursi, id_pesan)
        self.db.insertValue(query, data)

    def update_pesan(self):
        print("=== Update Pesan ===")
        Id_pesan = int(input("Masukkan ID Pesan yang akan diupdate: "))
        query = """SELECT * FROM pesan WHERE Id_pesan = %s"""
        data = (Id_pesan,)
        self.db.selectValuepretty(query, data)
        result = self.db.selectValue(query, data)

        test = str(input("Apa data ingin diupdate (y/n)? "))
        if test.lower() == 'y' :
            self.edit_tiket(result, Id_pesan)
            print("=== Anda Berhasil Meng-update Data Pesan ===")
        else :
            print("=== Anda Gagal Meng-update Data Pesan ===")


    def delete_pesan(self):
        print("=== Delete Pesan ===")
        Id_pesan = int(input("Masukkan ID Pesan yang akan dihapus: "))

        query = """DELETE FROM pesan WHERE Id_pesan = %s """
        data = (Id_pesan,)
        self.db.selectValuepretty(query, data=None)

        test = str(input("Apa anda yakin ingin menghapus data ini (y/n)? "))
        if test.lower() == 'y' :
            self.db.insertValue(query, data)
            print("=== Anda Berhasil Menghapus Data Pesan")
        else :
            print("=== Anda Gagal Meng-update Data Pesan ===")

    def read_pesan(self):
        print("=== Read Pesan ===")
        query = """SELECT * FROM pesan"""
        result = self.db.selectValuepretty(query, data=None)

# tabel struk
class Bukti_pesan:
    def __init__(self, db):
        self.db = db

    def get_infopesan(self) :
        query = """SELECT * FROM pesan WHERE Id_pesan=%s"""
        data = int(input("Masukan Id Pesan Anda\t\t: "))
        result = self.db.selectValue(query, (data,)) 
        print(1)
        print(result)
        return result
    
    def get_infotiket(self, data) :
        query = """SELECT * FROM tiket WHERE id_tiket=%s"""
        result = self.db.selectValue(query, (data,)) 
        print(2)
        print(result)

        return result    
    
    def get_judulfilm(self,data) :
        query = """SELECT * FROM film WHERE id_film=%s"""
        result = self.db.selectValue(query, (data,)) 
        return result[0][1]
    
    def insert_buktipesan(self):
        print("=== Input Kursi ===")
        pesan = self.get_infopesan()
        id_pesan = pesan[0][0]
        id_tik = pesan[0][1]
        total_kursi = pesan[0][3]

        tiket = self.get_infotiket(id_tik)
        id_tiket = tiket[0][1]
        Jam_tayang = tiket[0][2]
        Hari = tiket[0][3]
        tanggal = tiket[0][4]
        harga = tiket[0][5]

        judul = self.get_judulfilm(id_tiket)
        Id_pegawai = str(input("Masukan Id Pegawai\t\t: "))
        for i in range(total_kursi) :
            query = """INSERT INTO bukti_pesan(Id_pesan, Id_pegawai, Judul, Jam_tayang, Hari, Tanggal, Harga) VALUES (%s, %s, %s,%s,%s,%s,%s)"""
            data = (id_pesan, Id_pegawai, judul,Jam_tayang,Hari,tanggal,harga)
            self.db.insertValue(query,data)
            i += 1

    def delete_buktipesan(self):
        print("=== Delete Bukti Pesan ===")
        Id_pesan = int(input("Masukkan ID Id_pesan yang akan dihapus: "))

        query = """DELETE FROM bukti_pesan WHERE Id_pesan = %s """
        data = (Id_pesan,)
        self.db.insertValue(query, data)
        print("=== Berhasil Menghapus Data Bukti Pesan")

    def read_buktipesan(self):
        while True :
            print("=== Read Bukti Pesan ===")
            print("=== 1. Lihat semua buktipesan ===")
            print("=== 2. Lihat bedasarkan Id_pesan")
            pilih = int(input("Pilih Menu : "))
            if pilih == 1 :
                query = """SELECT * FROM bukti_pesan"""
                self.db.selectValuepretty(query, data=None)
                print("=== Berhasil Menampilkan Data Bukti Pesan")

            elif pilih == 2 :
                Id_pesan = int(input("Masukkan ID pesan yang akan dilihat: "))
                query = """SELECT * FROM bukti_pesan WHERE Id_pesan = %s"""
                data = (Id_pesan,)
                self.db.selectValuepretty(query, data)
                print("=== Berhasil Menampilkan Data Bukti Pesan")

            else :
                print("Pilihan tidak tersedia")

            lihat = str(input("Apa ingin melihat data lagi (y/n)? "))
            if lihat.lower() == 'y' :
                continue
            else :
                break
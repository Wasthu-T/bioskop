import os
from connector import database
from createtable import film, penonton,pegawai,pesan,kursi
from query import Film, Penonton, Pegawai, Pesan, Kursi
db = database()
db.connect()
db.createTbl(film)
db.createTbl(penonton)
db.createTbl(pegawai)
db.createTbl(pesan)
db.createTbl(kursi)

while True :
    os.system('cls')
    print("="*22)
    print("=== Selamat Datang ===")
    print("=== Di Atrium XXII ===")
    print("="*22)
    print("\n==== Menu Bioskop ====")
    print("===[1] Penonton\t   ===")
    print("===[2] Pegawai\t   ===")
    print("===[3] Film\t   ===")
    print("===[4] Kursi\t   ===")
    print("===[5] Pesan\t   ===")
    print("===[0] Keluar\t   ===")
    print("="*22)
    pilih = int(input("Pilih Menu : "))
    if pilih == 1 :
        print("\n\t===== Menu Penonton =====")
        print("\t===[1] Insert Penonton ==")
        print("\t===[2] Update Penonton ==")
        print("\t===[3] Delete Penonton ==")
        print("\t===[4] Read Penonton   ==")
        print("\t=========================")
        pilih = int(input("Pilih Menu : "))
        pen = Penonton(db)
        if pilih == 1 :
            pen.insert_penonton()
            print("=== Anda Berhasil Menambahkan Data Penonton ===")
        elif pilih == 2 :
            pen.update_penonton()
            print("=== Anda Berhasil Meng-update Data Penonton ===")
        elif pilih == 3 :
            pen.delete_penonton()
            print("=== Anda Berhasil Menghapus Data Penonton ===")
        elif pilih == 4 :
            pen.read_penonton()
            print("=== Anda Berhasil Menampilkan Data Penonton ===")
        else :
            print("=== Pilihan tidak tersedia ===")
            print("=== Kembali ke menu utama ===")
        os.system('pause')
    elif pilih == 2 :
        print("\n\t===== Menu Pegawai =====")
        print("\t===[1] Insert Pegawai ==")
        print("\t===[2] Update Pegawai ==")
        print("\t===[3] Delete Pegawai ==")
        print("\t===[4] Read Pegawai   ==")
        print("\t========================")
        pilih = int(input("Pilih Menu : "))
        pgw = Pegawai(db)
        if pilih == 1 :
            pgw.insert_pegawai()
            print("=== Anda Berhasil Menambahkan Data Pegawai ===")
        elif pilih == 2 :
            pgw.update_pegawai()
            print("=== Anda Berhasil Meng-update Data Pegawai ===")
        elif pilih == 3 :
            pgw.delete_pegawai()
            print("=== Anda Berhasil Menghapus Data Pegawai ===")
        elif pilih == 4 :
            pgw.read_pegawai()
            print("=== Anda Berhasil Menampilkan Data Pegawai ===")
        else :
            print("=== Pilihan tidak tersedia ===")
            print("=== Kembali ke menu utama ===")
        os.system('pause')
    elif pilih == 3 :
        print("\n\t===== Menu Film =====")
        print("\t===[1] Insert Film ==")
        print("\t===[2] Update Film ==")
        print("\t===[3] Delete Film ==")
        print("\t===[4] Read Film   ==")
        print("\t=====================")
        pilih = int(input("Pilih Menu : "))
        f = Film(db)
        if pilih == 1 :
            f.insert_film()
            print("=== Anda Berhasil Menambahkan Data Film ===")
        elif pilih == 2 :
            f.update_film()
            print("=== Anda Berhasil Meng-update Data Film ===")
        elif pilih == 3 :
            f.delete_film()
            print("=== Anda Berhasil Menghapus Data Film ===")
        elif pilih == 4 :
            f.read_film()
            print("=== Anda Berhasil Menampilkan Data Film ===")
        else :
            print("=== Pilihan tidak tersedia ===")
            print("=== Kembali ke menu utama ===")
        os.system('pause')
    elif pilih == 4 :
        print("\n\t===== Menu Kursi =====")
        print("\t===[1] Insert Kursi ==")
        print("\t===[2] Update Kursi ==")
        print("\t===[3] Delete Kursi ==")
        print("\t===[4] Read Kursi   ==")
        print("\t=====================")
        pilih = int(input("Pilih Menu : "))
        kur = Kursi(db)
        if pilih == 1 :
            kur.insert_kursi()
            print("=== Anda Berhasil Menambahkan Data Kursi ===")
        elif pilih == 2 :
            kur.update_kursi()
            print("=== Anda Berhasil Meng-update Data Kursi ===")
        elif pilih == 3 :
            kur.delete_kursi()
            print("=== Anda Berhasil Menghapus Data Kursi ===")
        elif pilih == 4 :
            kur.read_kursi()
            print("=== Anda Berhasil Menampilkan Data Kursi ===")
        else :
            print("=== Pilihan tidak tersedia ===")
            print("=== Kembali ke menu utama ===")
        os.system('pause')
    elif pilih == 5 :
        print("\n\t===== Menu Pesan =====")
        print("\t===[1] Daftar Film  ==")
        print("\t===[2] Daftar Kursi ==")
        print("\t===[3] Beli Tiket   ==")
        print("\t======================")
        pilih = int(input("Pilih Menu : "))
        f = Film(db)
        if pilih == 1 :
            f.read_film()
            print("=== Anda Berhasil Menambahkan Data Film ===")
        elif pilih == 2 :
            f.update_film()
            print("=== Anda Berhasil Meng-update Data Film ===")
        elif pilih == 3 :
            print("\n\t===== Menu Tiket =====")
            print("\t===[1] Pesan Tiket  ==")
            print("\t===[2] Edit Tiket   ==")
            print("\t===[3] Hapus Tiket  ==")
            print("\t===[4] Lihat Tiket  ==")
            print("\t=====================")
            pilih = int(input("Pilih Menu : "))
            pes = Pesan(db)
            if pilih == 1 :
                pes.insert_pesan()
            elif pilih == 2 :
                pes.update_pesan()
            elif pilih == 3 :
                pes.delete_pesan()
            elif pilih == 4 :
                pes.read_pesan()
            else :
                print("=== Pilihan tidak tersedia ===")
                print("=== Kembali ke menu utama ===")
            os.system('pause')
    elif pilih == 0 :
        print("\t=== Terimakasih ===")
        print("=== Jangan Lupa Datang Kembali ===")
    else :
        print("Pilihan tidak tersedia")
        os.system('pause')
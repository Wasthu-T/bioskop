import os
from connector import database
from createtable import created_table
from query import Film, Penonton, Pegawai, Pesan, Tiket, Bukti_pesan
db = database()
db.connect()
created_table(db)
f = Film(db)
pen = Penonton(db)
pgw = Pegawai(db)
tik = Tiket(db)
pes = Pesan(db)


while True :
    os.system('cls')
    print("="*22)
    print("=== Selamat Datang ===")
    print("=== Di Atrium XXII ===")
    print("="*22)
    print("==== Menu Akses ====")
    print("===[1] Penonton\t   ===")
    print("===[2] Pegawai\t   ===")
    print("===[0] Keluar\t   ===")
    print("======================")
    pilih = int(input("Pilih Menu : "))
    if pilih == 1 :
        print("\n\t===== Menu Penonton =====")
        print("\t===[1] Kelola Akun ==")
        print("\t===[2] Lihat Film ==")
        print("\t===[3] Pesan ==")
        print("\t======================")

        pilih = int(input("Pilih Menu : "))
        if pilih == 1 :
            print("\n\t===== Menu Penonton =====")
            print("\t===== Kelola Akun =====")
            print("\t===[1] Insert Penonton ==")
            print("\t===[2] Update Penonton ==")
            print("\t===[3] Delete Penonton ==")
            print("\t=========================")
            pilih = int(input("Pilih Menu : "))
            if pilih == 1 :
                pen.insert_penonton()
            elif pilih == 2 :
                pen.update_penonton()
            elif pilih == 3 :
                pen.delete_penonton()
            elif pilih == 4 :
                pen.read_penonton()
                print("=== Anda Berhasil Menampilkan Data Penonton ===")
            else :
                print("=== Pilihan tidak tersedia ===")
                print("=== Kembali ke menu utama ===")

        elif pilih == 2 :
            f.read_film()
            print("=== Anda Berhasil Menampilkan Data Film ===")

        elif pilih == 3 :
            print("\n\t===== Menu Penonton =====")
            print("\t===== Pesan Tiket Bioskop =====")
            print("\t===[1] Daftar Tiket ==")
            print("\t===[2] Beli Tiket   ==")
            print("\t======================")
            pilih = int(input("Pilih Menu : "))
            if pilih == 1 :
                tik.read_tiket()
            elif pilih == 2 :
                print("\n\t===== Pesan Tiket Bioskop =====")
                print("\t===== Beli Tiket =====") #class pesan
                print("\t===[1] Pesan Tiket  ==")
                print("\t===[2] Edit Tiket   ==")
                print("\t=====================")
                pilih = int(input("Pilih Menu : "))
                if pilih == 1 :
                    pes.insert_pesan()
                elif pilih == 2 :
                    pes.update_pesan()
                else :
                    print("=== Pilihan tidak tersedia ===")
                    print("=== Kembali ke menu utama ===")

    elif pilih == 2 :
        print("\n\t===== Menu Pegawai =====")
        print("===[1] Kelola Akun\t   ===") #done
        print("===[2] Film\t   ===") #done
        print("===[3] Tiket\t   ===") #done
        print("===[4] Cetak Struck\t   ===") #progres
        print("\t========================")
        pilih = int(input("Pilih Menu : "))
        if pilih == 1 :
            print("\n\t===== Menu Pegawai =====")
            print("\t===== Kelola Akun =====")
            print("\t===[1] Insert Pegawai ==")
            print("\t===[2] Update Pegawai ==")
            print("\t===[3] Delete Pegawai ==")
            print("\t===[4] Read Pegawai   ==")
            print("\t========================")
            pilih = int(input("Pilih Menu : "))
            if pilih == 1 :
                pgw.insert_pegawai()
            elif pilih == 2 :
                pgw.update_pegawai()
            elif pilih == 3 :
                pgw.delete_pegawai()
            elif pilih == 4 :
                pgw.read_pegawai()
                print("=== Anda Berhasil Menampilkan Data Pegawai ===")
            else :
                print("=== Pilihan tidak tersedia ===")
                print("=== Kembali ke menu utama ===")
   
        elif pilih == 2 :
            print("\n\t===== Menu Pegawai =====")
            print("\t===== Kelola Film =====")
            print("\t===[1] Insert Film ==")
            print("\t===[2] Update Film ==")
            print("\t===[3] Delete Film ==")
            print("\t===[4] Read Film   ==")
            print("\t=====================")
            pilih = int(input("Pilih Menu : "))
            if pilih == 1 :
                f.insert_film()
            elif pilih == 2 :
                f.update_film()
            elif pilih == 3 :
                f.delete_film()
            elif pilih == 4 :
                f.read_film()
                print("=== Anda Berhasil Menampilkan Data Film ===")
            else :
                print("=== Pilihan tidak tersedia ===")
                print("=== Kembali ke menu utama ===")

        elif pilih == 3 :
            print("\n\t===== Menu Pegawai =====")
            print("\t===== Kelola Tiket =====")
            print("\t===[1] Insert Tiket ==")
            print("\t===[2] Update Tiket ==")
            print("\t===[3] Delete Tiket ==")
            print("\t===[4] Read Tiket   ==")
            print("\t=====================")
            pilih = int(input("Pilih Menu : "))
            if pilih == 1 :
                tik.insert_tiket()
            elif pilih == 2 :
                tik.update_tiket()
            elif pilih == 3 :
                tik.delete_tiket()
            elif pilih == 4 :
                tik.read_tiket()
            else :
                print("=== Pilihan tidak tersedia ===")
                print("=== Kembali ke menu utama ===")
    
        elif pilih == 4 :
            print("\n\t===== Menu Struck =====")
            print("\t===[1] Insert Struck ==")
            print("\t===[2] Read Struck   ==")
            print("\t=====================")
            pilih = int(input("Pilih Menu : "))
            Bp = Bukti_pesan(db)
            if pilih == 1 :
                Bp.insert_buktipesan()
            elif pilih == 2 :
                Bp.read_buktipesan()
            else :
                print("=== Pilihan tidak tersedia ===")
                print("=== Kembali ke menu utama ===")
        else :
            print("=== Pilihan tidak tersedia ===")
            print("=== Kembali ke menu utama ===")
        
    elif pilih == 0 :
        print("\t=== Terimakasih ===")
        print("=== Jangan Lupa Datang Kembali ===")
        break

    else :
        print("Pilihan tidak tersedia")
    os.system('pause')

import os

while True :
    os.system('cls')
    print("=== Menu Bioskop ===")
    print("1. Penonton")
    print("2. Pegawai")
    print("0. Keluar")
    pilih = int(input("Pilih Menu : "))
    if pilih == 1 :
        print("=== Menu Penonton ===")
        print("1. Daftar film")
        print("2. Pesan tiket")
        pilih = int(input("Pilih Menu : "))
        if pilih == 1 :
            # Judul
            # Durasi
            # Jenis 
            # Produser
            # Sutradara
            # Penulis
            # Produksi
            # Casts
            pass
        elif pilih == 2 :
            # Judul
            # Kursi
            pass
        else :
            print("Pilihan tidak tersedia")
            print("Kembali ke menu utama")
            os.system('pause')
    elif pilih == 2 :
        print("=== Menu Pegawai ===")
        print("1. Film")
        print("2. Kursi")
        pilih = int(input("Pilih Menu : "))
        if pilih == 1 :
            pass
        elif pilih == 2 :
            pass
        else :
            print("Pilihan tidak tersedia")
            print("Kembali ke menu utama")
            os.system('pause')
    elif pilih == 0 :
        print("Keluar")
    else :
        print("Pilihan tidak tersedia")
        os.system('pause')
    
from connector import database

penonton ='''CREATE TABLE IF NOT EXISTS Penonton(
   Id_penonton int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
   Nama varchar(200) NOT NULL,
   Email varchar(200) NOT NULL UNIQUE,
   Nomor varchar(30) NOT NULL UNIQUE,
   Password varchar(200) not null
    );
'''

pegawai = '''CREATE TABLE IF NOT EXISTS Pegawai(
   Id_pegawai int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
   Nama varchar(200) NOT NULL,
   Email varchar(200) NOT NULL UNIQUE,
   Nomor varchar(30) NOT NULL UNIQUE,
   Usia varchar(200) not null,
   Jenis_kelamin ENUM('Laki-laki', 'Perempuan') NOT NULL
    );
'''

film = '''CREATE TABLE IF NOT EXISTS Film(
   Id_film int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
   Judul varchar(200) ,
   Jenis varchar(200) ,
   Produser varchar(200) ,
   Sutradara varchar(200),
   Penulis varchar(200),
   Produksi varchar(200),
   Casts varchar(200)
    );
'''
tiket = '''CREATE TABLE IF NOT EXISTS Tiket(
   Id_tiket int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
   Id_film int(10),
   Jam_tayang time ,
   Hari varchar(20) ,
   Tanggal date,
   Harga int(20),
   Stok_kursi int(10),
   FOREIGN KEY(Id_film) REFERENCES film(Id_film) ON DELETE CASCADE
   
    );
'''

pesan = '''CREATE TABLE IF NOT EXISTS Pesan(
   Id_pesan int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
   Id_tiket int(10),
   Id_penonton int(10),
   Total_kursi int(10),
   Total_harga int(20),
   FOREIGN KEY(Id_tiket) REFERENCES tiket(Id_tiket) ON DELETE CASCADE,
   FOREIGN KEY(Id_penonton) REFERENCES penonton(Id_penonton) ON DELETE CASCADE
    );
'''

bukti = '''CREATE TABLE IF NOT EXISTS Bukti_pesan(
   Id_pesan int(10),
   Id_pegawai int(10),
   Judul varchar(200),
   Jam_tayang time ,
   Hari varchar(20) ,
   Tanggal date,
   Harga int(20),
   FOREIGN KEY(Id_pesan) REFERENCES pesan(Id_pesan) ON DELETE CASCADE,
   FOREIGN KEY(Id_pegawai) REFERENCES pegawai(Id_pegawai) ON DELETE CASCADE
    );
'''



def created_table(db) :
    db.createTbl(film)
    db.createTbl(penonton)
    db.createTbl(pegawai)
    db.createTbl(tiket)
    db.createTbl(pesan)
    db.createTbl(bukti)
    print("Tabel berhasil dibuat")
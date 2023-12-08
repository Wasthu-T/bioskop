
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

Pesan = '''CREATE TABLE IF NOT EXISTS Pesan(
   Id_pesan int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
   Judul varchar(200) ,
   Kursi varchar(200) ,
   hari varchar(20) ,
   jam datetime,
   tgl date,
   Harga varchar(200)
    );
    '''
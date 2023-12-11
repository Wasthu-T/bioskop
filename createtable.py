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

pesan = '''CREATE TABLE IF NOT EXISTS Pesan(
   Id_pesan int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
   Judul varchar(200) ,
   Nomor_kursi varchar(200) ,
   Jenis_kursi ENUM('Reguler', 'VIP', 'Premium', 'Khusus') NOT NULL,
   Hari varchar(20) ,
   Jam time,
   Tgl date,
   Harga varchar(200)
    );
'''

kursi = '''CREATE TABLE IF NOT EXISTS Kursi(
   Id_kursi int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
   Nomor_kursi varchar(200) NOT NULL,
   Jenis_kursi ENUM('Reguler', 'VIP', 'Premium', 'Khusus') NOT NULL,
   Id_Ruangan varchar(200) NOT NULL UNIQUE
    );
'''
# -- Data untuk tabel Penonton
penonton = """INSERT INTO Penonton (Nama, Email, Nomor, Password) VALUES
('Wasthutatya', 'Wasthutatya@gmail.com', '081234513', 'qwerty123'),
('David Bagas Santoso', 'David@gmail.com', '089765423', 'asdfg123'),
('Tsani Nur Syabani', 'Tsani@gmail.com', '089764231', 'zxcvb123');"""

# -- Data untuk tabel Pegawai
pegawai = """INSERT INTO Pegawai (Nama, Email, Nomor, Usia, Jenis_kelamin) VALUES
('Jusuf Ahmad', 'emma@example.com', '555123456', '28', 'Laki-laki'),
('Anisa Zulkifar', 'david@example.com', '555987654', '32', 'Perempuan'),
('Fatimah Ratu', 'sophia@example.com', '555456789', '25', 'Perempuan');"""

# -- Data untuk tabel Film
film = """INSERT INTO Film (Judul, Jenis, Produser, Sutradara, Penulis, Produksi, Casts) VALUES
('Siksa Neraka', 'Horor', 'Dheeraj Kalwani', 'Anggy Umbara', 'Lele Laila', 'Dee Company', 'Ratu Sofya, Rizky Fachrel'),
('The Animal Kingdom', 'Petualangan', 'Pierre Guyard', 'Thomas Cailley', 'Pauline Munier', 'Studio Canal', 'Romain Duris, Paul Kircher'),
('Wonka', 'Fantasi', 'Alexandra Derbyshire', 'Paul King', 'Simon Farnaby', 'Timothee Chalamet', ',Olivia Colman');"""

# -- Data untuk tabel Tiket
tiket ="""INSERT INTO Tiket (Id_film, Jam_tayang, Hari, Tanggal, Harga, Stok_kursi) VALUES
(1, '13:00:00', 'Senin', '2023-12-18', 30000, 88),
(2, '15:30:00', 'Jumat', '2023-12-22', 35000, 77),
(3, '18:00:00', 'Minggu', '2023-12-24', 40000, 98);"""

# -- Data untuk tabel Pesan
pesan = """INSERT INTO Pesan (Id_tiket, Id_penonton, Total_kursi, Total_harga) VALUES
(1, 1, 2, 60000),
(2, 2, 3, 70000),
(3, 3, 2, 80000);"""

def created_data(db) :
    db.create(film)
    db.create(penonton)
    db.create(pegawai)
    db.create(tiket)
    db.create(pesan)
    print("Data Sampel berhasil dibuat")
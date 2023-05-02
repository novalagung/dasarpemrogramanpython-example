#%% Deklarasi variabel
nama = "noval"
hobi = 'makan'
umur = 18
laki = True

print("==== biodata ====")
print("nama: %s" % (nama))
print("hobi: %s, umur: %d, laki: %r" % (hobi, umur, laki))

#%% Naming convention variabel

pesan = 'halo, selamat pagi'
nilai_ujian = 99.2

#%% Operasi assignment
nama = "noval"
umur = 18
nama = "noval agung"
umur = 21

#%% Deklarasi tipe data variabel
nama: str = "noval"
hobi: str = 'makan'
umur: int = 18
laki: bool = True
nilai_ujian: float = 99.2

#%% Deklarasi banyak variabel dalam satu baris
nilai1, nilai2, nilai3, nilai4 = 24, 25, 26, 21
nilai_rata_rata = (nilai1 + nilai2 + nilai3 + nilai4) / 4

print("rata-rata nilai: %f" % (nilai_rata_rata))

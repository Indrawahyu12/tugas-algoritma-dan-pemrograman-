import math

# Meminta pengguna memasukkan nilai jari-jari
r = float(input("Masukkan nilai jari-jari lingkaran: "))

# Menghitung luas lingkaran
luas = math.pi * (r ** 2)

# Menampilkan hasil
print("Luas lingkaran dengan jari-jari", r, "adalah:", round(luas, 2))
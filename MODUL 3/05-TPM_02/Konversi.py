# Meminta input suhu dalam Fahrenheit dari pengguna
fahrenheit = float(input("Masukkan suhu dalam F: "))

# Mengonversi suhu ke Celsius menggunakan rumus (F-32) 5/9 
celsius = (fahrenheit - 32) * 5/9

# Menampilkan hasil konversi 
print(f"{fahrenheit}°F konvensi F-C {celsius:.2f}°C")
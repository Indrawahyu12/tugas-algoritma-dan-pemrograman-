def hitung_diskon(nama_pelanggan, status_member, total_belanja):
    # Menentukan potongan berdasarkan kriteria yang diberikan
    if status_member == "ya":  # Pelanggan dengan kartu member
        if total_belanja > 500000:
            diskon_persen = 10  # Potongan 10%
        elif 100000 < total_belanja <= 499999:
            diskon_persen = 0  # Tidak ada potongan
        else:
            diskon_persen = 3  # Potongan 3%
    else:  # Pelanggan tanpa kartu member
        if total_belanja > 100000:
            diskon_persen = 3  # Potongan 3%
        else:
            diskon_persen = 0  # Tidak ada potongan
    
    # Menghitung diskon dalam rupiah
    diskon_rupiah = total_belanja * (diskon_persen / 100)
    # Menghitung total belanja setelah potongan
    total_belanja_setelah_potongan = total_belanja - diskon_rupiah
    
    # Menampilkan hasil
    print("Nama Pelanggan:", nama_pelanggan)
    print("Status Kartu Member:", "Ada" if status_member == "ya" else "Tidak Ada")
    print("Total Belanja Sebelum Potongan: Rp", format(total_belanja, ",.2f"))
    print("Diskon (dalam persen):", diskon_persen, "%")
    print("Diskon (dalam Rupiah): Rp", format(diskon_rupiah, ",.2f"))
    print("Total Belanja Setelah Potongan: Rp", format(total_belanja_setelah_potongan, ",.2f"))

# Input data pelanggan
nama_pelanggan = input("Masukkan nama pelanggan: ")
status_member = input("Apakah pelanggan memiliki kartu member (ya/tidak): ").strip().lower()
total_belanja = float(input("Masukkan total belanja: "))

# Memanggil fungsi untuk menghitung diskon dan menampilkan hasil
hitung_diskon(nama_pelanggan, status_member, total_belanja)

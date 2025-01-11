Mulai
    Masukkan Nama_Pelanggan
    Masukkan Status_Kartu_Member (ya/tidak)
    Masukkan Total_Belanja

    Jika Status_Kartu_Member = "ya"
        Jika Total_Belanja > 500000
            Potongan_Persen = 10
        Jika Total_Belanja >= 100000 dan Total_Belanja <= 499999
            Potongan_Persen = 0
        Jika Total_Belanja < 100000
            Potongan_Persen = 3
    Jika Status_Kartu_Member = "tidak"
        Jika Total_Belanja > 100000
            Potongan_Persen = 3
        Jika Total_Belanja <= 100000
            Potongan_Persen = 0

    Diskon_Rupiah = Total_Belanja * Potongan_Persen / 100
    Total_After_Discount = Total_Belanja - Diskon_Rupiah

    Tampilkan "Nama Pelanggan: ", Nama_Pelanggan
    Tampilkan "Status Kartu Member: ", Status_Kartu_Member
    Tampilkan "Total Belanja Sebelum Potongan: ", Total_Belanja
    Tampilkan "Potongan: ", Potongan_Persen, "%"
    Tampilkan "Diskon (Dalam Rupiah): ", Diskon_Rupiah
    Tampilkan "Total Belanja Setelah Potongan: ", Total_After_Discount
Selesai

def hitung_diskon(total_belanja, kartu_member):
    if kartu_member == "ya":
        if total_belanja > 500000:
            diskon_persen = 10
        elif total_belanja >= 100000 and total_belanja <= 499999:
            diskon_persen = 0
        else:
            diskon_persen = 3
    else:
        if total_belanja > 100000:
            diskon_persen = 3
        else:
            diskon_persen = 0

    diskon_rupiah = total_belanja * diskon_persen / 100
    total_setelah_diskon = total_belanja - diskon_rupiah
    return diskon_persen, diskon_rupiah, total_setelah_diskon


def main():
    nama_pelanggan = input("Masukkan Nama Pelanggan: ")
    kartu_member = input("Apakah Anda memiliki kartu member (ya/tidak)? ").lower()
    total_belanja = float(input("Masukkan Total Belanja: "))

    diskon_persen, diskon_rupiah, total_setelah_diskon = hitung_diskon(total_belanja, kartu_member)

    print("\nInformasi Pembelian:")
    print(f"Nama Pelanggan: {nama_pelanggan}")
    print(f"Status Kartu Member: {kartu_member.capitalize()}")
    print(f"Total Belanja Sebelum Potongan: Rp {total_belanja:,.0f}")
    print(f"Diskon: {diskon_persen}%")
    print(f"Diskon (Dalam Rupiah): Rp {diskon_rupiah:,.0f}")
    print(f"Total Belanja Setelah Potongan: Rp {total_setelah_diskon:,.0f}")


if __name__ == "__main__":
    main()

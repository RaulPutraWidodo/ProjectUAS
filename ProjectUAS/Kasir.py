menu = {
    1: {"nama": "Nasi Goreng", "harga": 10000},
    2: {"nama": "Soto Ayam", "harga": 15000},
    3: {"nama": "Es Teh", "harga": 5000},
    4: {"nama": "Es Jeruk", "harga": 6000}
}

def tampilkan_menu():
    print("Menu Makanan/Minuman:")
    for nomor, item in menu.items():
        print(f"{nomor}. {item['nama']}: Rp {item['harga']}")

def hitung_total(pesanan):
    total = 0
    for nomor in pesanan:
        if nomor in menu:
            total += menu[nomor]["harga"]
    return total

def main():
    pesanan = []
    tampilkan_menu()

    while True:
        pilihan = input("Pilih menu (ketik 'selesai' untuk menyelesaikan pesanan): ")
        
        if pilihan.lower() == 'selesai':
            break

        try:
            nomor = int(pilihan)
            if nomor in menu:
                pesanan.append(nomor)
            else:
                print("Nomor menu tidak valid. Silakan pilih nomor menu yang tersedia.")
        except ValueError:
            print("Masukkan nomor menu yang valid.")

    total_harga = hitung_total(pesanan)

    print("\nStruk Pembelian:")
    for nomor in pesanan:
        item = menu[nomor]
        print(f"{item['nama']}: Rp {item['harga']}")

    print(f"\nTotal Harga: Rp {total_harga}")

if __name__ == "__main__":
    main()

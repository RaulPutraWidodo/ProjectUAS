# Project_UAS

|NAMA   | Raul Putra Widodo |
| --- | --- |
| NIM    | 312310610 |
| KELAS  | TI.23.A6 |
| DOSEN  | Agung Nugroho,S.Kom.,M.Kom |


# Kode Sederhana
```python
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
```


# Langkah-langkah membuat program sederhana kasir dengan python 
Program yang Anda berikan adalah program kasir sederhana menggunakan Python dengan format dictionary. Berikut adalah penjelasan rinci mengenai setiap bagian dari program:
```python
1. **Menu Makanan/Minuman:**
   - Pada fungsi `tampilkan_menu()`, program menampilkan menu makanan/minuman beserta nomor dan harga menggunakan perulangan `for`.

2. **Hitung Total Harga Pesanan:**
   - Fungsi `hitung_total(pesanan)` digunakan untuk menghitung total harga pesanan. Program melakukan iterasi melalui pesanan yang telah dibuat dan menambahkan harga masing-masing item ke total.

3. **Main Function:**
   - Fungsi `main()` adalah fungsi utama yang menjalankan program kasir.
   - Pertama-tama, program memanggil `tampilkan_menu()` untuk menampilkan opsi menu kepada pengguna.
   - Selanjutnya, program masuk ke dalam loop `while True` untuk meminta pengguna memilih menu. Pengguna dapat memasukkan nomor menu atau mengetik 'selesai' untuk menyelesaikan pesanan.
   - Dalam loop, program mencoba mengonversi input pengguna ke integer. Jika berhasil, itu dianggap sebagai nomor menu, dan program memeriksa apakah nomor menu tersebut valid. Jika valid, nomor menu ditambahkan ke dalam pesanan; jika tidak valid, pesan kesalahan ditampilkan.
   - Jika input tidak dapat diubah menjadi integer, program menampilkan pesan kesalahan.
   - Setelah pengguna selesai memasukkan pesanan, program menghitung total harga menggunakan fungsi `hitung_total(pesanan)`.
   - Program kemudian menampilkan struk pembelian, mencetak nama dan harga setiap item pesanan, dan total harga keseluruhan.

4. **Eksekusi Program:**
   - Terakhir, blok `if __name__ == "__main__":` memastikan bahwa program hanya dijalankan jika script ini dieksekusi langsung (bukan diimpor sebagai modul oleh script lain).
```

Untuk menjalankan program ini, cukup salin kode ke dalam file Python dan jalankan. Program akan menampilkan menu, meminta pengguna untuk memilih, dan memberikan struk pembelian dengan total harga.# ProjectUAS

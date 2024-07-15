from tabulate import tabulate as tb

Rental_Mobil = {
    "Nama Mobil": ["Yaris", "Avanza", "Brio", "Jazz", "Innova", "APV", "Pajero", "Xenia", "Grand Max", "Terios", "Rush", "Rubicon"],
    "Stock": [11, 5, 6, 10, 9, 4, 5, 3, 7, 8, 9, 2],
    "Harga": [250000, 300000, 275000, 325000, 500000, 275000, 650000, 250000, 225000, 350000, 350000, 1500000],
    "Hari" : [30, 7, 5, 6, 3, 8, 4, 24, 27, 63, 43, 8],
    "Merk": ["Toyota", "Toyota", "Honda", "Honda", "Toyota", "Suzuki", "Mitsubisi", "Daihatsu", "Daihatsu", "Daihatsu", "Toyota", "Jeep"],
    "Jenis": ["HATCHBACK", "MPV", "HATCHBACK", "HATCHBACK", "SUV", "MPV", "SUV", "MPV", "MVP", "MPV", "MPV", "OFF ROAD"],
}

def Daftar_Mobil():     # PILIHAN 1. MENAMPILKAN DAFTAR MOBIL
    headers = Rental_Mobil.keys()
    print(tb(Rental_Mobil, showindex="always", headers=headers, tablefmt="github",))
    print()
    while True:
        try:
            print("\n1.Main menu 2.Keluar Program")
            main_menu = int(input("Masukan kode yang akan diinput: "))
            if main_menu == 1:
                rental()
            elif main_menu == 2:
                exit_program()
            else:
                print("\nPilihan tidak valid, Silahkan masukkan lagi")
            break
        except ValueError:
            print("\nMasukan tidak valid. Silakan masukkan nomor pilihan yang valid.")
        

def Menambah_Mobil():   # PILIHAN 2. MENAMBAHKAN MOBIL
    headers = Rental_Mobil.keys()
    print(tb(Rental_Mobil, showindex="always", headers=headers, tablefmt="github",))
    print()
    while True:
        try:
            tambah_mobil = input("\nMasukkan nama Mobil yang ingin ditambahkan: ").capitalize()
            Jumlah_Stock = int(input("\nMasukkan jumlah yang ingin ditambahkan: "))
            Harga_Sewa = int(input("\nMasukkan harga uang sewa yang ingin ditambahkan: "))
            Hari = int(input("\nMasukkan berapa hari bisa menyewa: "))
            Merk_Mobil = input("\nMasukkan Merk mobil: ").capitalize()
            Jenis_Mobil = input("\nMasukkan jenis mobil: ").upper()

            tambah_konfirmasi = input(f"Apakah kamu yakin ingin menambahkan {tambah_mobil}? (Y/N): ").lower()
            if tambah_konfirmasi == "y":
                Rental_Mobil["Nama Mobil"].append(tambah_mobil)
                Rental_Mobil["Harga"].append(Harga_Sewa)
                Rental_Mobil["Hari"].append(Hari)
                Rental_Mobil["Jenis"].append(Jenis_Mobil)
                Rental_Mobil["Merk"].append(Merk_Mobil)
                Rental_Mobil["Stock"].append(Jumlah_Stock)
                print(f"Mobil {tambah_mobil} berhasil ditambahkan.")
                break

            elif tambah_konfirmasi == "n":
                print("\nBatalkan penambahan.")
                break
            else:
                print("\nPilihan tidak valid. Silakan masukkan 'Y' untuk konfirmasi atau 'N' untuk membatalkan.")
        except ValueError:
            print("\nMasukan tidak valid. Silakan masukkan nomor pilihan yang valid.")
    # Setelah menambahkan mobil, minta pengguna untuk tindakan lebih lanjut     
    while True:
        try:
            print("\n 1. Main menu 2.Menambahkan Mobil Kembali 3.Keluar Program")
            main_menu = int(input("\nMasukan kode yang akan diinput: "))
            if main_menu == 1: # Dengan asumsi `rental()` adalah fungsi utama Anda untuk menampilkan opsi
                rental()
            elif main_menu == 2: # Panggil fungsi tambah mobil secara rekursif jika pengguna memilih
                Menambah_Mobil()
            elif main_menu == 3: # Untuk keluar dari program (jika diterapkan)
                exit_program()
            else:
                print("\nPilihan tidak valid, Silahkan masukkan lagi")
        except ValueError:
            print("\nMasukan tidak valid. Silakan masukkan nomor pilihan yang valid.")

def edit_mobil() : # PILIHAN 3 EDIT MOBIL
    headers = Rental_Mobil.keys()
    print(tb(Rental_Mobil, showindex="always", headers=headers, tablefmt="github",))
    print()
    try:
        while True:
            print("""
List Menu Edit:
1.Main Menu
2.Edit Stock
3.Edit Harga
4.Edit Hari
5.Edit Merk
6.Edit Jenis
7.Keluar Program """
                  )
            main_menu = int(input("Masukan kode yang akan diinput: "))
            if main_menu == 1:
                rental()
            elif main_menu == 2:
                edit_stock()
            elif main_menu == 3:
                edit_harga()
            elif main_menu == 4:
                edit_hari()
            elif main_menu == 5:
                edit_merk()
            elif main_menu == 6:  
                edit_jenis()
            elif main_menu == 7: 
                exit_program()
            else:
                print("\nPilihan tidak valid, Silahkan masukkan lagi")
    except ValueError:
        print("\nMasukan tidak valid. Silakan masukkan nomor pilihan yang valid.")

    while True: # MENGEDIT NAMA MOBIL 1A.
        try:
            editnama = int(input("\nMasukkan indeks Nama Mobil yang mau diedit: "))
            if 0 <= editnama < len(Rental_Mobil["Nama Mobil"]):

                new_name = input(f"Masukkan Nama Mobil yang baru untuk indeks  {editnama} : ").capitalize()
                Rental_Mobil["Nama Mobil"][editnama] = new_name
                print("\nNama Mobil berhasil diubah")
                break
            else:
                print("\nPilihan tidak valid, Silahkan masukkan lagi")
        except ValueError:
            print("\nMasukan tidak valid. Silakan masukkan nomor pilihan yang valid.")

def edit_stock(): # MENGEDIT STOCK MOBIL 2A.
    headers = Rental_Mobil.keys()
    print(tb(Rental_Mobil, showindex="always", headers=headers, tablefmt="github",))
    print()
    while True:
        try:
            editstock = int(input("\nMasukkan indeks Stock yang mau diedit: "))
            if 0 <= editstock < len(Rental_Mobil["Stock"]):

                new_name = int(input(f"Masukkan Stock yang baru untuk indeks {editstock}: "))
                Rental_Mobil["Stock"][editstock] = new_name
                print("\nStock mobil berhasil diubah")
                break
            else:
                print("\nPilihan tidak valid, Silahkan masukkan lagi")
        except ValueError:
            print("\nMasukan tidak valid. Silakan masukkan nomor pilihan yang valid.")

def edit_harga(): # MENGEDIT HARGA MOBIL 3A.
    headers = Rental_Mobil.keys()
    print(tb(Rental_Mobil, showindex="always", headers=headers, tablefmt="github",))
    print()
    while True:
        try:
            editharga = int(input("\nMasukkan indeks Harga yang mau diedit: "))
            if 0 <= editharga < len(Rental_Mobil["Harga"]):
                new_name = int(input(f"Masukkan indeks Harga yang mau diedit {editharga}: "))
                Rental_Mobil["Harga"][editharga] = new_name
                print("\nHarga berhasil diubah")
                break
            else:
                print("\nPilihan tidak valid, Silahkan masukkan lagi")
        except ValueError:
            print("\nMasukan tidak valid. Silakan masukkan nomor pilihan yang valid.")

def edit_hari(): # MENGEDIT HARI 4A.
    headers = Rental_Mobil.keys()
    print(tb(Rental_Mobil, showindex="always", headers=headers, tablefmt="github",))
    print()
    while True:
        try:
            edithari = int(input("\nMasukkan indeks hari yang mau diedit"))
            if 0 <= edit_hari < len(Rental_Mobil["Hari"]):
                new_name = str(input(f"Masukkan indeks Merk yang mau diedit {edithari}: ")).capitalize()
                Rental_Mobil["Hari"][edithari] = new_name
                print("\nHari berhasil diubah")
                break
            else:
                print("\nPilihan tidak valid, Silahkan masukkan lagi")
        except ValueError:
            print("\nMasukan tidak valid. Silakan masukkan nomor pilihan yang valid.")

def edit_merk(): # MENGEDIT MERK MOBIL 5A.
    headers = Rental_Mobil.keys()
    print(tb(Rental_Mobil, showindex="always", headers=headers, tablefmt="github",))
    print()
    while True:
        try:
            editmerk = int(input("\nMasukkan indeks Merk yang mau diedit: "))
            if 0 <= editmerk < len(Rental_Mobil["Merk"]):
                new_name = str(input(f"Masukkan indeks Merk yang mau diedit {editmerk}: ")).capitalize()
                Rental_Mobil["Merk"][editmerk] = new_name
                print("\nMerk berhasil diubah")
                break
            else:
                print("\nPilihan tidak valid, Silahkan masukkan lagi")
        except ValueError:
            print("\nMasukan tidak valid. Silakan masukkan nomor pilihan yang valid.")

def edit_jenis():  # MENGEDIT JENIS MOBIL 6A.
    headers = Rental_Mobil.keys()
    print(tb(Rental_Mobil, showindex="always", headers=headers, tablefmt="github",))
    print()
    while True:
        try:
            editjenis = int(input("\nMasukkan indeks Jenis yang mau diedit: "))
            if 0 <= editjenis < len(Rental_Mobil["Jenis"]):
                new_name = str(input(f"Masukkan indeks Jenis yang mau diedit {editjenis}: ")).upper()
                Rental_Mobil["Jenis"][editjenis] = new_name
                print("\nJenis berhasil diubah")
                break
            else:
                print("\nPilihan tidak valid, Silahkan masukkan lagi")
        except ValueError:
            print("\nMasukan tidak valid. Silakan masukkan nomor pilihan yang valid.")

def Menghapus_Mobil():  # PILIHAN 4 MENGHAPUS MOBIL
    headers = Rental_Mobil.keys()
    print(tb(Rental_Mobil, showindex="always", headers=headers, tablefmt="github",))
    print()
    while True:
        try:
            hapus_mobil = int(input("\nMasukkan indeks mobil yang akan dihapus: "))
            if 0 <= hapus_mobil < len(Rental_Mobil["Nama Mobil"]):
                del Rental_Mobil["Nama Mobil"][hapus_mobil]
                del Rental_Mobil["Harga"][hapus_mobil]
                del Rental_Mobil["Stock"][hapus_mobil]
                del Rental_Mobil["Jenis"][hapus_mobil]
                del Rental_Mobil["Merk"][hapus_mobil]
                del Rental_Mobil["Hari"][hapus_mobil]
                print(f"Mobil berhasil dihapus.")
                break
            else:
                print("\nPilihan tidak valid, Silahkan masukkan lagi")
        except ValueError:
            print("\nMasukan tidak valid. Silakan masukkan nomor pilihan yang valid.")

    while True:
        try:
            print("\n1.Main menu 2.Menghapus kembali 3.Keluar Program")
            main_menu = int(input("Masukan kode yang akan diinput: "))
            if main_menu == 1:
                rental()
            elif main_menu == 2:
                Menghapus_Mobil()
            elif main_menu == 3:
                exit_program()
            else:
                print("\nPilihan tidak valid, Silahkan masukkan lagi")
        except ValueError:
            print("\nMasukan tidak valid. Silakan masukkan nomor pilihan yang valid.")

def Menyewa_Mobil():    # PILIHAN 5 MENYEWA MOBIL
    headers = Rental_Mobil.keys()
    print(tb(Rental_Mobil, showindex="always", headers=headers, tablefmt="github",))
    print()
    while True:
        try:
            indexsewa = int(input("\nMasukkan indeks mobil yang ingin disewa: "))
            if 0 <= indexsewa < len(Rental_Mobil["Nama Mobil"]):
                break
            else:
                print("\nMobil tidak tersedia.")
        except ValueError:
            print("\nMasukan tidak valid. Silakan masukkan nomor pilihan yang valid.")

    while True:     # Mobil yang akan disewa
        try:
            jumlahsewa = int(input("\nMasukkan jumlah mobil yang ingin disewa: "))
            if jumlahsewa > Rental_Mobil["Stock"][indexsewa]:
                print(f"Maaf, jumlah stock {Rental_Mobil['Nama Mobil'][indexsewa]} hanya tersedia {Rental_Mobil['Stock'][indexsewa]}.")
            else:
                break
        except ValueError:
            print("\nMasukan tidak valid. Silakan masukkan nomor pilihan yang valid.")

    while True:     # Berapa hari akan disewa
        try:
            jumlahhari = int(input("\nMasukkan berapa Hari yang ingin disewa: "))
            if jumlahhari > Rental_Mobil["Hari"][indexsewa]:
                print(f"Maaf, hanya bisa menyewa {Rental_Mobil['Hari'][indexsewa]} Hari.")
            else:
                break
        except ValueError:
            print("\nMasukan tidak valid. Silakan masukkan nomor pilihan yang valid.")

    # Menghitung total biaya berdasarkan mobil dan jumlah hari
    Rental_Mobil["Stock"][indexsewa] -=jumlahsewa
    totalsewa = jumlahsewa * Rental_Mobil["Harga"][indexsewa]
    totalsemua = totalsewa * jumlahhari
    print(f"Total yang harus dibayar : {totalsemua}")

    while True:     # Pembayaran
        try:
            total_uang = int(input("\nMasukkan uang Anda: "))
            if total_uang < totalsemua:
                print(f"Uang Anda kurang {totalsemua - total_uang}")
            else:
                break
        except ValueError:
            print("\nMasukan tidak valid. Silakan masukkan nomor pilihan yang valid.")

    if total_uang > totalsemua:
        print(f"Uang kembalian anda: {total_uang - totalsemua}")
        print("\nTerima kasih!")
 
    while True:
        try:
            print("\n1. Main Menu 2.Sewa Mobil Kembali 3.Keluar Program")
            main_menu = int(input("Masukan kode yang akan diinput: "))
            if main_menu == 1:
                rental()
            elif main_menu == 2:
                Menyewa_Mobil()
            elif main_menu == 3:
                exit_program()
            else:
                print("\nPilihan tidak valid, Silahkan masukkan lagi")
        except ValueError:
            print("\nMasukan tidak valid. Silakan masukkan nomor pilihan yang valid.")
        
def exit_program():  # PILIHAN 6
    while True:
        try:
            print("\nApakah anda yakin keluar dari Rental Mobil SARAGICAR")  
            menu_exit = input("\nKonfirmasi 'Y' untuk keluar dari Program atau 'N' untuk kembali ke Menu: ").lower()
            if menu_exit == 'y':
                exit("\nKeluar dari Program.")
            elif menu_exit == 'n':
                rental()
            else:
                print('\nPilihan tidak valid, Silahkan masukkan lagi')
        except ValueError:
            print("\nTidak Valid, Silahkan Konfirmas 'Y' atau 'N': ")

def rental():
    global pilih       
    while True:
        print("\nSelamat Datang di Rental Mobil")
        print("\n==========SARAGICAR==========")
        print()
        print()
        print("List Menu:")
        print("1. Menampilkan Daftar Mobil")
        print("2. Menambah Mobil")
        print("3. Edit mobil")
        print("4. Menghapus Mobil")
        print("5. Menyewa Mobil")
        print("6. Keluar Program")
        try:
            pilih = int(input("\nMasukkan kode yang mau diakses: "))
            if pilih == 1:
                Daftar_Mobil()
            elif pilih == 2:
                Menambah_Mobil()
            elif pilih == 3:
                edit_mobil()
            elif pilih == 4:
                Menghapus_Mobil()
            elif pilih == 5:
                Menyewa_Mobil() 
            elif pilih == 6:
                exit_program()
                print("\nKeluar dari Program.")
                break
            else:
                print("\nPilihan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("\nMasukan tidak valid. Silakan masukkan nomor pilihan yang valid.")

rental()

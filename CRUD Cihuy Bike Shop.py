import pandas as pd #untuk menampilkan data
from tabulate import tabulate #untuk menampilkan tabel
from datetime import datetime #untuk menampilkan waktu di file

# List Data Stok
data_stok = [
        {"ID": "1-HE", "Nama Produk": "Polygon Heist", "Brand": "Polygon", "Kategori": "Sepeda Hybrid", "Stok": 8, "Harga": 5000000},
        {"ID": "2-CL", "Nama Produk": "United Clovis", "Brand": "United", "Kategori": "Sepeda Gunung", "Stok": 8, "Harga": 7000000},
        {"ID": "3-HA", "Nama Produk": "Family Happy", "Brand": "Family", "Kategori": "Sepeda Anak", "Stok": 10, "Harga": 800000},
        {"ID": "4-TC", "Nama Produk": "Giant Tcr", "Brand": "Giant", "Kategori": "Roadbike", "Stok": 12, "Harga": 25000000},
        {"ID": "5-HI", "Nama Produk": "Helm Bolt Hijau", "Brand": "Polygon", "Kategori": "Helm Dewasa", "Stok": 4, "Harga": 240000},
        {"ID": "6-AE", "Nama Produk": "Helm Aero", "Brand": "Non Brand", "Kategori": "Helm Anak", "Stok": 6, "Harga": 100000},
        {"ID": "7-AL", "Nama Produk": "Bel Sepeda Alloy", "Brand": "Non Brand", "Kategori": "Bel Sepeda", "Stok": 5, "Harga": 25000},
        {"ID": "8-KO", "Nama Produk": "Bel Sepeda Kompas", "Brand": "Polygon", "Kategori": "Bel Sepeda", "Stok": 5, "Harga": 25000},
]
   
# LIST BARANG DIHAPUS
data_barang_dihapus = []

# LIST TRANSAKSI PENJUALAN
data_penjualan = []

# FUNGSI WARNA TEKS
def merah(teks):
    return f"\033[91m{teks}\033[0m"
def hijau(teks):
    return f"\033[92m{teks}\033[0m"
def biru(teks):
    return f"\033[94m{teks}\033[0m"
def kuning(teks):
    return f"\033[93m{teks}\033[0m"

# FUNGSI TAMPILAN TABEL
def tampilkan_tabel(data):
    print(tabulate(data, headers="keys", tablefmt="rst"))
    
# PESAN PILIHAN TIDAK VALID
def pesan_tidak_valid():
    print(merah("Pilihan tidak valid. Silakan coba lagi."))

# FUNGSI VALIDASI YES / NO
def validasi_konfirmasi(prompt):
    valid_yes = ["yes", "y", "ye", "yess", "yesss", "yeses", "yese", "sey", "eys", "esy"]
    valid_no = ["no", "n", "none", "nope", "noes", "naw", "nah"]
    while True:
        pilihan = input(prompt).strip().lower()
        if pilihan in valid_yes:
            return True
        elif pilihan in valid_no:
            return False
        else:
            print(merah("Input tidak valid. Masukkan 'yes' atau 'no'."))
            
# FUNGSI VALIDASI INPUT PRODUK
def validasi_input_produk(prompt):
    while True:
        nama_produk = input(prompt).strip().lower()
        if not nama_produk: #cek input nama kosong tidak
            print(merah("Tidak boleh kosong. Silakan ketik ulang."))
            continue
        huruf = [char for char in nama_produk if char.isalpha()]
        if len(huruf) < 2:
            print(merah("Minimal memuat 2 huruf. Silakan ketik ulang."))
            continue
        # Cek apakah semua karakter sesuai dengan kriteria
        valid_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'_- ")
        if not all(char in valid_chars for char in nama_produk):
            print(merah("Input tidak sesuai. Silakan ketik ulang."))
            continue
        return nama_produk

# VALIDASI INPUT NUMERIK
def validasi_input_numerik(prompt): # Memastikan input adalah angka
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(merah("Input tidak valid. Silakan masukkan angka."))
            
# VALIDASI INPUT NAMA PEMBELI
def validasi_input_nama(prompt):
    while True:
        nama = input(prompt).strip()
        huruf = [char for char in nama if char.isalpha()]
        if len(huruf) < 3:
            print(merah("Nama harus mengandung minimal 3 huruf. Silakan ketik ulang."))
            continue # akan kembali ke awal dari while True
        
        valid_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '\".")
        if not all(char in valid_chars for char in nama):
            print(merah("Input tidak sesuai. Hanya huruf, spasi, petik satu, titik, dan petik dua yang diperbolehkan."))
            continue
        return nama

# FUNGSI Generate ID Barang | Ketentuan ID: ID awal (angka terbesar dari data_stok dan data_barang_dihapus) + 1
def generate_id_barang(nama_produk):
    all_ids = [int(item['ID'].split('-')[0]) for item in data_stok + data_barang_dihapus] #revisi penjelasan
    kode_awal = f"{max(all_ids, default=0) + 1}"
    kata_terakhir = nama_produk.split()[-1]  # Mengambil kata terakhir dari nama barang
    kode_produk = kata_terakhir[:2].upper()  # Mengambil 2 huruf dari kata terakhir
    return kode_awal + "-" + kode_produk  

# VALIDASI INPUT SAAT EDIT | Digunakan pada saat edit nama produk, brand, kategori
def validasi_input_edit(prompt, nilai_sekarang):
    while True:
        input_edit = input(prompt).strip()
        if len(input_edit) > 0:
            return input_edit.title()
        elif input_edit == "":  # Jika pengguna menekan enter atau hanya memasukkan spasi
            return nilai_sekarang # Mengembalikan nilai sebelumnya
        else:
            print(merah("Input tidak boleh kosong. Silakan ketik ulang."))

# VALIDASI ANGKA EDIT | Digunakan pada saat edit stok & harga
def validasi_angka_edit(prompt, nilai_saat_ini):
    while True:
        input_angka = input(prompt).strip()
        if len(input_angka) == 0:  # Jika pengguna menekan enter atau memasukkan spasi
            return nilai_saat_ini
        try:
            input_angka = int(input_angka)
            if input_angka > 0:
                return input_angka
            else:
                print("Input harus lebih dari nol. Silakan ketik ulang.")
        except ValueError:
            print("Input harus berupa angka. Silakan ketik ulang.")
# VALIDASI CARI BARANG - Saat Mencari Bisa berupa apaun kecuali spasi
def validasi_input_cari(prompt):
    while True:
        input_user = input(prompt).strip()  # Menghapus kelebihan spasi
        if input_user:  # Memastikan tidak kosong
            return input_user.lower()
        else:
            print(merah("Masukkan teks kembali untuk mencari."))

# VALIDASI INPUT ID BARANG
def validasi_id_barang(prompt):
    while True:
        input_id = input(prompt).strip()  # Menghapus kelebihan spasi
        # Jika input tidak kosong akan dibuat upper
        if input_id:
            return input_id.upper()  # input ID barang akan di-upper
        else:
            print(merah("Input tidak boleh kosong. Silakan coba lagi."))
       
# FUNGSI PENCARIAN BARANG - DIGUNAKAN PADA SUBMENU CARI BARANG
def cari_barang():# PENCARIAN BARANG
    keyword = validasi_input_cari("Masukkan nama/brand/kategori barang yang dicari: ")
    hasil_pencarian = [item for item in data_stok if keyword in item['Nama Produk'].lower() or keyword in item['Brand'].lower() or keyword in item['Kategori'].lower()]

    if hasil_pencarian:
        print(hijau(f"Hasil pencarian kata '{keyword}' :"))
        tampilkan_tabel(hasil_pencarian)
    else:
        print(merah(f"Tidak ditemukan '{keyword}' dalam data stok."))
        
# FUNGSI EKSPOR TABEL DATA KE CSV
def ekspor_csv(nama_file, data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    df = pd.DataFrame(data)
    df.to_csv(f"{nama_file}_{timestamp}.csv", index=False)
    print(hijau(f"Data berhasil diekspor ke {nama_file}_{timestamp}.csv."))
    
# FUNGSI UMUM EKSPOR DATA
def ekspor_data_umum(data, nama_data):
    if not data:
        print(merah(f"Peringatan: Data {nama_data} kosong, tidak ada yang diekspor."))
        print(kuning("Kembali ke menu utama."))
        return
    tampilkan_tabel(data)
    while True:
        print(f"1. Lanjut ekspor data {nama_data} sebagai .csv")
        print("0. Kembali ke menu utama")
        pilihan = validasi_input_numerik("Pilih opsi :")
        if pilihan == 1:
            ekspor_csv(nama_data, data)
        elif pilihan == 0:
            print(kuning("Kembali ke menu utama."))
            break
        else:
            pesan_tidak_valid()

# SUBMENU TAMPILKAN STOK
def submenu_stok():
    while True:
        print("\nSubmenu Stok Barang:")
        print("1. Urutkan berdasarkan nama barang (a-z)")
        print("2. Urutkan berdasarkan stok barang (banyak - sedikit)")
        print("3. Urutkan berdasarkan harga barang (tinggi – rendah)")
        print("4. Reset tampilan ke default")
        print("5. Cari barang berdasarkan nama/brand/kategori")
        print("0. Kembali ke menu utama")

        pilihan = validasi_input_numerik("Pilih opsi: ")

        if pilihan == 1:
            print(hijau("Tabel berdasarkan nama barang (a-z):"))
            sorted_data = sorted(data_stok, key=lambda x: x['Nama Produk']) # Mengurutkan data berdasarkan kolom Nama Produk
            tampilkan_tabel(sorted_data)
        elif pilihan == 2:
            print(hijau("Tabel berdasarkan stok barang (banyak - sedikit):"))
            sorted_data = sorted(data_stok, key=lambda x: x['Stok'], reverse=True)
            tampilkan_tabel(sorted_data)
        elif pilihan == 3:
            print(hijau("Tabel berdasarkan harga barang (tinggi - rendah):"))
            sorted_data = sorted(data_stok, key=lambda x: x['Harga'], reverse=True)
            tampilkan_tabel(sorted_data)
        elif pilihan == 4:
            print(hijau("Tabel data stok:"))
            tampilkan_tabel(data_stok)
        elif pilihan == 5:
            print("Submenu pencarian barang")
            cari_barang()
        elif pilihan == 0:
            print(kuning("Kembali ke menu utama"))
            break  # Kembali ke menu utama
        else:
            pesan_tidak_valid()

# CEK DUPLIKAT BARANG
def cek_duplikat_barang(nama_produk, brand, kategori, id_barang=None):
    for item in data_stok:
        # Jika ID disediakan (saat edit), pastikan untuk mengabaikan item dengan ID yang sama
        if item["Nama Produk"] == nama_produk and item["Brand"] == brand and item["Kategori"] == kategori:
            if id_barang is None or item["ID"] != id_barang: 
                return True
    return False

# MENU 1 : TAMPILKAN STOK BARANG
def tampilkan_stok_barang():
    if not data_stok:
        print(merah("Stok Barang Kosong."))
        pilihan = validasi_konfirmasi("Ingin menambahkan data stok? (Yes/No): ")
        if pilihan == True:
            tambah_barang()
        else:
            print(kuning("Kembali ke menu utama."))
    else:
        print("Tabel Stok Barang :")
        tampilkan_tabel(data_stok)
        submenu_stok()  # artinya submenu_stok() akan dijalankan apapun yang ada di submenu_stok()

# MENU 2 : TAMBAH BARANG
def tambah_barang():
    while True:
        print("\nSubmenu Tambah Barang:")
        print("1. Tambah Barang Baru")
        print("0. Kembali ke menu utama")

        pilihan = validasi_input_numerik("Pilih opsi: ")

        if pilihan == 1:
            print(kuning("Tambah Barang Baru"))
            nama_produk = validasi_input_produk("Masukkan Nama Produk: ").title()
            brand = validasi_input_produk("Masukkan Brand: ").title()
            kategori = validasi_input_produk("Masukkan Kategori: ").title()

            if cek_duplikat_barang(nama_produk, brand, kategori):
                print(merah("Barang sudah ada. Silakan masukkan barang baru"))
                continue

            stok = validasi_input_numerik("Masukkan Stok: ")
            harga = validasi_input_numerik("Masukkan Harga Satuan: ")

            konfirmasi = validasi_konfirmasi("Simpan barang baru? (Yes/No): ")
            if konfirmasi:
                id_barang = generate_id_barang(nama_produk)
                data_stok.append({
                    "ID": id_barang,
                    "Nama Produk": nama_produk,
                    "Brand": brand,
                    "Kategori": kategori,
                    "Stok": stok,
                    "Harga": harga
                })
                print(hijau("Barang berhasil ditambahkan."))
                tampilkan_tabel(data_stok)
                return True  # Berhasil ditambahkan
            else:
                print(merah("Penambahan barang dibatalkan."))
                continue

        elif pilihan == 0:
            print(kuning("Kembali ke menu utama"))
            return False  # Indicate cancellation
        else:
            pesan_tidak_valid()

# MENU 3 : EDIT BARANG
def edit_barang():
    if not data_stok:
        print(merah("Saat ini data stok kosong."))
        print("1. Tambahkan Data Stok")
        print("2. Kembali ke Menu Utama")

        pilihan = validasi_input_numerik("Pilih opsi: ")

        if pilihan == 1:
            berhasil = tambah_barang()
            if berhasil:
                return  # Kembali ke menu utama jika penambahan barang berhasil
        elif pilihan == 2:
            return
        else:
            pesan_tidak_valid()
            return

    print("Tabel Stok Barang:")
    tampilkan_tabel(data_stok)

    while True:
        id_barang = validasi_id_barang(kuning("Masukkan ID Barang yang ingin diedit:"))
        item = None

        # Cari item berdasarkan ID
        for i in data_stok:
            if i['ID'].upper() == id_barang.upper():
                item = i
                break #akan kembali ke awal looping
        # Jika item ditemukan
        if item:
            print("Masukkan perubahan data :")
            print(kuning("Catatan : tekan enter jika tidak ingin mengubah data."))
            nama_produk_baru = validasi_input_edit(f"Nama Produk (sekarang: {item['Nama Produk']}): ", item['Nama Produk'])
            brand_baru = validasi_input_edit(f"Brand (sekarang: {item['Brand']}): ", item['Brand'])
            kategori_baru = validasi_input_edit(f"Kategori (sekarang: {item['Kategori']}): ", item['Kategori'])
            stok_baru = validasi_angka_edit(f"Stok (sekarang: {item['Stok']}): ", item['Stok'])
            harga_baru = validasi_angka_edit(f"Harga (sekarang: {item['Harga']}): ", item['Harga'])

            # Cek jika ada perubahan
            if (nama_produk_baru == item['Nama Produk'] and
                brand_baru == item['Brand'] and
                kategori_baru == item['Kategori'] and
                stok_baru == item['Stok'] and
                harga_baru == item['Harga']):
                print(merah("Tidak ada perubahan. Edit dibatalkan."))
                return

            # Menentukan nilai final dari input
            nama_produk_final = nama_produk_baru or item['Nama Produk']
            brand_final = brand_baru or item['Brand']
            kategori_final = kategori_baru or item['Kategori']
            stok_final = stok_baru or item['Stok']
            harga_final = harga_baru or item['Harga']

            # Cek duplikat jika Nama Produk, Brand, dan Kategori sama dengan barang lain di data stok
            if cek_duplikat_barang(nama_produk_final, brand_final, kategori_final):
                print(merah("Barang sudah disimpan di ID lain. Edit dibatalkan"))
                return

            # Update item jika ada perubahan
            item['Nama Produk'] = nama_produk_final
            item['Brand'] = brand_final
            item['Kategori'] = kategori_final
            item['Stok'] = stok_final
            item['Harga'] = harga_final

            print(hijau("Barang berhasil diedit."))
            tampilkan_tabel(data_stok)
            return

        print(merah("ID Barang tidak ditemukan."))
        
        # Validasi pilihan untuk memasukkan ulang ID atau membatalkan edit
        while True:
            print("1. Masukkan Ulang ID Barang")
            print("0. Batalkan Edit Barang")
            pilihan = validasi_input_numerik("Pilih opsi: ")
            if pilihan == 1:
                break  # kembali ke awal loop
            elif pilihan == 0:
                print(merah("Edit barang dibatalkan. Kembali ke menu utama."))
                return
            else:
                print(merah("Pilihan tidak valid. Silakan masukkan 1 atau 0."))

# MENU 4 : HAPUS BARANG
def hapus_barang():
    if not data_stok:
        print(merah("Stok Barang Kosong."))
        validasi_konfirmasi("Ingin menambahkan data stok? (Yes/No)")
        if pilihan == True:
            tambah_barang()
        else:
            print(kuning("Kembali ke menu utama."))
    while True:
        print("Menu Hapus Barang dipilih")
        print("\nTabel stok barang saat ini:")
        tampilkan_tabel(data_stok)
        id_barang = input("Masukkan ID Barang yang ingin dihapus: ")
        
        # Mencari ID Barang dalam data_stok
        item = next((item for item in data_stok if item['ID'] == id_barang.upper()), None)

        if item:
            tabel_data = [
            ["ID", "Nama Produk", "Brand", "Kategori", "Stok", "Harga"],
            [item['ID'], item['Nama Produk'], item['Brand'], item['Kategori'], item['Stok'], item['Harga']]
        ]
        # Menampilkan tabel
            print(tabulate(tabel_data, headers="firstrow", tablefmt="rst"))
            data_stok.remove(item)
            data_barang_dihapus.append(item)
            print(merah("Peringatan : Data ini akan dihapus!"))
            # Konfirmasi untuk menyimpan data
            simpan = validasi_konfirmasi("Konfirmasi hapus data. (Yes/No): ")
            if simpan == True:
                print(hijau(f"ID {id_barang} berhasil dihapus. \nData stok berhasil diperbarui."))
            elif simpan == False:
                data_stok.append(item)
                data_barang_dihapus.remove(item)
                print(merah("Penghapusan dibatalkan."))
                print(hijau("Barang dikembalikan ke data stok."))
            else:
                print(merah("Pilihan tidak valid. Penghapusan dibatalkan."))
            return  # Kembali setelah menghapus atau membatalkan

        print(merah("ID Barang tidak ditemukan."))
        
        while True:
            print("1. Masukkan Ulang ID Barang")
            print("0. Batalkan Penghapusan")
            pilihan = validasi_input_numerik("Pilih opsi: ")
            if pilihan == 1:
                break  # Kembali ke awal loop untuk memasukkan ID lagi
            elif pilihan == 0:
                print(merah("Penghapusan dibatalkan. Kembali ke menu sebelumnya."))
                return
            else:
                pesan_tidak_valid()
            
# MENU 5 : LIHAT BARANG DIHAPUS
def lihat_barang_dihapus():
    while True:
        if not data_barang_dihapus:
            print(merah("Tidak ada data barang dihapus"))
            break
        else:
            print("\nMenu Lihat Barang Dihapus:")
            print("1. Lihat data barang dihapus")
            print("0. Kembali ke menu utama")
            
            pilihan = validasi_input_numerik("Pilih opsi: ")
            if pilihan == 1:
                print("Tabel Barang Dihapus")
                tampilkan_tabel(data_barang_dihapus)
                
                # Submenu untuk menghapus data atau mengembalikan ke stok
                print("\nSubmenu:")
                print("1. Hapus seluruh data")
                print("2. Kembalikan barang ke stok")
                print("3. Kembalikan seluruh data ke stok")
                print("0. Kembali ke menu utama")
                pilihan_hapus = validasi_input_numerik("Pilih opsi: ")

                if pilihan_hapus == 1:
                    konfirmasi = validasi_konfirmasi("Yakin hapus seluruh data? (Yes/No): ")
                    if konfirmasi == True:
                        data_barang_dihapus.clear()  # Hapus semua data
                        print(hijau("Seluruh data berhasil dihapus."))
                        break  # Kembali ke menu utama setelah menghapus
                    elif konfirmasi == False:
                        print(merah("Penghapusan dibatalkan."))
                    else:
                        pesan_tidak_valid()
                
                elif pilihan_hapus == 2:
                    id_barang = validasi_id_barang("Masukkan ID barang yang ingin dikembalikan ke stok: ")
                    barang_dikembalikan = None
                    for barang in data_barang_dihapus:
                        if barang['ID'] == id_barang.upper():
                            barang_dikembalikan = barang
                            break
                    # Cek apakah ID ditemukan    
                    if barang_dikembalikan:
                        konfirmasi = validasi_konfirmasi("Konfirmasi pengembalian barang ke data stok: (Yes/No): ")
                        if konfirmasi == True:
                            data_stok.append(barang_dikembalikan)  # Kembalikan barang ke stok
                            data_barang_dihapus.remove(barang_dikembalikan)  # Hapus dari daftar barang dihapus
                            print(hijau("Barang berhasil dikembalikan ke stok."))
                        elif konfirmasi == False:
                            print(merah("Pengembalian dibatalkan."))
                        else:
                            pesan_tidak_valid()
                    else:
                        print(merah("ID barang tidak ditemukan."))

                elif pilihan_hapus == 3:
                    konfirmasi = validasi_konfirmasi("Konfirmasi pengembalian seluruh data ke stok: (Yes/No): ")
                    if konfirmasi == True:
                        data_stok.extend(data_barang_dihapus)  # Kembalikan seluruh barang ke stok
                        data_barang_dihapus.clear()  # Hapus semua data dari daftar barang dihapus
                        print(hijau("Seluruh barang berhasil dikembalikan ke stok."))
                    elif konfirmasi == False:
                        print(merah("Pengembalian dibatalkan."))
                    else:
                        pesan_tidak_valid()
                
                elif pilihan_hapus == '0':
                    break  # Kembali ke menu utama
                else:
                    pesan_tidak_valid()
            
            elif pilihan == 0:
                print(kuning("Kembali ke menu utama."))
                break  # Kembali ke menu utama
            else:
                pesan_tidak_valid()

# MENU 6 : TAMBAH TRANSAKSI PENJUALAN
def tambah_transaksi_penjualan():
    print("\nTambah Data Penjualan:")  # Ditampilkan untuk memberi informasi stok tersedia
    print("Stok tersedia :")
    tampilkan_tabel(data_stok)
    nama_pembeli = validasi_input_nama("Masukkan Nama Pembeli: ")

    while True:  # Loop untuk meminta input ID produk hingga ID yang valid atau membatalkan
        id_produk = validasi_id_barang("Masukkan ID Produk: ")  # supaya tidak case sensitive
        valid_id = False  # Menandakan apakah ID produk valid

        for item in data_stok:
            if item['ID'] == id_produk:
                print(f"Produk yang Anda pilih :", item["Nama Produk"])
                valid_id = True  # ID produk valid
                
                while True:  # Loop untuk meminta input quantity
                    print(f"Stok tersedia :", item["Stok"])
                    quantity = validasi_input_numerik("Masukkan quantity pembelian: ")
                    
                    # Menggunakan ketersediaan stok
                    if quantity > item['Stok']:
                        print(merah("Stok tidak tersedia. Silakan pilih opsi."))
                        print("1. Ubah Quantity")
                        print("2. Batalkan Transaksi")

                        pilihan = validasi_input_numerik("Pilih opsi: ")

                        if pilihan == 1:
                            continue  # Kembali ke awal loop untuk mengubah quantity
                        elif pilihan == 2:
                            print(merah("Penambahan Transaksi Dibatalkan"))
                            return  # Keluar dari fungsi
                        else:
                            pesan_tidak_valid()
                    else:
                        total = item['Harga'] * quantity

                        # Mengambil 2 huruf pertama dari nama pembeli
                        kode_pembeli = nama_pembeli[:2].upper()
                        
                        # Konfirmasi simpan transaksi
                        konfirmasi = validasi_konfirmasi("Simpan transaksi penjualan? Yes/No: ")
                        
                        if konfirmasi:
                            data_penjualan.append({
                                "ID Transaksi": f"{len(data_penjualan) + 1}{kode_pembeli}",  # Membuat ID Transaksi secara otomatis
                                "Nama Pembeli": nama_pembeli,
                                "ID Produk": item['ID'],
                                "Nama Produk": item['Nama Produk'],
                                "Brand": item['Brand'],
                                "Kategori": item['Kategori'],
                                "Quantity": quantity,
                                "Harga": item['Harga'],
                                "Total": total
                            })

                            item['Stok'] -= quantity  # Mengurangi stok
                            print(hijau("Transaksi berhasil ditambahkan."))
                            tampilkan_tabel(data_penjualan)
                        else:
                            print(merah("Transaksi dibatalkan."))
                        
                        return
        # Jika ID produk tidak ditemukan
        print(merah("ID Produk tidak ditemukan."))
        print("Opsi :")
        print("1. Masukkan ID Barang lagi")
        print("2. Batalkan transaksi")

        pilihan = validasi_input_numerik("Pilih opsi: ")
        if pilihan == 1:
            continue  # Kembali ke awal loop untuk mencari ID lagi
        elif pilihan == 2:
            print("Input transaksi dibatalkan.")
            break  # Keluar dari fungsi
        else:
            pesan_tidak_valid()

# MENU 7 : LIHAT TRANSAKSI PENJUALAN
def lihat_transaksi_penjualan():
    while True: 
        if not data_penjualan:
            print(merah("Belum ada transaksi penjualan!\n"))
            print("1. Tambah Transaksi Penjualan")
            print("0. Kembali ke Menu Utama")
            pilihan = validasi_input_numerik("Pilih Opsi :")

            if pilihan == 1:
                tambah_transaksi_penjualan()
            elif pilihan == 0:
                print(kuning("Kembali ke menu utama."))
                break
            else:
                print(merah("Pilihan tidak valid. Kembali ke menu utama."))
        else:
            print("Transaksi Penjualan :")
            tampilkan_tabel(data_penjualan)
            break
    
# MENU 8 : EKSPOR DATA STOK
def ekspor_data_stok():
    ekspor_data_umum(data_stok, "stok")

# MENU 9 : EKSPOR DATA PENJUALAN
def ekspor_data_penjualan():
    ekspor_data_umum(data_penjualan, "penjualan")

# MENU UTAMA
def menu_utama():
    print(biru("\nMENU ADMIN TOKO SEPEDA CIHUY"))
    while True:
        print(biru("\nDAFTAR MENU UTAMA:"))
        print("1. Tampilkan Stok Barang")
        print("2. Tambah Barang")
        print("3. Edit Barang")
        print("4. Hapus Barang")
        print("5. Lihat Barang Dihapus")
        print("6. Tambah Transaksi Penjualan")
        print("7. Lihat Transaksi Penjualan")
        print("8. Ekspor Data Stok")
        print("9. Ekspor Data Penjualan")
        print("0. Keluar")

        pilihan = validasi_input_numerik("Pilih menu: ")

        if pilihan == 1:
            tampilkan_stok_barang()
        elif pilihan == 2:
            tambah_barang()
        elif pilihan == 3:
            edit_barang()
        elif pilihan == 4:
            hapus_barang()
        elif pilihan == 5:
            lihat_barang_dihapus()
        elif pilihan == 6:
            tambah_transaksi_penjualan()
        elif pilihan == 7:
            lihat_transaksi_penjualan()
        elif pilihan == 8:
            ekspor_data_stok()
        elif pilihan == 9:
            ekspor_data_penjualan()
        elif pilihan == 0:
            print(merah("Program diakhiri."))
            print(hijau("Selamat beraktivitas kembali!"))
            break  # Keluar dari program
        else:
            pesan_tidak_valid()
                   
# MENJALANKAN PROGRAM
if __name__ == "__main__":
    menu_utama()
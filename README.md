# APLIKASI ADMIN TOKO SEPEDA CIHUY

Program ini menerapkan 4 fungsi utama CRUD :

    1. Create
    2. Read
    3. Update
    4. Delete

Program dibuat untuk admin toko.

Admin Toko Sepeda Cihuy memiliki akses penuh terhadap seluruh menu utama pada aplikasi ini.

## Penjelasan Data

### 1. Data Stok

Data ini berisi stok produk yang tersedia :
| No | Nama Kolom  | Type | Deskripsi                 | Keterangan                         |
|----|-------------|------|---------------------------|------------------------------------|
| 1  | ID          | str  | ID unik barang            | Unik setiap barang. Generate otomatis                 |
| 2  | Nama Produk | str  | Nama Produk               | Bisa sama di kolom yang sama       |
| 3  | Brand       | str  | Nama Brand                | Bisa sama di kolom yang sama       |
| 4  | Kategori    | str  | Kategori Produk           | Bisa sama di kolom yang sama       |
| 5  | Stok        | int  | Jumlah stok yang tersedia | Bisa 0, stok tidak terbatas        |
| 6  | Harga       | int  | Harga satuan barang       | Tidak bisa 0, harga tidak terbatas |

Catatan : Nama Produk, Brand, dan Kategori tidak bisa sama ketiganya.

### 2. Data Penjualan
Data ini berisi detail produk yang sudah terjual
| No | Nama Kolom   | Type | Deskripsi                                                                            | Keterangan                                                                                                                       |
|----|--------------|------|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| 1  | ID Transaksi | str  | ID unik untuk transaksi penjualan                                                    | Unik setiap transaksi. Kombinasi dari angka sebagai urutan,  huruf dari cuplikan Nama Pembeli.                                   |
| 2  | Nama Pembeli | str  | Nama Pembeli untuk mendapatkan ID Transaksi                                          | - Bisa sama dengan nama pembeli lain - Tidak bisa berisi karakter kosong - Minimal terdiri dari 2 huruf - Bisa lebih dari 1 kata |
| 3  | ID Produk    | str  | ID Produk yang didapat dari Data Stok                                                | Bisa sama dengan transaksi lain                                                                                                  |
| 4  | Nama Produk  | str  | Nama Produk yang didapat dari Data Stok                                              | Bisa sama dengan transaksi lain                                                                                                  |
| 5  | Brand        | str  | Brand diambil dari Data Stok                                                         | Bisa sama dengan transaksi lain                                                                                                  |
| 6  | Quantity     | int  | Jumlah barang yang dibeli. Akan mengurangi Stok di Data Stok                         | Tidak bisa nol                                                                                                                   |
| 7  | Harga        | int  | Harga satuan barang didapat dari Data Stok                                           | Tidak bisa nol                                                                                                                   |
| 8  | Total        | int  | Total harga yang didapat dari perkalian  <br> Quantity dan Harga pada Transaksi Penjualan | Dibuat otomatis                                                                                                                  |

## Menu Utama
Saat dijalankan, program akan menampilkan 9 menu utama dan 1 opsi untuk keluar program.

### 1. Tampilkan Stok Barang
Jika stok barang kosong submenu tidak ditampilkan.
Saat stok barang terisi, submenu akan tampil.

#### Submenu Stok Barang :
    1. Urutkan berdasarkan nama barang (a-z)
    2. Urutkan berdasarkan stok barang (banyak-sedikit)
    3. Urutkan berdasarkan harga barang (mahal-murah)
    4. Reset tampilan
    5. Cari barang berdasarkan nama

### 2. Tambah Barang
Di menu ini user bisa menambahkan barang yang akan masuk ke data stok.
#### Submenu Tambah Barang :
    1. Tambah barang baru
    2. Kembali ke menu utama

### 3. Edit Barang
Jika stok barang kosong, tidak ada yang ditampilkan.
Saat stok barang terisi, tabel stok barang ditampilkan dan muncul perintah untuk memasukkan ID barang yang ingin diedit.

### 4. Hapus Barang
Jika stok barang kosong, tidak ada yang ditampilkan.
Saat stok barang terisi, tabel stok barang ditampilkan dan muncul perintah untuk memasukkan ID barang yang akan dihapus.

### 5. Lihat Barang Dihapus
#### Submenu Lihat Barang Dihapus :
    1. Lihat data barang dihapus
    0. Kembali ke menu utama

### 6. Tambah Transaksi Penjualan
Digunakan untuk menambah data transaksi penjualan.
User diminata untuk memasukkan Nama Produk, Brand, Kategori, dan Quantity pembelian.

### 7. Lihat Transaksi Penjualan
Jika transaksi belum ada, tidak ada data yang ditampilkan.
Saat ada transaksi, akan tampil tabel dari data transaksi penjualan.

### 8. Ekspor Data Stok
Jika stok barang kosong, submenu tidak ditampilkan.
Saat data stok ada, akan muncul tabel data stok dan submenu.
#### Submenu Data Stok :
    1. Lanjut ekspor data stok
    0. Kembali ke menu utama

Data yang berhasil diekspor akan disimpan dalam format .csv dan memiliki timestamp sebagai nama filenya.

### 9. Ekspor Data Penjualan
Jika data transaksi penjualan kosong, submenu tidak ditampilkan.
Saat data transaksi penjualan ada, akan muncul tabel data transaksi penjualan dan submenu.
#### Submenu Data Stok :
    1. Lanjut ekspor data penjualan
    0. Kembali ke menu utama

Data yang berhasil diekspor akan disimpan dalam format .csv dan memiliki timestamp sebagai nama filenya.
### 0. Keluar
Akan mengakhiri program.

## 🚀 About Me
Kaffatufiddin, siswa program Bootcamp Data Science Purwadhika on Campus Jogja 2024.


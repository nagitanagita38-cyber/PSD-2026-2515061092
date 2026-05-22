# Implementasi Binary Search Tree (BST) untuk Operasi Penyimpanan, Penghapusan, dan Pencarian Rute Terpendek dan Tercepat
## Deskripsi Singkat
Program ini merupakan struktur data Binary Search Tree (BST) Lanjutan uuntuk operasi penyimpanan, penghapusan, dan pencarian rute terpendek dan tercepat berdasarkan urutan abjad. Setiap rute yang disimpan dalam noda berdasarkan nilai kunci(key), sehingga data terurut secara otomatis. Struktur ini membuat proses pengolahan data menjadi lebih efisien karena setiap data akan otomatis tersusun berdasarkan urutan abjad tanpa perlu pengurutan manual. Setiap penambahan atau penghapusan rute langsung disesuaikan dengan aturan Binary Search Tree, sehingga data selalu berada pada posisi yang tepat sesuai perbandingan nilai kunci. Selain itu, program ini juga menyediakan fitur untuk menampilkan seluruh data rute menggunakan metode level-order traversal serta menentukan rute dengan urutan alfabet terkecil dan terbesar.
## Source Code
<img width="665" height="2503" alt="source code bst" src="https://github.com/user-attachments/assets/17afed0b-3ecd-4ae0-a0ee-191d0053af6a" />

Baris 1 membuat class Node yang digunakan sebagai tempat penyimpanan data pada Binary Search Tree (BST). 

Baris 2 mendefinisikan constructor def__init__(self, key): yang otomatis dijalankan saat objek node dibuat. 

Baris 3 self.key = key untuk menyimpan nilai atau data node ke dalam variabel key. 

Baris 4 self.left = None untuk menginisialisasi anak kiri (left) dengan nilai None, artinya belum memiliki anak kiri. 

Baris 5 self.right = None untuk menginisialisasi anak kanan (right) dengan nilai None, artinya belum memiliki anak kanan.

Baris 7 membuat class BSTLanjut sebagai class utama BST. 

Baris 8 def __init__(self): untuk mendefinisikan constructor pada class BST. 

Baris 9 self.root = None untuk menginisialisasi root BST dengan nilai None yang berarti tree masih kosong.

Baris 11 membuat fungsi def insert_node(self, root, key): untuk menambahkan node secara rekursif ke dalam BST. 

Baris 12 if root is None: untuk memeriksa apakah posisi node saat ini kosong. 

Baris 13 return Node(key) untuk membuat node baru jika posisi kosong ditemukan. 

Baris 14 if key < root.key: untuk memeriksa apakah nilai key lebih kecil dari root. 

Baris 15  root.left = self.insert_node(root.left, key) untuk memasukkan data ke subtree kiri secara rekursif. 

Baris 16 elif key > root.key: untuk memeriksa apakah nilai key lebih besar dari root. 

Baris 17 root.right = self.insert_node(root.right, key) untuk memasukkan data ke subtree kanan secara rekursif. 

Baris 18 return root untuk mengembalikan root setelah proses insert selesai.

Baris 20 membuat fungsi def insert(self, key): sebagai fungsi utama untuk menambah data. 

Baris 21 self.root = self.insert_node(self.root, key) untuk memanggil fungsi insert_node() dimulai dari root BST.

Baris 23 membuat fungsi def find_min_node(self, root): untuk mencari node dengan nilai terkecil. 

Baris 24 current = root untuk menyimpan root sementara ke variabel current. 

Baris 25 while current is not None and current.left is not None: untuk melakukan perulangan selama node masih memiliki anak kiri. 

Baris 26 current = current.left untuk menggeser posisi current ke anak kiri. 

Baris 27 return current untuk mengembalikan node paling kiri sebagai nilai terkecil.

Baris 29 membuat fungsi def delete_node(self, root, key): untuk menghapus node secara rekursif. 

Baris 30 if root is None: untuk memeriksa apakah root kosong. 

Baris 31 return None untuk mengembalikan None. 

Baris 32 if key < root.key: untuk memeriksa apakah key lebih kecil dari root. 

Baris 33 root.left = self.delete_node(root.left, key) untuk mencari node yang akan dihapus di subtree kiri. 

Baris 34 elif key > root.key: untuk memeriksa apakah key lebih besar dari root. 

Baris 35 root.right = self.delete_node(root.right, key) untuk mencari node yang akan dihapus di subtree kanan. 

Baris 36 else: dijalankan jika node ditemukan. 

Baris 37 if root.left is None and root.right is None: untuk memeriksa apakah node tidak memiliki anak. 

Baris 38 return None untuk menghapus node dengan mengembalikan None. 

Baris 39 elif root.left is None: untuk memeriksa apakah node hanya memiliki anak kanan. 

Baris 40 return root.right untuk mengganti node dengan anak kanan. 

Baris 41 elif root.right is None: untuk memeriksa apakah node hanya memiliki anak kiri. 

Baris 42 return root.left untuk mengganti node dengan anak kiri. 

Baris 43 else: dijalankan jika node memiliki dua anak. 

Baris 44 successor = self.find_min_node(root.right) untuk mencari successor yaitu node terkecil pada subtree kanan. 

Baris 45 root.key = successor.key untuk mengganti nilai node dengan nilai successor. 

Baris 46 root.right = self.delete_node(root.right, successor.key) untuk menghapus node successor yang lama. 

Baris 47 return root untuk mengembalikan root setelah proses delete selesai.

Baris 49 membuat fungsi def delete(self, key): sebagai fungsi utama penghapusan data. 

Baris 50 self.root = self.delete_node(self.root, key) untuk memanggil fungsi delete_node() mulai dari root BST.

Baris 52 membuat fungsi def level_order(self, root): untuk traversal level order atau Breadth First Search (BFS). 

Baris 53 if root is None: untuk memeriksa apakah tree kosong. 

Baris 54 print("(kosong)") menampilkan tulisan “(kosong)” jika BST kosong. 

Baris 55 return untuk menghentikan fungsi. 

Baris 56 queue = [] untuk membuat list kosong sebagai queue.

Baris 57 queue.append(root) untuk memasukkan root ke queue. 

Baris 58 while len(queue) > 0: untuk melakukan perulangan selama queue masih berisi node. 

Baris 59 current = queue.pop(0) untuk mengambil node paling depan dari queue. 

Baris 60 print("-", current.key) untuk menampilkan nilai node saat ini. 

Baris 61 if current.left is not None: untuk memeriksa apakah node memiliki anak kiri. 

Baris 62 queue.append(current.left) untuk memasukkan anak kiri ke queue. 

Baris 63 if current.right is not None: untuk memeriksa apakah node memiliki anak kanan. 

Baris 64 queue.append(current.right) untuk memasukkan anak kanan ke queue. 

Baris 65 print() menampilkan baris kosong setelah traversal selesai.

Baris 67 membuat fungsi def rute_terpendek(self): untuk mencari rute dengan nilai terkecil. 

Baris 68 if self.root is None: untuk memeriksa apakah BST kosong.

Baris 69 return None mengembalikan None jika kosong. 

Baris 70 return self.find_min_node(self.root).key untuk mengambil nilai terkecil menggunakan fungsi find_min_node().

Baris 72 membuat fungsi def rute_tercepat(self): untuk mencari rute dengan nilai terbesar. 

Baris 73 if self.root is None: untuk memeriksa apakah BST kosong. 

Baris 74 return None mengembalikan None jika kosong. 

Baris 76 current = self.root untuk menyimpan root ke variabel current. 

Baris 77 while current.right is not None: untuk melakukan perulangan selama masih ada anak kanan. 

Baris 78 current = current.right untuk menggeser current ke anak kanan. 

Baris 79 return current.key mengembalikan nilai node terbesar.

Baris 81 membuat fungsi utama def main():. 

Baris 82 bst = BSTLanjut() untuk membuat objek BST bernama bst. 

Baris 83 pilih = 0 untuk menginisialisasi variabel pilih dengan nilai 0. 

Baris 84 while pilih != 6: untuk membuat perulangan menu selama user belum memilih keluar.

Baris 85 print("\n=== MENU BST LANJUT (RUTE) ===") untuk menampilkan judul menu program. 

Baris 86 sampai 91 
       
        print("1. Simpan Rute")
        print("2. Hapus Rute")
        print("3. Tampilkan Susunan Rute")
        print("4. Rute Terpendek")
        print("5. Rute Tercepat")
        print("6. Keluar")
        
untuk menampilkan daftar pilihan menu BST.

Baris 93 menggunakan try untuk menangani error input. 

Baris 94 pilih = int(input("Pilih: ")) untuk meminta user memasukkan pilihan menu dalam bentuk angka. 

Baris 95 except ValueError: untuk menangkap error jika input bukan angka. 

Baris 96 print("Input tidak valid!") utnuk menampilkan pesan “Input tidak valid!”. 

Baris 97 continue untuk mengulang kembali ke menu awal.

Baris 99 if pilih == 1: dijalankan jika user memilih menu simpan rute. 

Baris 100 x = input("Masukkan rute yang dicari: ") meminta input nama rute. 

Baris 101 bst.insert(x) menambahkan rute ke BST. 

Baris 102 print(f"Rute '{x}' berhasil disimpan") untuk menampilkan pesan bahwa rute berhasil disimpan.

Baris 104 elif pilih == 2: dijalankan jika user memilih menu hapus rute. 

Baris 105 x = input("Hapus rute yang dicari: ") meminta input rute yang akan dihapus. 

Baris 106 bst.delete(x) untuk menghapus rute dari BST. 

Baris 107 print(f"Rute '{x}' berhasil dihapus") untuk menampilkan pesan bahwa rute berhasil dihapus.

Baris 109 elif pilih == 3: dijalankan jika user memilih menu tampilkan susunan rute. 

Baris 110 print("Susunan rute yang dicari: ") untuk menampilkan judul traversal. 

Baris 111 bst.level_order(bst.root) untuk menjalankan traversal level order untuk menampilkan isi BST.

Baris 113 elif pilih == 4: dijalankan jika user memilih menu rute terpendek. 

Baris 114 hasil = bst.rute_terpendek() untuk menyimpan hasil rute terkecil ke variabel hasil. 

Baris 115 print("Rute terpendek yang dicari:", hasil) untuk menampilkan hasil rute terpendek.

Baris 117 elif pilih == 5: dijalankan jika user memilih menu rute tercepat. 

Baris 118 hasil = bst.rute_tercepat() untuk menyimpan hasil rute terbesar ke variabel hasil. 

Baris 119 print("Rute tercepat yang dicari:", hasil) untuk menampilkan hasil rute tercepat.

Baris 121 elif pilih == 6: dijalankan jika user memilih keluar dari program. 

Baris 122 print("Program selesai") untuk menampilkan pesan “Program selesai”.

Baris 124 else: dijalankan jika pilihan menu tidak tersedia. 

Baris 125 print("Pilihan tidak valid!") untuk menampilkan pesan “Pilihan tidak valid!” jika input salah.

Baris 127 if __name__ == "__main__": untuk memeriksa apakah file dijalankan langsung. 

Baris 128 main() menjalankan fungsi main() sebagai program utama.

## Output
<img width="671" height="2916" alt="output bst" src="https://github.com/user-attachments/assets/da0e9c9d-1d1f-4e7b-ac31-095128913054" />

Program tersebut merupakan simulasi Rute Perjalanan menggunakan struktur data Binary Search Tree (BST) Lanjut. Pada awalnya, pengguna memilih Menu 1 untuk memasukkan delapan rute secara bertahap yang dimulai dari 'Lampung' sebagai root (akar pohon), diikuti oleh Yogyakarta, Bandung, Surabaya, Malang, Medan, Pontianak, dan Halmahera, yang masing-masing posisinya diatur otomatis ke cabang kiri atau kanan berdasarkan urutan abjadnya. Ketika Menu 3 dipilih, program menampilkan susunan rute tersebut dari posisi atas ke bawah menggunakan metode penelusuran Level-Order (lapis demi lapis), sehingga memunculkan visualisasi hierarki kota yang terstruktur.

Selanjutnya, pengguna memilih Menu 2 dengan menghapus rute 'Medan', yang secara otomatis diikuti oleh penyesuaian struktur pohon agar sifat-sifat BST tetap terjaga, dibuktikan dengan hilangnya nama kota tersebut saat susunan rute ditampilkan kembali. Fitur pencarian nilai ekstrem ditunjukkan pada Menu 4 dan Menu 5; Menu 4 digunakan untuk mencari "Rute Terpendek" dengan menelusuri cabang paling kiri untuk menemukan kota dengan abjad paling awal (yaitu 'Bandung'), sedangkan Menu 5 mencari "Rute Tercepat" dengan menelusuri cabang paling kanan untuk menemukan kota dengan abjad paling akhir (yaitu 'Yogyakarta'). Proses simulasi ini diakhiri secara bersih melalui Menu 6 yang menghentikan seluruh jalannya sistem dengan memunculkan pesan konfirmasi bahwa program telah selesai.

## Link Youtube

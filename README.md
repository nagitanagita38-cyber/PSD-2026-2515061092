# Implementasi Hash Map Menggunakan Metode Separate Chaining untuk Pencarian Data Barang

## Deskripsi Singkat

Program ini digunakan untuk menyimpan dan mencari data barang berdasarkan kode barang menggunakan struktur data Hash Map. Setiap barang memiliki kode unik sebagai key dan nama barang sebagai value. Pengguna dapat memasukkan kode barang untuk mencari informasi barang yang tersimpan di dalam hash table. Algoritma yang diterapkan adalah Hashing dengan Separate Chaining. Teknik hashing digunakan untuk menentukan lokasi penyimpanan data pada tabel menggunakan fungsi hash. Jika terjadi collision (dua data memiliki indeks yang sama), maka data disimpan dalam bentuk linked list pada indeks tersebut. Metode ini memungkinkan pencarian data tetap berjalan dengan efisien meskipun terjadi collision.

## Source Code
<img width="404" height="846" alt="Screenshot 2026-06-08 185940" src="https://github.com/user-attachments/assets/43bd8f6c-006e-448f-8e30-31d7dee96e81" />

Baris 1 class Node: digunakan untuk mendefinisikan kelas Node yang berfungsi sebagai elemen pada linked list. 

Baris 2 def __init__(self, key, value): merupakan constructor yang akan dijalankan ketika objek Node dibuat. 

Baris 3 self.key = key digunakan untuk menyimpan kode barang sebagai key. 

Baris 4 self.value = value digunakan untuk menyimpan nama barang sebagai value. 

Baris 5 self.next = None digunakan untuk menyimpan referensi ke node berikutnya yang pada awalnya bernilai None.

Baris 7 class HashMapSeparateChaining: digunakan untuk mendefinisikan kelas Hash Map yang menerapkan metode Separate Chaining. 

Baris 8 def __init__(self, size=10): merupakan constructor kelas Hash Map. 

Baris 9 self.SIZE = size digunakan untuk menyimpan ukuran hash table. 

Baris 10 self.table = [None] * self.SIZE digunakan untuk membuat hash table dengan jumlah slot sesuai ukuran yang ditentukan.

Baris 12 def hash_function(self, key): digunakan untuk membuat fungsi hash. 

Baris 13 return (key % self.SIZE + self.SIZE) % self.SIZE digunakan untuk menghitung indeks penyimpanan data berdasarkan nilai key menggunakan operasi modulo.

Baris 15 def insert(self, key, value): digunakan untuk membuat fungsi penambahan data. 

Baris 16 index = self.hash_function(key) digunakan untuk menghitung indeks tempat data akan disimpan. 

Baris 17 current = self.table[index] digunakan untuk mengambil node pertama pada indeks tersebut. 

Baris 18 while current is not None: digunakan untuk menelusuri linked list jika terdapat data pada indeks tersebut. 

Baris 19 if current.key == key: digunakan untuk mengecek apakah key sudah ada. 

Baris 20 current.value = value digunakan untuk memperbarui value jika key ditemukan. 

Baris 21 return digunakan untuk menghentikan proses insert setelah update berhasil. 

Baris 22 current = current.next digunakan untuk berpindah ke node berikutnya. 

Baris 23 new_node = Node(key, value) digunakan untuk membuat node baru. 

Baris 24 new_node.next = self.table[index] digunakan untuk menghubungkan node baru ke node lama pada indeks tersebut. 

Baris 25 self.table[index] = new_node digunakan untuk menjadikan node baru sebagai head linked list.

Baris 27 def search(self, key): digunakan untuk membuat fungsi pencarian data. 

Baris 28 index = self.hash_function(key) digunakan untuk menghitung indeks pencarian. 

Baris 29 current = self.table[index] digunakan untuk mengambil node pertama pada indeks tersebut. 

Baris 30 while current is not None: digunakan untuk menelusuri linked list. 

Baris 31 if current.key == key: digunakan untuk memeriksa apakah key ditemukan. 

Baris 32 return current digunakan untuk mengembalikan node yang ditemukan. 

Baris 33 current = current.next digunakan untuk berpindah ke node berikutnya. 

Baris 34 return None digunakan untuk mengembalikan nilai None apabila data tidak ditemukan.

Baris 36 def display(self): digunakan untuk membuat fungsi menampilkan isi hash table. 

Baris 37 print("\nIsi Hash Table (Separate Chaining):") digunakan untuk menampilkan judul output. 

Baris 38 for i in range(self.SIZE): digunakan untuk melakukan perulangan pada seluruh indeks hash table. 

Baris 39 print(f"{i}: ", end="") digunakan untuk menampilkan nomor indeks. 

Baris 40 current = self.table[i] digunakan untuk mengambil node pertama pada indeks tersebut. 

Baris 41 while current is not None: digunakan untuk menelusuri linked list. 

Baris 42 print(f"({current.key},{current.value}) -> ", end="") digunakan untuk menampilkan data pada node. 

Baris 43 current = current.next digunakan untuk berpindah ke node berikutnya. 

Baris 44 print("NONE") digunakan untuk menandai akhir linked list pada indeks tersebut.

Baris 47 def main(): digunakan untuk membuat fungsi utama program. 

Baris 48 hashmap = HashMapSeparateChaining() digunakan untuk membuat objek Hash Map. 

Baris 49 sampai 55 hashmap.insert(...) digunakan untuk menambahkan data barang ke dalam hash table. 

Baris 56 hashmap.display() digunakan untuk menampilkan seluruh isi hash table.

Baris 58 while True: digunakan untuk membuat perulangan agar pengguna dapat melakukan pencarian berulang kali. 

Baris 59 kode_barang = int(input("cari kode barang :")) digunakan untuk menerima input kode barang dari pengguna. 

Baris 61 if kode_barang == 0: digunakan untuk mengecek apakah pengguna ingin mengakhiri program. 

Baris 62 print("Program selesai.") digunakan untuk menampilkan pesan program selesai. 

Baris 64 hasil = hashmap.search(kode_barang) digunakan untuk mencari data berdasarkan kode barang yang dimasukkan. 

Baris 66 if hasil is not None: digunakan untuk mengecek apakah data ditemukan. 

Baris 67 print(f"\nKode Barang : {hasil.key}") digunakan untuk menampilkan kode barang. Baris 68 print(f"\nNama Barang : {hasil.value}") digunakan untuk menampilkan nama barang.

Baris 69 else: digunakan jika data tidak ditemukan. 

Baris 70 print("\nBarang dengan kode {kode_barang} tidak ditemukan.") digunakan untuk menampilkan pesan bahwa barang tidak ditemukan.

Baris 72 if __name__ == "__main__": digunakan untuk memastikan program dijalankan langsung. 

Baris 73 main() digunakan untuk memanggil fungsi utama sehingga program dapat dieksekusi.

## Output
<img width="645" height="263" alt="Screenshot 2026-06-08 190102" src="https://github.com/user-attachments/assets/b16f9286-0ae8-4297-98c0-bdea552608f1" />

# Aplikasi Riwayat Edit Menggunakan Stack Array
## Deskripsi Singkat
Program ini adalah simulasi dari sistem riwayat pengeditan seperti fungsi undo dalam aplikasi yang digunakan untuk mengedit, seperti untuk foto, dokumen, atau video. Program ini dikembangkan dengan memanfaatkan struktur data _Stack_ yang berbasis array. Stack adalah sebuah struktur data yang beroperasi berdasarkan prinsip LIFO (Last In First Out), yang berarti elemen terakhir yang dimasukkan adalah elemen pertama yang akan dikeluarkan. Prinsip ini mirip dengan tumpukan piring, di mana piring yang paling terakhir diletakkan di atas akan menjadi piring yang pertama kali diambil.

Dalam aplikasi ini, setiap tindakan pengeditan yang dilakukan oleh pengguna akan disimpan dalam stack menggunakan metode push. Saat pengguna mengakses fungsi undo, maka pengeditan terakhir akan dihapus dengan menggunakan metode pop. Selain itu, aplikasi juga dilengkapi dengan fitur untuk melihat pengeditan terakhir dengan menggunakan peek, serta menampilkan seluruh riwayat pengeditan melalui tampilan display. Penggunaan struktur data stack sangat tepat untuk aplikasi undo karena proses penghapusan biasanya dilakukan pada data yang terakhir kali dimasukkan. Program ini juga mengimplementasikan konsep array sebagai sarana penyimpanan data sehingga pengelolaan riwayat pengeditan dapat dilakukan secara lebih teratur dan efisien.

## Source Code
<img width="402" height="893" alt="Source Code StackArray" src="https://github.com/user-attachments/assets/8779318e-67cf-4451-8145-1d9c48c8f360" />

Baris 1: class StackArray: - Membuat class bernama StackArray untuk merepresentasikan struktur data stack menggunakan array.

Baris 2: def_init_(self, max_size=100): - untuk inisialisasi object stack dengan ukuran maksimal default 100.

Baris 3: self.MAX = max_size - Menyimpan kapasitas maksimum stack ke variabel MAX.

Baris 4: self.st = [None] * self.MAX - Membuat array/list kosong berukuran MAX.

Baris 5: self.top_idx = -1 - Menandakan stack masih kosong karena belum ada data.

Baris 7: def is_empty(self): - Method untuk mengecek apakah stack kosong.

Baris 8: return self.top_idx == -1 - Mengembalikan nilai True jika stack kosong.

Baris 10: def is_full(self): - Method untuk mengecek apakah stack penuh.

Baris 11: return self.top_idx == self.MAX - 1 - Jika indeks paling atas sudah mencapai kapasitas maksimum, maka stack penuh.

Baris 13: def push(self, x): - Method untuk menambahkan data ke stack.

Baris 14: if self.is_full(): - Mengecek apakah stack penuh.

Baris 15: print("Riwayat penuh") - Menampilkan pesan jika stack penuh.

Baris 16: return - Menghentikan proses penambahan data.

Baris 17: self.top_idx += 1 - Menambah posisi indeks teratas stack.

Baris 18: self.st[self.top_idx] = x - Menyimpan data ke posisi teratas stack.

Baris 19: print(f"Edit {x} ditambahkan") - Menampilkan pesan bahwa data berhasil ditambahkan.

Baris 21: def pop(self): - untuk menghapus data paling atas stack.

Baris 22: if self.is_empty(): - Mengecek apakah stack kosong.

Baris 23: print("Tidak ada riwayat edit") - Menampilkan pesan jika stack kosong.

Baris 24: return - Menghentikan proses penghapusan.

Baris 25: print(f"Mengurungkan edit {self.st[self.top_idx]} berhasil") - Menampilkan data edit yang dihapus.

Baris 26: self.top_idx -= 1 - Mengurangi indeks teratas sehingga data dianggap terhapus.

Baris 28: def peek(self): - Method untuk melihat data paling atas tanpa menghapusnya.

Baris 29: if self.is_empty(): - Mengecek apakah stack kosong.

Baris 30: print("Tidak ada riwayat edit.") - Menampilkan pesan jika stack kosong.

Baris 31: return - Menghentikan proses.

Baris 32: print(f"Edit terakhir: {self.st[self.top_idx]}") - Menampilkan edit terakhir pada stack.

Baris 34: def display(self): - Method untuk menampilkan seluruh isi stack.

Baris 35: if self.is_empty(): - Mengecek apakah stack kosong.

Baris 36: print("Belum ada riwayat edit") - Menampilkan pesan jika belum ada data.

Baris 37: return - Menghentikan proses.

Baris 38: print("Tampilkan riwayat edit terbaru: ") - Menampilkan judul output riwayat edit.

Baris 39: for i in range(self.top_idx, -1, -1): - Perulangan dari data paling atas ke bawah.

Baris 40: print("-", self.st[i]) - Menampilkan isi stack satu per satu.

Baris 41: print() - Memberi jarak baris agar output lebih rapi.

Baris 43: def main(): - Function utama program.

Baris 44: stack = StackArray() - Membuat object stack dari class StackArray.

Baris 45: pilih = 0 - Variabel untuk menyimpan pilihan menu.

Baris 46: while pilih != 5: - Perulangan program selama user belum memilih keluar.

Baris 47–52: print("\n=== STACK (Array) ===")

print("1. Tambah Edit")

print("2. Mengurungkan Edit")

print("3. Lihat Edit Terakhir")

print("4. Tampilkan Riwayat Edit")

print("5. Keluar Program")

digunakan untuk menampilkan menu program.

Baris 53: try: - Mencoba menjalankan input user.

Baris 54: pilih = int(input("Pilih: ")) - Menerima input pilihan menu dari user.

Baris 55–57: except ValueError:
print("Input tidak valid!")
continue - Menangani error jika input bukan angka.

Baris 58: if pilih == 1: - Jika user memilih menu tambah edit.

Baris 59: try: - Mencoba menerima input edit.

Baris 60: val = input("Masukkan jenis edit: ") - Input jenis edit dari user.

Baris 61: stack.push(val) - Menambahkan edit ke stack.

Baris 62–63: except ValueError:
print("Input tidak valid!") - Menangani error input.

Baris 64–65: elif pilih == 2:
stack.pop() - Menjalankan fitur undo.

Baris 66–67: elif pilih == 3:
stack.peek() - Menampilkan edit terakhir.

Baris 68–69: elif pilih == 4:
stack.display() - Menampilkan seluruh riwayat edit.

Baris 70–71: elif pilih == 5:
print("Program selesai.") - Keluar dari program.

Baris 72–73: else:
print("Pilihan tidak valid!"). - Menampilkan pesan jika pilihan menu tidak tersedia.

Baris 76: if name == "main": - Mengecek apakah file dijalankan langsung.

Baris 77: main() - Menjalankan function main().


## Output
<img width="213" height="923" alt="Output StackArray" src="https://github.com/user-attachments/assets/5c436f28-f8d4-404b-9824-dd25087d373a" />

Output tersebut menunjukkan proses penggunaan program Stack berbasis Array untuk menyimpan riwayat edit. Saat program dijalankan, sistem menampilkan menu utama yang berisi pilihan tambah edit, mengurungkan edit, lihat edit terakhir, tampilkan riwayat edit, dan keluar program. Pada awalnya pengguna memilih menu 1 yaitu tambah edit. Program meminta pengguna memasukkan jenis edit, lalu pengguna memasukkan “filter”. Setelah itu program menampilkan pesan “Edit filter ditambahkan”, artinya data berhasil dimasukkan ke dalam stack. Selanjutnya pengguna kembali memilih menu 1 dan memasukkan jenis edit “elemen”. Program kemudian menyimpan data tersebut ke dalam stack dan menampilkan pesan “Edit elemen ditambahkan”. Kemudian pengguna kembali memilih menu tambah edit dan memasukkan “foto”. Program kembali menambahkan data tersebut ke stack dan menampilkan pesan “Edit foto ditambahkan”. Setelah itu pengguna menambahkan lagi jenis edit “teks”. Data “teks” menjadi data terakhir yang masuk sehingga berada di posisi paling atas stack. Program menampilkan pesan “Edit teks ditambahkan”. Karena stack menggunakan prinsip LIFO (Last In First Out), maka data yang terakhir masuk akan menjadi data pertama yang keluar. Berikut urutan isi stack setelah semua data ditambahkan:

- teks

- foto

- elemen

- filter

Lalu pengguna memilih menu 2 yaitu mengurungkan edit. Program menghapus data paling atas yaitu “teks” dan menampilkan pesan “Mengurungkan edit teks berhasil”. Ini menunjukkan operasi pop pada stack. Setelah data teks dihapus dan isi stack menjadi:

- foto

- elemen

- filter
  
Kemudian pengguna memilih menu 3 yaitu lihat edit terakhir. Program menampilkan “Edit terakhir: foto” karena setelah teks dihapus, data paling atas sekarang adalah “foto”. Selanjutnya pengguna memilih menu 4 yaitu tampilkan riwayat edit. Program menampilkan seluruh isi stack dari yang terbaru sampai yang terlama:

- foto
  
- elemen

- filter

Urutan tersebut sesuai dengan konsep stack, yaitu data paling atas ditampilkan lebih dahulu. Terakhir pengguna memilih menu 5 untuk keluar dari program. Program kemudian menampilkan pesan “Program selesai”, yang berarti program telah dihentikan.

## Link Youtube

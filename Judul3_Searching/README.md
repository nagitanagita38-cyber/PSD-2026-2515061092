# Program pencarian barang menggunakan algoritma Binary Search dengan bahasa pemrograman Python
# Deskripsi Singkat
Program ini dibuat untuk menemukan informasi tentang barang pada sebuah daftar yang telah tersusun dengan baik. Pengguna diminta untuk memasukkan nama barang yang ingin dicari, setelah itu program akan melaksanakan pencarian menggunakan algoritma Binary Search. Setelah barang tersebut ditemukan, program akan menunjukkan jumlah barang yang tersedia dan lokasi penyimpanannya, seperti pada lemari, kursi, kasur, atau meja.

Algoritma yang digunakan dalam program ini ialah Binary Search, yang merupakan metode pencarian dengan cara membagi data menjadi dua bagian secara berulang sampai data tersebut ditemukan. Struktur data yang diterapkan adalah array/list karena barang-barang disimpan dalam daftar yang sudah terurut. Binary Search dipilih karena proses pencariannya lebih cepat dan efisien dibandingkan dengan pencarian Sequential Search, terutama ketika jumlah data sangat banyak.

# Source Code
<img width="1291" height="857" alt="SourceCode BinarySearch" src="https://github.com/user-attachments/assets/b061f6b0-e97e-43db-ba37-5df8ac1b17a6" />
Baris 1 - def binary_search(data, n, target):
Membuat fungsi Binary Search untuk mencari barang dalam list.

Baris 2 - l = 0
Menentukan batas kiri array dimulai dari indeks 0.

Baris 3 - r = n - 1
Menentukan batas kanan array pada indeks terakhir.

Baris 4 - pos = -1
Menyimpan posisi data, -1 berarti data belum ditemukan.

Baris 5 - while l <= r:
Perulangan berjalan selama batas kiri tidak melewati batas kanan.

Baris 6 - m = l + (r - l) // 2
Menghitung indeks tengah atau median.

Baris 7 - print(f"Median: {m}, nilai: {data[m]}")
Menampilkan indeks median dan nilai pada posisi median.

Baris 8 - if data[m] == target:
Mengecek apakah data pada median sama dengan target.

Baris 9 - pos = m
Menyimpan posisi data yang ditemukan.

Baris 10 - break
Menghentikan perulangan karena data sudah ditemukan.

Baris 11 - elif data[m] < target:
Mengecek apakah target lebih besar dari data median.

Baris 12 - print("Mencari di kanan")
Menampilkan bahwa pencarian dilanjutkan ke kanan.

Baris 13 - l = m + 1
Menggeser batas kiri ke kanan median.

Baris 14 - else:
Dijalankan jika target lebih kecil dari data median.

Baris 15 - print("Mencari di kiri")
Menampilkan bahwa pencarian dilanjutkan ke kiri.

Baris 16 - r = m - 1
Menggeser batas kanan ke kiri median.

Baris 17 - return pos
Mengembalikan posisi data yang ditemukan.

Baris 19 - def main():
Membuat fungsi utama program.

Baris 20 - data = [...]
Menyimpan daftar barang ke dalam list.

Baris 21 - n = len(data)
Menghitung jumlah data pada list.

Baris 22 - print(f"Data array: {data}")
Menampilkan seluruh isi data barang.

Baris 23 - while True:
Melakukan perulangan untuk input.

Baris 24 - try:
Mencoba menjalankan kode yang mungkin error.

Baris 25 - target = input("Masukkan barang yang ingin dicari: ")
Meminta pengguna memasukkan nama barang.

Baris 26 - break
Menghentikan perulangan jika input berhasil.

Baris 27 - except ValueError:
Menangani error jika input tidak valid.

Baris 28 - print("Input tidak valid, silakan masukkan nama barang yang ingin dicari.")
Menampilkan pesan kesalahan input.

Baris 29 - pos = binary_search(data, n, target)
Memanggil fungsi Binary Search untuk mencari barang.

Baris 30 - counter = data.count(target)
Menghitung jumlah barang yang sama dalam list.

Baris 31 - if pos <= 4:
Mengecek apakah posisi barang berada pada indeks 0–4.

Baris 32 - print(f"Barang {data[pos]} ditemukan sebanyak {counter} kali di Lemari")
Menampilkan barang ditemukan di lemari.

Baris 33 - elif pos <= 7:
Mengecek apakah posisi barang berada pada indeks 5–7.

Baris 34 - print(f"Barang {data[pos]} ditemukan sebanyak {counter} kali di Kursi")
Menampilkan barang ditemukan di kursi.

Baris 35 - elif pos <=11:
Mengecek apakah posisi barang berada pada indeks 8–11.

Baris 36 - print(f"Barang {data[pos]} ditemukan sebanyak {counter} kali di Kasur")
Menampilkan barang ditemukan di kasur.

Baris 37 - elif pos <=14:
Mengecek apakah posisi barang berada pada indeks 12–14.

Baris 38 - print(f"Barang {data[pos]} ditemukan sebanyak {counter} kali di Meja")
Menampilkan barang ditemukan di meja.

Baris 39 - else:
Dijalankan jika barang tidak ditemukan.

Baris 40 - print("Tidak ditemukan")
untuk menampilkan pesan barang tidak ditemukan.

Baris 42 - 43 -  if __name__ == "__main__":
main() untuk menjalankan fungsi utama program.

#  Output Program
<img width="1255" height="142" alt="Output BinarySearch" src="https://github.com/user-attachments/assets/5ce3c69f-ce2d-44ca-b532-271cfb43daad" />

- Program pertama menampilkan seluruh data barang yang ada di dalam array.
  
- Pengguna memasukkan kata “Baju” sebagai barang yang ingin dicari.
  
- Binary Search memulai pencarian dari nilai tengah array, yaitu indeks 7 dengan nilai “Kunci”.
  
- Karena “Baju” lebih kecil dari “Kunci”, pencarian berpindah ke bagian kiri array.
  
- Program kembali mencari nilai tengah pada bagian kiri dan mendapatkan indeks 3 dengan nilai “Buku”.
  
- Karena “Baju” masih lebih kecil dari “Buku”, pencarian kembali berpindah ke kiri.
  
- Pada pencarian berikutnya program mendapatkan indeks 1 dengan nilai “Baju”.
  
- Data berhasil ditemukan dan program menghitung jumlah “Baju” sebanyak 2 kali.
  
- Karena posisi indeks berada pada rentang 0–4, maka lokasi barang berada di Lemari.

# Link Youtube
https://youtu.be/VLLjN-uZ958?si=GlYOrXMYds9v85-X

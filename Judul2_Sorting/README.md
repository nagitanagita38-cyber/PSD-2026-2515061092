# Pengurutan Ukuran Gelas Menggunakan Algoritma Bubble Sort (Descending)
# Deskripsi Singkat
Program ini digunakan untuk mengurutkan ukuran yang dimasukkan oleh pengguna. Pengguna diminta untuk memasukkan jumlah gelas terlebih dahulu, kemudian memasukkan ukuran gelas secara random dalam bentuk angka. Setelah itu, program akan mengurutkan data tersebut. Algoritma yang digunakan pada program tersebut adalah Bubble Sort, yiatu membandingkan dua eleman yang berdekatan lalu menukarnya jika tidak berurutan. Pada program ini, pengurutan dilakukan secara descending (pengurutan dari yang terbesar ke yang terkecil).
# Source Code
<img width="748" height="868" alt="Screenshot 2026-04-30 183742" src="https://github.com/user-attachments/assets/f89d7566-22dc-40eb-b110-2ec92a563e89" />
Baris 1 - def tukar(arr, i, j): Membuat fungsi untuk menukar posisi dua elemen dalam array

Baris 2 - temp = arr[i] Menyimpan sementara nilai pada indeks i

Baris 3 - arr[i] = arr[j] Mengganti nilai indeks i dengan nilai indeks j

Baris 4 - arr[j] = temp Mengisi indeks j dengan nilai awal indeks i

Baris 6 - def bubble_sort(arr, n): Fungsi utama untuk melakukan pengurutan

Baris 7 - for i in range(n - 1): Loop untuk jumlah iterasi pengurutan

Baris 8 - for j in range(n - i - 1): Loop untuk membandingkan elemen yang berdekatan

Baris 9 - if arr[j] < arr[j + 1]: Jika elemen kiri lebih kecil dari kanan, maka tukar (descending) dan begitupun sebaliknya jika elemen kiri lebih besar, maka tukar (ascending)

Baris 10 - tukar(arr, j, j + 1) Memanggil fungsi tukar

Baris 11 - def main(): Fungsi utama program

Baris 13 - n = int(input("Masukkan jumlah gelas:")) Input jumlah gelas.

Baris 14 - except ValueError: Menangani jika input bukan angka
 
Baris 15 - print untuk angka yang diinputkan tidak valid

Baris 16 - return digunakan untuk menghentikan fungsi main agar program yang salah input akan langsung keluar dari fungsi dan tidak dilanjutkan

Baris 17 - arr = [] Membuat list kosong untuk menyimpan data

Baris 18 - user memasukkan ukuran gelas

Baris 19 - for i in range(n): Loop input ukuran gelas

Baris 20 - while True: Memastikan input valid

Baris 22 - nilai = int(input()) Input ukuran gelas

Baris 23 - arr.append(nilai) Menambahkan ke list

Baris 27 - print(f"Gelas sebelum diurutkan: {arr}") Menampilkan data sebelum diurutkan

Baris 28 - bubble_sort(arr, n) Memanggil fungsi pengurutan

Baris 29 - print("Gelas setelah diurutkan") Menampilkan hasil setelah diurutkan

Baris 31 - print(arr[i], end=" "): digunakan untuk mengambil nilai  dari array berdasarkan index, agar hasil print tidak pindah baris, tetapi hanya dipisahkan spasi

Baris 35 - 36 - menjalankan fungsi main() saat program dijalankan

# Output Program
<img width="563" height="196" alt="Screenshot 2026-04-30 192822" src="https://github.com/user-attachments/assets/1e814bc0-5f49-4d6e-883b-e2c82dcfc5bf" />
Pertama, pengguna diminta memasukkan jumlah gelas sebanyak 5.
Kemudian, pengguna diminta memasukkan ukuran gelas: 850, 250, 1900, 2100, 300.
Program menampilkan data awal sesuai input dalam bentuk list.
Setelah diproses menggunakan algoritma Bubble Sort, data diurutkan secara descending (pengurutan dari terbesar ke terkecil).
Hasil akhir menjadi: 2100, 1900, 850, 300, 250.
Ini menunjukkan bahwa proses pengurutan berjalan dengan benar tanpa error.

# Link Youtube
https://youtu.be/W6ve3JcwhQY?si=7AT6LDGYK2BOB1cw

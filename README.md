# Pendataan Siswa Menggunakan List 1 Dimensi pada Python
# Deskripsi Singkat
Program ini adalah aplikasi sederhana menggunakan Python untuk mengelola data siswa, seperti menginput data siswa, menampilkan data siswa, dan menghapus data siswa. Datanya disimpan dalam sebuah list, jadi setiap nama siswa ada di satu daftar. Program ini dibuat dengan konsep menu interaktif pilih_menu() untuk tampilan menu, while running() yang membuat menu itu muncul, dan input("Pilih Menu: ") untuk menerima inputan dari user.

Dalam penerapannya, program ini memakai struktur data list untuk menyimpan data siswa secara dinamis yaitu kapasitasnya bisa bertambah atau berkurang secara otomatis saat program berjalan. Setiap data yang dimasukkan akan ditambahkan ke dalam list dengan append(), sedangkan untuk menghapus dengan pop(). Program ini juga memakai perulangan while supaya tetap berjalan sampai pengguna memilih keluar, serta percabangan if-elif-else untuk menentukan proses sesuai menu yang di pilih. Dengan cara ini, program bisa mengelola data sederhana m,enggunakan Python. 

# Source Code
<img width="822" height="1216" alt="merged (2)" src="https://github.com/user-attachments/assets/eb09e691-dfb4-41e4-867f-74e04469d78b" />
Baris 1 - membuat fungsi pilih_menu() 

Baris 2 - menampilkan opsi 1 (input data siswa)

Baris 3 - menampilkan opsi 2 (lihat data siswa)

Baris 4 - menampilkan opsi 3 (hapus data siswa)

Baris 5 - menampilkan opsi 4 (keluar program)

Baris 7 - membuat fungsi main() yang di mana ini adalah fungsi utama program

Baris 8 - membuat list data_siswa untuk menyimpan nama siswa

Baris 9 - membuat variabel running untuk mengontrol program tetap jalan

Baris 10 - membuat perulangan selama running = True (program terus jalan)

Baris 11 - memanggil fungsi pilih_menu() untuk menampilkan menu

Baris 13 - user memasukkan pilihan menu

Baris 14 - mencoba mengubah input jadi angka

Baris 15 - jika input bukan angka maka error, akan tampil pesan “Pilihan tidak valid”

Baris 16 - ulang kembali ke menu

Baris 17 - jika user pilih menu 1

Baris 18 - input nama siswa

Baris 19 - menambahkan nama ke list data_siswa

Baris 20 - menampilkan pesan "Data Siswa Berhasil Diinput"

Baris 22 - jika user pilih menu 2

Baris 23 - cek apakah data kosong

Baris 24 - jika kosong tampil pesan "Belum Ada Data Siswa."

Baris 25 - jika ada data lanjut

Baris 26 - tampilkan judul daftar

Baris 27–28 - menampilkan semua data siswa dengan nomor

Baris 30 - jika user pilih menu 3

Baris 31 - cek apakah data kosong

Baris 32 - jika kosong tampil pesan "Data tidak ada."

Baris 33 - jika ada data lanjut

Baris 34–35 - tampilkan semua data siswa

Baris 37 - input nomor data yang mau dihapus

Baris 38 - hapus data dari list

Baris 39 - tampil pesan "Data berhasil dihapus."

Baris 41 - jika error tampil pesan “pilihan tidak valid”

Baris 43 - jika user pilih menu 4

Baris 44 - menghentikan program (running = False)

Baris 45 - tampil pesan program selesai

Baris 46 - jika input bukan 1–4

Baris 47 - tampil pesan “pilihan tidak valid”

Baris 49-50 - menjalankan fungsi main() saat program dijalankan

# Output Program
<img width="455" height="1941" alt="merged (3)" src="https://github.com/user-attachments/assets/71f17ad8-bd0b-4bcc-bb57-6d5f9c174435" />
Program pertama kali nmenampilkan menu:

- Input data siswa
  
- Tampilkan data siswa
  
- Hapus data siswa
  
- Keluar
- 
Yang artinya program siap dipakai dan nunggu input user.

User beberapa kali pilih menu 1, jadi dia masukin nama siswa satu per satu:

Nagita

Ade Nadya

Cornelia

Marsalena

Syifa

Yohana

Setiap nama yang dimasukkan langsung disimpan ke list data_siswa.

Saat pilih menu 2, program menampilkan semua data siswa kasih nomor urut otomatis

Hasilnya:

1 Nagita

2 Ade Nadya

3 Cornelia

4 Marsalena

5 Syifa

6 Yohana

Ini bukti semua data sudah tersimpan dengan benar.

Saat pilih menu 3:

program menampilkan semua data terlebih dahiulu, lalu user disuruh pilih nomor yang mau dihapus.

User pilih: 1 (Nagita)

Maka, Nagita dihapus dari list.

Saat ditampilkan lagi:

1 Ade Nadya

2 Cornelia

3 Marsalena

4 Syifa

5 Yohana

Nagita sudah hilang karena berhasil dihapus dan nomor 1 menjadi Ade Nadya, nomor 2 menjadi Cornelia, nomor 3 menjadi Marsalena, nomor 4 Syifa, dan nomor 5 menjadi Yohana.

Saat pilih 4:

program berhenti jalan akan muncul tulisan Program selesai.

# Link Youtube

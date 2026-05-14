# Aplikasi Riwayat Edit Menggunakan Stack Array
## Deskripsi Singkat
Program ini adalah simulasi dari sistem riwayat pengeditan seperti fungsi undo dalam aplikasi yang digunakan untuk mengedit, seperti untuk foto, dokumen, atau video. Program ini dikembangkan dengan memanfaatkan struktur data _Stack_ yang berbasis array. Stack adalah sebuah struktur data yang beroperasi berdasarkan prinsip LIFO (Last In First Out), yang berarti elemen terakhir yang dimasukkan adalah elemen pertama yang akan dikeluarkan. Prinsip ini mirip dengan tumpukan piring, di mana piring yang paling terakhir diletakkan di atas akan menjadi piring yang pertama kali diambil.

Dalam aplikasi ini, setiap tindakan pengeditan yang dilakukan oleh pengguna akan disimpan dalam stack menggunakan metode push. Saat pengguna mengakses fungsi undo, maka pengeditan terakhir akan dihapus dengan menggunakan metode pop. Selain itu, aplikasi juga dilengkapi dengan fitur untuk melihat pengeditan terakhir dengan menggunakan peek, serta menampilkan seluruh riwayat pengeditan melalui tampilan display. Penggunaan struktur data stack sangat tepat untuk aplikasi undo karena proses penghapusan biasanya dilakukan pada data yang terakhir kali dimasukkan. Program ini juga mengimplementasikan konsep array sebagai sarana penyimpanan data sehingga pengelolaan riwayat pengeditan dapat dilakukan secara lebih teratur dan efisien.

## Source Code
<img width="402" height="893" alt="Source Code StackArray" src="https://github.com/user-attachments/assets/8779318e-67cf-4451-8145-1d9c48c8f360" />



## Output
<img width="213" height="923" alt="Output StackArray" src="https://github.com/user-attachments/assets/5c436f28-f8d4-404b-9824-dd25087d373a" />

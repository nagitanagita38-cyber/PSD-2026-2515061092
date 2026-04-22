def pilih_menu():
    print("1. Input Data Siswa")
    print("2. Tampilkan Data Siswa")
    print("3. Hapus Data Siswa")
    print("4. Keluar")

def main():
    data_siswa = []
    running = True
    while running:
        pilih_menu()
        try:
            choice = int(input("Pilih Menu: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue
        if choice == 1:
            nama = input("Masukkan Nama Siswa: ")
            data_siswa.append(nama)
            print("Data siswa berhasil diinput.")

        elif choice == 2:
            if len(data_siswa) == 0:
                print("Belum ada data siswa.")
            else:
                print("Daftar Siswa:")
                for i in range(len(data_siswa)):
                    print(i+1, data_siswa[i])

        elif choice == 3:
            if len(data_siswa) == 0:
                print("Data tidak ada.")
            else:
                for i in range(len(data_siswa)):
                    print(i+1, data_siswa[i])
                try:
                    hapus = int(input("Pilih nomor siswa yang dihapus: "))
                    data_siswa.pop(hapus-1)
                    print("Data berhasil dihapus.")
                except:
                    print("Pilihan tidak valid.")
                    
        elif choice == 4:
            running = False
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
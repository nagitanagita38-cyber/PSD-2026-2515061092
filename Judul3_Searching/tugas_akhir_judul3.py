def binary_search(data, n, target): 
    l = 0 
    r = n - 1 
    pos = -1 
    while l <= r: 
        m = l + (r - l) // 2 
        print(f"Median: {m}, nilai: {data[m]}") 
        if data[m] == target: 
            pos = m 
            break 
        elif data[m] < target: 
            print("Mencari di kanan") 
            l = m + 1 
        else: 
            print("Mencari di kiri") 
            r = m - 1 
    return pos 
 
def main(): 
    data = ["Baju", "Baju", "Botol", "Buku", "Buku", "Headset", "Kabel", "Kunci", "Laptop", "Parfum", "Pensil", "Pulpen", "Sisir", "Tas", "Tipe-X"]
    n = len(data) 
    print(f"Data array: {data}") 
    while True: 
        try: 
            target = input("Masukkan barang yang ingin dicari: ")
            break 
        except ValueError: 
            print("Input tidak valid, silakan masukkan nama barang yang ingin dicari tidak ada.") 
    pos = binary_search(data, n, target) 
    counter = data.count(target)
    if pos <= 4: 
        print(f"Barang {data[pos]} ditemukan sebanyak {counter} kali di Lemari") 
    elif pos <= 7:
        print(f"Barang {data[pos]} ditemukan sebanyak {counter} kali di Kursi")
    elif pos <=11:
        print(f"Barang {data[pos]} ditemukan sebanyak {counter} kali di Kasur")
    elif pos <=14:
        print(f"Barang {data[pos]} ditemukan sebanyak {counter} kali di Meja")
    else: 
        print("Tidak ditemukan") 
 
if __name__ == "__main__": 
    main()

class StackArray: 
    def __init__(self, max_size=100): 
        self.MAX = max_size 
        self.st = [None] * self.MAX 
        self.top_idx = -1 
 
    def is_empty(self): 
        return self.top_idx == -1 
 
    def is_full(self): 
        return self.top_idx == self.MAX - 1 
 
    def push(self, x): 
        if self.is_full(): 
            print("Riwayat penuh") 
            return 
        self.top_idx += 1 
        self.st[self.top_idx] = x 
        print(f"Edit {x} ditambahkan") 
 
    def pop(self): 
        if self.is_empty(): 
            print("Tidak ada riwayat edit") 
            return 
        print(f"Mengurungkan edit {self.st[self.top_idx]} berhasil") 
        self.top_idx -= 1 
 
    def peek(self): 
        if self.is_empty(): 
            print("Tidak ada riwayat edit.") 
            return 
        print(f"Edit terakhir: {self.st[self.top_idx]}") 
 
    def display(self): 
        if self.is_empty(): 
            print("Belum ada riwayat edit") 
            return 
        print("Tampilkan riwayat edit terbaru: ") 
        for i in range(self.top_idx, -1, -1): 
            print("-", self.st[i])
        print()
    
def main(): 
    stack = StackArray() 
    pilih = 0 
    while pilih != 5: 
        print("\n=== STACK (Array) ===") 
        print("1. Tambah Edit") 
        print("2. Mengurungkan Edit") 
        print("3. Lihat Edit Terakhir") 
        print("4. Tampilkan Riwayat Edit") 
        print("5. Keluar Program") 
        try: 
            pilih = int(input("Pilih: ")) 
        except ValueError: 
            print("Input tidak valid!")
            continue 
        if pilih == 1: 
            try: 
                val = input("Masukkan jenis edit: ") 
                stack.push(val) 
            except ValueError: 
                print("Input tidak valid!") 
        elif pilih == 2: 
            stack.pop() 
        elif pilih == 3: 
            stack.peek() 
        elif pilih == 4: 
            stack.display() 
        elif pilih == 5: 
            print("Program selesai.") 
        else: 
            print("Pilihan tidak valid!") 
 
 
if __name__ == "__main__": 
    main() 
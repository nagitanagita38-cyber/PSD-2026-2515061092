class Node: 
    def __init__(self, key): 
        self.key = key 
        self.left = None 
        self.right = None 
 
class BSTLanjut: 
    def __init__(self): 
        self.root = None 
 
    def insert_node(self, root, key): 
        if root is None: 
            return Node(key) 
        if key < root.key: 
            root.left = self.insert_node(root.left, key) 
        elif key > root.key: 
            root.right = self.insert_node(root.right, key) 
        return root 
 
    def insert(self, key): 
        self.root = self.insert_node(self.root, key) 
 
    def find_min_node(self, root): 
        current = root 
        while current is not None and current.left is not None: 
             current = current.left 
        return current 
 
    def delete_node(self, root, key): 
        if root is None: 
            return None 
        if key < root.key: 
            root.left = self.delete_node(root.left, key) 
        elif key > root.key: 
            root.right = self.delete_node(root.right, key) 
        else: 
            if root.left is None and root.right is None: 
                return None 
            elif root.left is None: 
                return root.right 
            elif root.right is None: 
                return root.left 
            else: 
                successor = self.find_min_node(root.right) 
                root.key = successor.key 
                root.right = self.delete_node(root.right, successor.key) 
        return root 
 
    def delete(self, key): 
        self.root = self.delete_node(self.root, key) 
 
    def level_order(self, root): 
        if root is None: 
            print("(kosong)") 
            return 
        queue = [] 
        queue.append(root)
        while len(queue) > 0: 
            current = queue.pop(0) 
            print("-", current.key) 
            if current.left is not None: 
                queue.append(current.left) 
            if current.right is not None: 
                queue.append(current.right) 
        print() 

    def rute_terpendek(self):
        if self.root is None:
            return None
        return self.find_min_node(self.root).key

    def rute_tercepat(self):
        if self.root is None:
            return None

        current = self.root
        while current.right is not None:
            current = current.right
            return current.key
    
def main():
    bst = BSTLanjut()
    pilih = 0
    while pilih != 6:
        print("\n=== MENU BST LANJUT (RUTE) ===")
        print("1. Simpan Rute")
        print("2. Hapus Rute")
        print("3. Tampilkan Susunan Rute")
        print("4. Rute Terpendek")
        print("5. Rute Tercepat")
        print("6. Keluar")

        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            x = input("Masukkan rute yang dicari: ")
            bst.insert(x)
            print(f"Rute '{x}' berhasil disimpan")

        elif pilih == 2:
            x = input("Hapus rute yang dicari: ")
            bst.delete(x)
            print(f"Rute '{x}' berhasil dihapus")

        elif pilih == 3:
            print("Susunan rute yang dicari: ")
            bst.level_order(bst.root)

        elif pilih == 4:
            hasil = bst.rute_terpendek()
            print("Rute terpendek yang dicari:", hasil)

        elif pilih == 5:
            hasil = bst.rute_tercepat()
            print("Rute tercepat yang dicari:", hasil)

        elif pilih == 6:
            print("Program selesai")

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
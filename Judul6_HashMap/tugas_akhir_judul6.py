class Node:
    def __init__(self, key, value):
       self.key = key
       self.value = value
       self.next = None

class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE
    
    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE
 
    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None
    
    def display(self):
        print("\nIsi Hash Table (Separate Chaining):")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            current = self.table[i]
            while current is not None:
                print(f"({current.key},{current.value}) -> ", end="")
                current = current.next
        print("NONE")


def main():
    hashmap = HashMapSeparateChaining()
    hashmap.insert(101, "Binder")
    hashmap.insert(111, "Canvas")
    hashmap.insert(121, "Kuas")
    hashmap.insert(112, "Cat Air")
    hashmap.insert(141, "Palet")
    hashmap.insert(113, "Cat Minyak")
    hashmap.insert(131, "Sketchbook")
    hashmap.display()

    while True:
        kode_barang = int(input("cari kode barang :"))

        if kode_barang == 0:
            print("Program selesai.")
        
        hasil = hashmap.search(kode_barang)

        if hasil is not None:
            print(f"\nKode Barang : {hasil.key}")
            print(f"\nNama Barang : {hasil.value}")
        else:
            print(f"\nBarang dengan kode {kode_barang} tidak ditemukan.")

if __name__ == "__main__":
    main()

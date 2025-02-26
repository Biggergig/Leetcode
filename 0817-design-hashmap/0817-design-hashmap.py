class MyHashMap:

    def __init__(self):
        self.table = [("Empty", None)]*(1<<15)
        self.prime = 991 # My fav number!
    
    def _hash(self,v):
        return hash(v)%len(self.table)
    def _step(self,v):
        return (hash(v)+v)%self.prime

    def put(self, key: int, value: int) -> None:
        bi = self._hash(key)
        i = bi
        exp = 0
        while self.table[i][0] not in ("Open","Empty",key):
            i = (bi + self.prime ** exp)%len(self.table)
            exp+=1
        self.table[i] = (key, value)
    def get(self, key: int) -> int:
        bi = self._hash(key)
        i = bi
        exp = 0
        while self.table[i][0] not in ("Empty",key):
            i = (bi + self.prime ** exp)%len(self.table)
            exp+=1
        return -1 if self.table[i][0] == "Empty" else self.table[i][1]

    def remove(self, key: int) -> None:
        bi = self._hash(key)
        i = bi
        exp = 0
        while self.table[i][0] not in ("Empty", key):
            i = (bi + self.prime ** exp)%len(self.table)
            exp+=1
        if self.table[i][0] == key:
            self.table[i] = ("Open",None)



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
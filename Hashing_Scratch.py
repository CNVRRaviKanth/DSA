class HashMap:
    def __init__(self,size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self,key):
        return hash(key)%self.size
    
    def put(self,key,value):
        idx = self._hash(key)
        bucket = self.table[idx]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i] = (key,value)
                return 
            
        bucket.append((key,value))

    def get(self,key):
        idx = self._hash(key)
        bucket = self.table[idx]

        for k,v in bucket:
            if k == key:
                return v
            
        return "Key not found!"
    
    def delete(self,key):
        idx = self._hash(key)
        bucket = self.table[idx]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                return "Removed the key successfully!!"
            
        return "Key not found!"
    
    def display(self):
        for i in range(len(self.table)):
            print(self.table[i])


Map = HashMap(10)
Map.put("apple", 10)
Map.put("banana", 20)
Map.put("apple", 30)  # update
Map.display()
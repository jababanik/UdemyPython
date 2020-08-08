# Python program to demonstrate the 
# use of join function to join list 
# elements without any separator. 
  
# Joining with empty separator 
list1 = ['g','e','e','k', 's']  
print("".join(list1)) 

class AlgoHashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]

    def create_buckets(self):
        pass

    def set_val(self, key, value):
        pass

    def get_val(self, key):
        pass

    def __str__(self):
        #return "Hello !"
        return "".join(str(item) for item in self.hash_table)

hash_table = AlgoHashTable(256) # 256 lists are created
print(hash_table)

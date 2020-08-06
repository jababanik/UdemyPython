class Node:
    def __init__(self, data = None ):
        self.right = None
        self.left = None
        self.data = data
        
class BST:
    def __init__(self):
        self.root = None
    
    def entry(self, x):
        if not isinstance(x, Node):
            x = Node(x)
        ptr = self.root
        while True:
            if ptr is None:
                ptr = x
                break
            elif ptr.data < x.data:
                ptr = ptr.right
            else:
                ptr = ptr.left
             
    
    def print_recur(self,ptr):
        if ptr is None:
            return
        self.print_recur(ptr.left)
        print("\t"+str(ptr.data)+"\t")
        self.print_recur(ptr.right)
        
    
    
my_obt = BST()
my_obt.entry(2)
my_obt.entry(101)
my_obt.entry(20)
my_obt.entry(6)
my_obt.entry(5)
my_obt.entry(7)

my_obt.print_recur(my_obt.root)


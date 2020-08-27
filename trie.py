class Node:
    def __init__(self):
        self.list_of_Nodes = [None]*26
        self.isThisTheEnd = False
    
class Trie:
    def __init__(self):
        self.root = Node()
    
    def _indexEncoding(self,char):
        return ord(char)-ord('a')
    
    def add(self,word):
        ptr = self.root
        
        for ch in word:
            index = self._indexEncoding(ch)
            
            if not ptr.list_of_Nodes[index]:
                ptr.list_of_Nodes[index] = Node()
                
            ptr = ptr.list_of_Nodes[index]
            
        ptr.isThisTheEnd = True
        
    def search(self,word):
        ptr = self.root
        for ch in word:
            next = self._indexEncoding(ch)
            if ptr.list_of_Nodes[index] is not None:
                ptr = ptr.list_of_Nodes[next]
            else:    
                return "Not exist"
        return ptr is not None and ptr.isThisTheEnd
    
    def delete(self,word):
        ptr = self.root
        for ch in word:
            next = self._indexEncoding(ch)
            if ptr.list_of_Nodes[index] is not None:
                ptr = ptr.list_of_Nodes[next]
            else:    
                return "Not exist"
        if ptr is not None:
            ptr.isThisTheEnd = False
            return
        return "Not exist"
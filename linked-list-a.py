class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append_val(self, x):
        '''add x to the end of the list'''
        if not isinstance(x, Node):
            x = Node(x) # creating objof Node class
        if self.head == None:
            self.head = x
        else:
            self.tail.next = x
        self.tail = x

    def __str__(self):
        # [5->4->10->1]
        to_print = ""
        curr = self.head
        while curr is not None:
            to_print += str(curr.data) + "->"
            curr = curr.next
        if to_print:
            return "[" + to_print[:-2] + "]"
        return "[]"

    def add_to_start(self, x):
        '''add x to the left of the list making it the head'''
        if not isinstance(x,Node):
            x = Node(x)
        x.next = self.head
        self.head = x
        
 
    def search_val(self, x):
        '''return indices where x was found'''
        indi = []
        ptr = self.head
        index = 0
        while ptr is not None:
            if ptr.data == x:
                indi.append(index)
            index += 1
            ptr = ptr.next
        return indi
            

    def remove_val_by_index(self, x):
        '''remove and return value at index x provided as parameter'''
        ptr = self.head
        for counter in range(x-1):
            ptr = ptr.next
        data_to_return = ptr.next.data
        p2 = ptr.next
        ptr.next = ptr.next.next
        del p2
        return data_to_return
        

    def length(self):
        '''return the length of the list, rep'd by number of nodes'''
        ptr = self.head
        c = 1
        while ptr is not None:
            ptr = ptr.next
            c =+ 1
        return c
            

    def reverse_list_recur(self, current, previous):
        '''reverse the sequence of node pointers in the linked list'''
        # Given [1->2->3->4->5] reverse pointers [1<-2<-3<-4<-5]
        # Turning list to [5->4->3->2->1]
        if self.head == None:
            return
        elif current.next == None:
            current.next = previous
            self.head, self.tail = self.tail, self.head
        else:
            next_node = current.next
            current.next = previous
            self.reverse_list_recur(next_node, current)
        

        

my_list = LinkedList()
print(my_list)
my_list.append_val(1)
my_list.append_val(2)
my_list.append_val(3)
my_list.append_val(2)
my_list.append_val(4)
my_list.append_val(5)
my_list.add_to_start(7)
my_list.append_val(2)
print(my_list.search_val(2))
print(my_list.remove_val_by_index(3))
print(my_list)
my_list.reverse_list_recur(my_list.head,None)
print(my_list)

class Node():
    def __init__(self,d):
        self.data = d
        self.next = None
        self.prev = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def add(self, data):
        new_node = Node(data)
        if(self.head == None):
            self.head = self.tail = new_node
            return True
        # O(1) — no loop needed!
        self.tail.next = new_node
        new_node.prev = self.tail
        new_node.next = None
        self.tail = new_node
        return True
        '''
        #discarded this as its time complexity is O(n) making it unefficient 
        temp_node=self.head
        while(temp_node.next):
            temp_node=temp_node.next
        temp_node.next= new_node
        new_node.prev= temp_node
        new_node.next= None
        self.tail = new_node
        return True
        '''
        
        
        

    
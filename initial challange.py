class Node():
    def __init__(self,d):
        self.data = d
        self.next = None
        self.prev = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def add(self, data):
        new_node = Node(data)
        if(self.head == None):
            self.head = self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
            self.size+=1
            return True
        # O(1) — no loop needed!
        self.tail.next = new_node
        new_node.prev = self.tail
        new_node.next = self.head
        self.head.prev= new_node
        self.tail = new_node
        self.size+=1
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
    def remove_node(self, node):
        if self.head is None:
            return None
        # If it's the last remaining node (size is 1), clear head and tail
        if self.size == 1:
            self.head = self.tail = None
            self.size = 0
            return None
        # Update head/tail pointers if we are removing them
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        # Bypass the node to remove it from the circle
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node.next

    def simulate(self, k):
        if self.head is None:
            print("No one in the desert!")
            return None
        current = self.head
        # Keep eliminating until only 1 person remains (size is 1)
        while self.size > 1:
            # Count k-1 times to find the k-th person
            for _ in range(k - 1):
                current = current.next
            print(f"Person {current.data} is eliminated!")
            # Remove current person and get the next starting point
            current = self.remove_node(current)

        print(f"The survivor is Person {self.head.data}!")
        return self.head.data

if __name__ == "__main__":
    # Example: 5 people in the desert, every 3rd person is eliminated
    game = LinkedList()
    for i in range(1, 6):
        game.add(i)
    print("Starting simulation...")
    game.simulate(3)

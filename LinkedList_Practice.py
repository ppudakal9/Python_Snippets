class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        curr = self.head
        while curr.next is not None:
            curr = curr.next #keep traversing the last element
        curr.next = new_node #set curr.next as new_node

    def length(self):
        total = 0
        curr = self.head
        while curr.next is not None:
            total += 1
            curr = curr.next

        return total

    def display(self):
        elems = []
        curr = self.head
        while curr.next is not None:
            curr = curr.next
            elems.append(curr.data)

        print(elems)

    def get(self, index):
        #check if index is within range
        if index >= self.length():
            print("ERROR : index out of range!")

        curr_index = 0
        curr = self.head
        while True:
            curr = curr.next
            if curr_index == index:
                return curr.data
            curr_index += 1

    def erase(self, index):
        #check if index is within range
        if index >= self.length():
            print("ERROR : index out of range!")

        curr_index = 0
        curr = self.head
        while True:
            #store last element
            last_node = curr
            curr = curr.next
            if curr_index == index:
                last_node.next = curr.next
                return
            curr_index+=1


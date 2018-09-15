from heapq import *

class implement_iterator:
    def __init__(self, l1, l2, l3):
        self.pq = []
        heapify(self.pq)
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def pq_using_heapq(self):

        i, j, k = 0, 0, 0
        #initialize priority queue with first smallest elements from each list
        heappush(self.pq, (l1[i], ('l1', i)))
        heappush(self.pq, (l2[j], ('l2', j)))
        heappush(self.pq, (l3[k], ('l3', k)))

    def getNextItem(self):
        if self.pq:
            elem, (list_name, index) = heappop(self.pq)
            print(elem)

            if list_name == 'l1':
                if len(l1) > index+1:
                    heappush(self.pq, (l1[index + 1], (list_name, index + 1)))
            elif list_name == 'l2':
                if len(l2) > index+1:
                    heappush(self.pq, (l2[index + 1], (list_name, index + 1)))
            elif list_name == 'l3':
                if len(l3) > index+1:
                    heappush(self.pq, (l3[index + 1], (list_name, index + 1)))
        else:
            print("Queue is empty! No more elements to iterate over!")
        print(self.pq)

l1 = [1,3,5,7]
l2 = [2,4,6]
l3 = [0]
obj = implement_iterator(l1, l2, l3)
obj.pq_using_heapq()
obj.getNextItem()
obj.getNextItem()
obj.getNextItem()
obj.getNextItem()
obj.getNextItem()
obj.getNextItem()
obj.getNextItem()
obj.getNextItem()
obj.getNextItem()


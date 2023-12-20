class Queue:  # first in first out --> Queue
    def __init__(self):
        self.items = ["one",
    "two",
    "three",
    "four",
    "five",
    "six"]

    def isEmpty(self):
        return len(self.items)  == 0 # Boolean --> True or False
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            print("queue is empty")
            return -1
        
    def size(self):
        return len(self.items)

    def front(self):
        if not self.isEmpty():
            return self.items[0]
        else:
            print("queue is empty")
            return -1
    def output(self):
        return self.items
    
q = Queue()

q.enqueue("pratyusha")
q.enqueue("kalyan")
q.enqueue("saigopi")
q.dequeue()
q.enqueue("saigopi")
q.enqueue("pratyusha")
q.dequeue()
q.dequeue()
q.dequeue()
print(q.output()) # printing self.items list
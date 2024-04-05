class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

queue = Queue()
print(queue.is_empty())

for i in range(5):
    queue.enqueue(i)

print(queue.size())

for i in range(5):
    queue.dequeue()

print(queue.size())
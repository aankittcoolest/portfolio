


## Implementing queues using python list

```py
class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        return False

    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of the queue."

    def dequeue(self):
        if self.isEmpty():
            return "There is not any element present in the queue."
        return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "There is not any element present in the queue."
        return self.items[0]

    def delete(self):
        self.items = None

customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.dequeue())
print(customQueue)
```
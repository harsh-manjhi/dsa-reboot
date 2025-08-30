class Queue :
    def __init__(self, size):
        self.size = size
        self.queue = [None] * self.size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1
    
    def is_full(self) :
        return (self.rear + 1) == self.size
    
    def Enqueue(self, value):
        if self.is_full() :
            print("Queue is Overflow.")
            return
        
        if self.is_empty() :
            self.front = 0

        self.rear += 1
        self.queue[self.rear] = value

        print("Enqueued :",value)

    def Dequeue(self) :
        if self.is_empty() :
            print("Queue is Underflow.")
            return None
        
        removed = self.queue[self.front]

        if self.front == self.rear :
            self.front = self.rear = -1
        else :
            self.front += 1

        print("Dequeued ")
        return removed
    
    def peek(self):
        if self.is_empty() :
            return None
        
        return self.queue[self.front]
    
    def display(self):
        if self.is_empty() :
            print("Queue is empty.")
            return
        
        i = self.front
        while i <= self.rear :
            print(self.queue[i],end=" ")
            i += 1 


q = Queue(5)

q.Enqueue(10)
q.Enqueue(20)
q.Enqueue(30)
q.Enqueue(40)
q.Enqueue(50)

q.display()

print(q.Dequeue())
print(q.Dequeue())

q.display()

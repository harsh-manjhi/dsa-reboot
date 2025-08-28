# Circular Queues 

class CircularQueue :
    def __init__(self,size):
        self.size = size
        self.front = -1 
        self.rear = -1
        self.queue = [None] * self.size

    def is_full(self):
        return  ((self.rear + 1) % self.size == self.front )
    
    def is_empty(self):
        return (self.front == -1)
    
    def enqueue(self,value):
        if self.is_full() :
            print("Queue Overflow.")
            return
        
        if self.is_empty() :    # First element
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        print(f"Enqueued : {value}")

    def dequeue(self):
        if self.is_empty() :
            print("Queue underflow.")
            return

        removed = self.queue[self.front]

        if self.front == self.rear :    # only one element
            self.front = self.rear = -1
        else :
            self.front = (self.front + 1) % self.size 
        print(f"Dequeued : {removed}")
        return removed

    def display(self):
        if self.is_empty() :
            print("Queue is Empty.")
            return
        
        i = self.front

        while True :
            print(self.queue[i],end= " ")
            if i == self.rear :
                break
            i = (i+1) % self.size
        print("\n")

    def peek(self):
        if self.is_empty() :
            print("Queue is Empty.")
            return 
        
        return self.queue[self.front]


q = CircularQueue(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

q.display()

print(q.dequeue())
print(q.dequeue())

q.display()

print("Peek() :",q.peek())
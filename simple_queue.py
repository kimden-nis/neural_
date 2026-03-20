my_array = [None] * 10
front = -1
rear = -1

def IsEmpty():
    if front == -1 and rear == -1:
        return True
    else:
        return False

def IsFull():
    if rear == len(my_array) - 1:
        return True
    else:
        return False
    
def Enqueue(value):
    global rear, front
    if IsFull():
        print("Queue is full")
    else:
        rear += 1
        my_array[rear] = value

def Dequeue():
    global front, rear
    if IsEmpty():
        print("Queue is empty")
    else:
        front += 1
        return my_array[front]
    
Enqueue(1)
Enqueue(2)
print(Dequeue())
print(Dequeue())
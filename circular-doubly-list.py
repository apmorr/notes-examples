#a cicular doubly linked list combines all three other types of lists; single linked list, doubly linked list, and circular linked lists
#we can traverse nodes foward and backward, as well as loop them on repeat

##gonna have to dumb this down alot
class Node:
    def __init__(self, data = None):
        self.data = data
        self.previous = self
        self.next = self
      
        
class DCLL:
    def __init__(self): ##create pointers and rename some variables
        self.head = None 
        self.count = 0
      
     
    def __repr__(self): ##this makes it easier to print out nodes (gets rid of the need for ".data")
        string = ""      ##remove it
          
        if(self.head == None):
            string += "Doubly Circular Linked List Empty"
            return string
          
        string += f"Doubly Circular Linked List:\n{self.head.data}"      
        temp = self.head.next
        while(temp != self.head):
            string += f" -> {temp.data}"
            temp = temp.next
        return string
     
    def append(self, data):##calls the insert method below and inputs in its own index
        self.insert(data, self.count)  
      
        return
     
    def insert(self, data, index): ##this is closer to the addPlayer() method i need
        if (index > self.count) | (index < 0):    ##delete the append method above and re work this so it doesnt need the index
            raise ValueError(f"Index out of range: {index}, size: {self.count}")
         
        if self.head == None:
            self.head = Node(data)
            self.count = 1
            return
         
        temp = self.head
        if(index == 0):
            temp = temp.previous
        else:
            for _ in range(index - 1):
                temp = temp.next
         
        temp.next.previous = Node(data)
        temp.next.previous.next, temp.next.previous.previous = temp.next, temp
        temp.next = temp.next.previous
        if(index == 0):
            self.head = self.head.previous
        self.count += 1
        return
     
    def remove(self, index): ##dont need
        if (index >= self.count) | (index < 0):
            raise ValueError(f"Index out of range: {index}, size: {self.count}")
             
        if self.count == 1:
            self.head = None
            self.count = 0
            return
         
        target = self.head
        for _ in range(index):
            target = target.next
             
        if target is self.head:
            self.head = self.head.next
             
        target.previous.next, target.next.previous = target.next, target.previous
        self.count -= 1
        
                 
    def index(self, data): ##dont need
        temp = self.head
        for i in range(self.count):
            if(temp.data == data):
                return i
            temp = temp.next
        return None
     
    def get(self, index): ##dont need
        if (index >= self.count) | (index < 0):
            raise ValueError(f"Index out of range: {index}, size: {self.count}")
             
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.data
     
    def size(self): #this is numberOfPlayer()
        return self.count
     
    def display(self): #this is to print it out
        print(self)
        
        
        
        
        

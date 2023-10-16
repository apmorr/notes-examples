#double Linked Lists can be traversed in either direction
#node1 <-> node2 <-> node3 <-> NULL
#mosrt of the code is the same as a standard Linked List but with a few changes

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None
  '''notice the addition of self.prev, this will allow us to move back and forth between nodes easier'''

class doublyLL:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        new_node.next = self.head
        while self.head != None:
            self.head = new_node
            self.prev = new_node.next
        
        
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        while self.head != None:
          self.head.prev = new_node
          self.head = new_node
      
    def listprint(self):
        print(self.prev)
        temp = self.head
        while (self.head != None):
            print(temp.data)
            last = temp
            temp = temp.next
  
  
DLL = doublyLL()
DLL.push(23)
DLL.push(901)
DLL.push(6)
DLL.listprint()

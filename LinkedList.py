#Linked Lists can only go in one direction
# node1 -> node2 -> node3 -> NULL

class Node: '''node class that stores a data point'''
  def __init__(self, data=None):
    self.data = data
    self.next = None
class LinkedList: '''class of a Linked List called LinkedList'''
  def __init__(self):
    self.head = node()

  def append(self, data): '''adds data point to the end of the linked list'''
    new_node = Node(data)
    current = self.head
    while current != None:
      current = current.next
    current.next = new_node
    ''' iterates through the items in the linked list usiong a while loop until it reaches an empty data point and fills it with given data parameter'''


  def length(self):
    current = self.head
    total = 0
    while current.next!=None:
      total += 1
      current = current.next
    return total
    '''return the length of the Linked List by counting through the nodes that arent equal to None'''

  def display(self):
    elem = []
    current_node = self.head
    while current_node.next != None:
      current_node = current_node.next
      elem.append(current_node.data)
      print elem
    '''Prints out a list made inside the method containing all the data nodes in the Linked List'''

  

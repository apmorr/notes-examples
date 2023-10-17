self.printTT()
        elems = []
        temp = None
        cur = None
        first = self._head
        last = self._tail
        a = self._head
        b = self._tail
        l = self._tail
        f = self._head
        count = 0


        for x in range(self._count):
            elems.append(last.data)
            last = last.prev
            count += 1
        for i in elems:
            a = a.next
            b = b.prev
            #print(elems)
            if i == self._tail.data:
                print('hi', i)
                temp = self._tail
                first = temp



            elif i == self._head.data:
                print('yo', i)
                cur = self._head
                last = cur

            else:
                print('hello', i)
                print(a.data, b.data)
                if a.data == 6:
                    self._head = l
                elif b.data == 1:
                    self._tail = f
                else:
                    print(a.data, '==', b.data)
                    


                self._head.next = a




            #print(self._head.data)

            #self._head = self._head.next
            #self._tail = self._tail.prev

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = self
        self.prev = self


class TurnTracker:
    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0

    def addPlayer(self, player):
        new_node = Node(player)
        # print(new_node.data)
        current = self._head
        if self._count == 0 and not self._head and not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            new_node.prev = self._tail
            self._tail = new_node
        self._count += 1

    def remove(self, data):  ##this works as intended
        cur = Node(data)
        temp = self._head
        # print(cur.data, temp.data, 'hey')
        if cur == temp:
            self.head = None
        temp = self.head
        # print(cur.data, temp.data, 'hi')

    def nextPlayer(self):  ##does not work yet

        temp = self._head
        current = None

        if (temp):
            current = temp.data
            self.addPlayer(temp.data)
            self._count -= 1
            self._prev = temp
            self._head = temp.next
        return current

 

    '''def skipNextPlayer(self):
        # print(self.L)
        # temp = self.L[len(self.L)-1]
        # print(temp)
        temp = self.L[0]
        self.L.pop(0)
        self.L.append(temp)
        print(self.L)'''

    def numberOfPlayers(self):
        return self._count


    def reverseTurnOrder(self):
        stack = []
        temp = self._head
        while temp:
            stack.append(temp.data)
            temp = temp.next

        # Add all the elements in the stack
        # in a sequence to the stack
        temp = self._head
        while temp:
            temp.data = stack.pop()
            temp = temp.next

        # Popped all the elements and the
        # added in the linked list,
        # in a reversed order.












        '''
        last = self._tail
        first = self._head
        
        elem = []
        self._head = last

        for x in range(self._count):

            elem.append(last.data)
            last = last.prev
            self._head.next = last
            print(elem)
        self.printTT()

        last = self._tail
   
        self.printTT()
        self._head = last
        self._tail = first
        last = last.prev
        first = first.next
        self.printTT()
        self._head.next = last
        self._tail.next = first
        last = last.prev
        first = first.next
        self.printTT()
        self._head.next = last
        self._tail.next = first
        last = last.prev
        first = first.next
        self.printTT()
        self._head.next = last
        self._tail.next = first
        last = last.prev
        first = first.next
        self.printTT()
        self._head.next = last
        self._tail.next = first
        last = last.prev
        first = first.next
        self.printTT()
        self._head.next = last
        self._tail.next = first
        self.printTT()

        print('----')
        '''





    def printTT(self):

        cur = self._head

        for x in range(self._count):
            print(cur.data, end=' ')
            cur = cur.next
        print()


tt = TurnTracker()
tt.addPlayer(1)
tt.addPlayer(2)
tt.addPlayer(3)
tt.addPlayer(4)
tt.addPlayer(5)
tt.addPlayer(6)

tt.reverseTurnOrder()
tt.printTT()

'''
print(tt.nextPlayer())
print(tt.nextPlayer())
print(tt.nextPlayer())
print(tt.nextPlayer())
print(tt.nextPlayer())
print(tt.nextPlayer())
tt.printTT()
print('-----')
tt.reverseTurnOrder()
print('-----')
tt.printTT()
print(tt.nextPlayer())
print(tt.nextPlayer())
print(tt.nextPlayer())
print(tt.nextPlayer())
print(tt.nextPlayer())
print(tt.nextPlayer())
'''

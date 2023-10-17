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

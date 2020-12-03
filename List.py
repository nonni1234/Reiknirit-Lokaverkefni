from Node import Node,Sivalningur,Keila,Kula



class List:
    def __init__(self):
        self.head = None

    def push(self,d):
        if not self.head:
            self.head = Node(d)
        else:
            temp = self.head
            self.head = Node(d)
            self.head.next = temp
            self.head.next.prev = self.head

    def append(self,d):
        if not self.head:
            self.head = Node(d)
        else:
            self.head.append(d)

    def staerstiSivalningur(self):
        staersti = Sivalningur(0,0)
        val = self.head.staerstiSivalningur(staersti)
        if val == staersti:
            return "Það er enginn Sívalningur í listanum"
        else:
            return val

    def staerstaKula(self):
        staersti = Kula(0)
        val = self.head.staerstaKula(staersti)
        if val == staersti:
            return "Það er engin Kula í listanum"
        else:
            return val
    def staerstaKeila(self):
        staersti = Keila(0, 0)
        val = self.head.staerstaKeila(staersti)
        if val == staersti:
            return "Það er engin Keila í listanum"
        else:
            return val


    def printList(self):
        if not self.head:
            print('Listi tómur')
        else:
            self.head.printList()

    def find(self,d):
        if not self.head:
            return False
        else:
            return self.head.find(d)

    def delete(self,d):
        if not self.find(d):
            return False
        elif self.head.data == d:
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
            return True
        else:
            if not self.head:
                return None
            else:
                return self.head.delete(d)
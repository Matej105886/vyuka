# from collections import deque
# list = deque()
# for i in range(1_000_000):
#     list.append(i)
# while len(list) != 0:
#     print(list.popleft())


class Node:
    def __init__(self, cislo):
        self.cislo = cislo
        self.node = None


class Deque2:
    def __init__(self):
        self.start = None
        self.maxlen = -1

    def append(self, cislo):
        # if self.maxlen == -1:
        #     pass
        if self.len() == self.maxlen and self.maxlen != -1:
            raise Exception("fronta je plna")
        node = Node(cislo)
        if self.start == None:
            self.start = node
            return
        current = self.start
        while current.node != None:
            current = current.node
        current.node = node

    def print(self):
        if self.start == None:
           return
        current = self.start
        print(current.cislo, end=" ")
        while current.node != None:
            current = current.node
            print(current.cislo, end= " ")
        print()



    def popleft(self):
        if self.start == None:
            raise Exception("fronta je prazdna")
        cislo = self.start.cislo
        self.start = self.start.node
        return cislo

    def clear(self):
        self.start = None


    def len(self):
        if self.start == None:
            return 0
        pocet = 1
        current = self.start
        while current.node != None:
            current = current.node
            pocet += 1
        return pocet

    def count(self, cislo):
        if self.start == None:
            return 0
        pocet = 0
        current = self.start
        while current.node != None:
            current = current.node
            if current.cislo == cislo:
                pocet += 1
        return pocet

    def popright(self):
        if self.start == None:
            raise Exception("fronta je prazdna")
        previous = None
        current = self.start
        while current.node != None:
            previous = current
            current = current.node
        if previous == None:
            self.start = None
        else:
            previous.node = None
        return current.cislo

    def remove(self, cislo):
        if self.start == None:
            return False
        previous = None
        current = self.start
        while current.node != None:
            previous = current
            current = current.node
            if cislo == current.cislo:
                previous.node = current.node
                return True
        return False

    def insert(self, i, cislo):
        if self.len() == self.maxlen and self.maxlen != -1:
            raise Exception("fronta je plna")
        if i > self.len():
            raise Exception("index je moc vysoky")
        if self.start == None:
            return

        index = 0
        previous = None
        current = self.start
        while current.node != None:
            previous = current
            current = current.node
            index += 1
            if i == index:
                previous.node = Node(cislo)
                previous.node.node = current
                return
        current.node = Node(cislo)





def len(fronta):
    if fronta.start == None:
        return 0
    pocet = 1
    current = fronta.start
    while current.node != None:
        current = current.node
        pocet += 1
    return pocet

def len2(fronta):
    return fronta.len()


deque = Deque2()
deque.append(1000)
print(len(deque))
deque.append(2000)
print(len2(deque))
# print(deque.popright())
# print(deque.popright())
# print(deque.popright())
# print(deque.popright())
# print(deque.popleft())
# print(deque.popleft())
# print(deque.popleft())
deque.append(3000)
deque.append(3000)
# print(deque.len())
print(deque.count(1110000))
print(deque.count(3000))
# deque.clear()
deque.print()
deque.append(5000)
deque.print()
print(deque.remove(3000))
deque.print()
deque.insert(2, 7000)
deque.print()
#deque.maxlen = 5
deque.insert(5, 6000)
deque.print()

# print(deque.len())



#deque.print()

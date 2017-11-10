from Person import Person
from Node import Node

class ListDE():

    def __init__(self):
        self.head: Node = None

    def __len__(self):
        length: int = 0
        if(self.isEmpty()):
            return length

        temp: Node = self.head
        while(temp != None):
            length += 1
            temp = temp.getNext()
        return length

    def isEmpty(self) -> bool:
        if(self.head == None):
            return True
        return False

    def append(self, object: object):

        if(self.head == None):
            self.head = Node(object)
            return

        temp: Node = self.head
        while (temp.getNext() != None):
            temp = temp.getNext()
        temp.setNext(Node(object))
        temp.getNext().setPrevious(temp)

    def remove(self, object: object):

        if(self.head == None):
            return

        temp: Node = self.head

        if(temp.record.__eq__(object)):
            self.head = temp.getNext()
            return

        while(temp.getNext() != None):
            if(temp.getNext() != None):
                if(temp.getNext().record.__eq__(object)):
                    if(temp.getNext().haveNext()):
                        temp.getNext().getNext().setPrevious(temp)
                        temp.setNext(temp.getNext().getNext())
                        return
                    temp.setNext(None)
                    return

            temp = temp.getNext()

    def clear(self):
        self.head = None

    def insert(self, index: object, object: object):

        if(index is None or object is None):
            return

        newObject: Node = Node(object)
        temp: Node = self.head
        if(temp == None):
            self.head = Node(index)
            return
        while((temp.getRecord() != index) and temp.haveNext()):
            temp = temp.getNext()
        if(temp.getRecord().__eq__(index)):
            newObject.setNext(temp.getNext())
            temp.setNext(newObject)
            temp.getNext().setPrevious(temp)

    def getObject(self, object: object) -> object:

        if(self.head == None):
            return None

        temp: Node = self.head
        while(temp != None):
            if(temp.getRecord().__eq__(object)):
                return temp.record
            temp = temp.getNext()
        return None

    def getObjectsList(self) -> []:

        responseList: [] = []

        if(self.head == None):
            return responseList

        temp: Node = self.head

        while(temp != None):
            responseList.append(temp.record)
            temp = temp.getNext()
        return responseList
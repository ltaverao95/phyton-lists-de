from Person import Person

class Node():

    def __init__(self, object: object):
        self.record: object = object
        self.next: Node = None
        self.previous: Node = None

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next

    def getPrevious(self):
        return self.previous

    def setPrevious(self, previous):
        self.previous = previous

    def haveNext(self):
        return self.next != None

    def havePrevious(self):
        return self.previous != None

    def setRecord(self, object: object):
        self.record = object

    def getRecord(self):
        return self.record
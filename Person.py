import json

class Person():

    def __init__(self, name, age, genre, telephone, email):
        self.name=name
        self.age=age
        self.genre=genre
        self.telephone=telephone
        self.email=email

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
from ListDE import ListDE
from Person import Person

listDE: ListDE = ListDE()

#Aditions at the end
listDE.append(Person("pepito", 27, "m", 34870, "sf"))
listDE.append(Person("pepito2", 27, "m", 34870, "sf"))
listDE.append(Person("pepito3", 27, "m", 34870, "sf"))
listDE.append(Person("pepito4", 27, "m", 34870, "sf"))

#Aditions in position
listDE.insert(Person("pepito4", 27, "m", 34870, "sf"), Person("pepito5", 27, "m", 34870, "sf"))

#Get by person
print(listDE.getObject(Person("pepito4", 27, "m", 34870, "sf")).__dict__)

#Remove by person
listDE.remove(Person("pepito5", 27, "m", 34870, "sf"))

#List length
print(listDE.__len__())

objectsList: [] = listDE.getObjectsList()
if(listDE.__len__() > 0):
    for object in objectsList:
        print(object.__dict__)
else:
    print("No records found")
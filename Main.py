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

#Other types

print("\n")

listDEString: ListDE = ListDE()

#Aditions at the end
listDEString.append("pepito")
listDEString.append("pepito2")
listDEString.append("pepito3")
listDEString.append("pepito4")

#Aditions in position
listDEString.insert("pepito3", "pepito5")

#Get by person
print(listDEString.getObject("pepito5"))

#Remove by person
listDEString.remove("pepito5")

#List length
print(listDEString.__len__())

objectsList: [] = listDEString.getObjectsList()
if(listDEString.__len__() > 0):
    for object in objectsList:
        print(object)
else:
    print("No records found")

class Teacher:
    def skills (self):
        print("Teacher teachs students...!")

class Engineer :
    def display(self):
        print("Enginer builds machine...!")

class Person(Teacher,Engineer):
    def details(self):
        print("A person have multiple roles...!")

obj1 = Teacher()
obj1.skills()

obj2 = Engineer()
obj2.display()

obj3 = Person()
obj3.details()

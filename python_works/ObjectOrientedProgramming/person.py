"""
Person

height
weight
name
age

set_person(self,name,height,weight)

walk()
run()
eat()
sleep()

"""

class Person:

    name:str

    height:int

    weight:int

    age:int


    def set_person(self,name,height,weight,age):

        self.name=name

        self.height=height

        self.weight=weight

        self.age=age

    def walk(self):

        print(self.name,"is walking")

    def run(self):

        print(self.name,"is running")

    def eat(self):

        print(self.name,"is eating")



person_instance1=Person()

person_instance1.set_person("dhibin",165,77,21)


person_instance2=Person()

person_instance2.set_person("renjith",166,52,20)

person_instance3=Person()

person_instance3.set_person("kalpak",157,53,20)

person_instance3.eat()

person_instance2.run()



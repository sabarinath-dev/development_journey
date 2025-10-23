# single inheritance is a type of inheritance in which a derivative class
# can access and inherit all the properities of its parent class.


class parentclass():
    def parent(self):
        print("parent")

class childclass(parentclass):
    def child(self):
        print("child")

obj1 = parentclass()
obj1.parent()

obj2 = childclass()
obj2.parent()
obj2.child()
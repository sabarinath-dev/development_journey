# Only one parent class and multiple child classes


class A:
    def method_A(self):
        print("A")

class B(A):
    def method_B(self):
        print("B")

class C(A):
    def method_C(self):
        print("C")

class D(A):
    def method_D(self):
        print("D")

obj1 = A()
obj1.method_A()

obj2 = B()
obj2.method_A()
obj2.method_B()





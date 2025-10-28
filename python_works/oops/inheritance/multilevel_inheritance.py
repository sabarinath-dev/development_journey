

# a chain of classes is called multilevel inheritance

class A:
    def function_A(self):
        print("Inside A")


class B(A):
    def function_B(self):
        print("Inside B")

class C(B):
    def function_C(self):
        print("Inside C")

obj1 = A()
obj1.function_A()

obj2 = B()
obj2.function_B()
obj2.function_A()

obj3 = C()
obj3.function_C()
obj3.function_B()
obj3.function_A()



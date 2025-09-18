

"""

dir(class name)used to list all the methods of the specified class.

class list

    def append() is used to  add a object at the end of the list.
    def insert(index value, object) add object at the specified index position.
    def pop(self,index= -1(by defualt the index value is -1)) remove and return item at the specified  index
    def index(object) returns the value of index on the first occurance.
    def count(self,object) return number of occurances of the object.
    def reverse() reverse the current list objects.
    def copy() used to shallow copy(outer object) a list.
    def sort(self, reverse=false) used to sort list objects.
    def extend(self,iterable(list to be added)) extend list by appending elemnts from the iterable.
    def remove(object) used to remove the first occurance of the object.

"""

"""
1) append()

list = [" " , " "]

list.append(" ")

append() is used to  add a object at the end of the list.


"""


# colors = ["red" , "blue" , "green"]

# colors.append("black")

# print(colors)

#output = ['red', 'blue', 'green' ,"black"]


"""
2) insert() add object at the specified index position.

list = [""]
list.insert(index value, object)

"""
# colors = ["red" , "blue" , "green"]

# colors.insert(2,"purple")

# print(colors)

#output = ['red', 'blue', 'purple', 'green']


"""
3) pop() remove and return item at the specified  index

list = [""]
list.pop(self,index= -1(by defualt the index value is -1))

"""

# colors = ["red" , "blue" , "green"]

# colors.pop(-2)

# print(colors)

# output = ['red', 'green']


"""
4) index() returns the value of index on the first occurance.

list = [""]
pos = list.index(object)

"""

# colors = ["red" , "blue" , "green" , "red" , "blue" , "green"]

# pos = colors.index("blue")

# print(pos)

# output = 1


"""
5) count() return number of occurances of the object

list = [""]
freq = list.count(self,object)

"""

# colors = ["red" , "blue" , "green" , "red" , "blue" , "green"]

# freq = colors.count("blue")

# print(freq)

# output = 2

"""
5) reverse() reverse the current list.

list = [""]
list.reverse()

"""

# colors = ["red" , "blue" , "green" , "red" , "blue" , "green"]

# colors.reverse()

# print(colors)


"""
6) copy() used to copy a list object.

list = [""]
list_copy = list.copy()

"""
# colors = ["red" , "blue" , "green" , "red" , "blue" , "green"]

# colors_copy = colors.copy()

# colors_copy[0] = "white"

# print(colors)
# print(colors_copy)

# output = ['red', 'blue', 'green', 'red', 'blue', 'green']
#          ['white', 'blue', 'green', 'red', 'blue', 'green']


"""
7) sort(self, reverse=false) used to sort list objects.

list = [""]
list.sort(reverse=false/True)

"""

# numbers = [20000 , 100 , 5 , 24500 , 5000 , 300 , 200000]

# numbers.sort(reverse=True)

# print(numbers)

# output = [200000, 24500, 20000, 5000, 300, 100, 5]


"""
8) extend(self,iterable(list to be added)) extend list by appending elemnts from the iterable.

list1 = [""]
list2 = [""]
list2.extend(list1)

"""


# arr1 = [20000 , 100 , 5 , 24500 , 5000 , 300 , 200000]
# arr2 = [1,2,3,4,5,6,7,8]

# arr2.extend(arr1)

# print(arr2)

#output = [1, 2, 3, 4, 5, 6, 7, 8, 20000, 100, 5, 24500, 5000, 300, 200000]



"""
9) remove(self,object) used to remove the first occurance of the object.

list = [""]
list.remove(object name)

"""

# colors = ["red" , "blue" , "green" , "red" , "blue" , "green"]

# colors.remove("green")

# print(colors)

# output = ['red', 'blue', 'red', 'blue', 'green']

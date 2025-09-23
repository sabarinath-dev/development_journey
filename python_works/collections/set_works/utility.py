
# class set
# define {value1 , value2 , ..... , n} or set{}
# unordered - indexing is not supported.
# mutable
# duplicates not allowed. Values will be unique.
# methods

"""
class set

    
    def union(self, object) - combine all the elements of two sets.
    
    def intersection(self,set_obj) - return the common objects in two sets.
    
    def difference(self,set_object) - remove the elements that are present in set 1 from set 2.
    
    def issubset(self,set_object) the larger, overall collection that contains all the items of another, smaller collection
    
    def issuperset(self,set_object) the smaller, collection that contains some of the items of another, larger collection.
    
    def symmetric_difference - set of objects that are in either A or B but not in both.
    
    def remove(self,object) -remove an object from the set.
    
    def isdisjoint - there will be no common objects in both sets.(intersection will be none)

    def update(self,object) - to update a set with another set.

    def add
    
    def clear
    
    def copy
    
    def difference_update
    
    def discard
    
    def intersection_update
    
    def pop

    def symmetric_difference_update


"""

set1 = {10,20,30,40,50,60}
set2 = {100,10,200,20,300,30,400,40}

union_set = set1.union(set2)    #combine both sets.
intersection_set = set1.intersection(set2) #return the common objects present in both sets.
difference_set = set2.difference(set1) #remove the objects that are present in set1 from set2
symme_difference_set = set1.difference(set2) #remove the objects that are present in set1 from set2 but not common to both

print("Union of set1 and set2:", union_set)
print("Intersection of set1 and set2:", intersection_set)
print("Difference of set2 and set1:", difference_set)
print(set2.issuperset(set1))
print(set1.issubset(set2))
print(set1.isdisjoint(set2))
print("Symmetric Difference of set2 and set1:", symme_difference_set)

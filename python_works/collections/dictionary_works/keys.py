"""
def key(self)       # return all keys
def values(self)    # return all value
def item            # return key and values
def pop(self,key)   # remove that key value pair
def get(self,key)   # return value using key
"""

course={
    "name":"python django",
    "fee":3990,
    "duration":"7 months",
    "tutor":"sajay"
}
all_keys=course.keys()

for k in all_keys:
    print(k)
    
all_values=course.values()
print()

for v in all_values:
    print(v)
    
course.pop("fee")
print(course)

print(course.get("name"))



from copy import deepcopy

basith=[
    ["tea","puttu"],#0
    ["biriyani","limejuice"],#1
    ["tea"],#2
    ["friedrice"]#3
]

# deep copy creates new object and recursivly copies all inner object
renjith=deepcopy(basith) #deepcopy


renjith[3][0]="porotta"

print(basith)
print(renjith)
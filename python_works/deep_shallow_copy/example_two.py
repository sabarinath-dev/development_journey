
from copy import copy

suma_fvt_colors=["black","red","pink"]

# shallow copy creates a new object but doesnot copy the nested objects
mariyam_fvt_colors=copy(suma_fvt_colors)#shallowcopy

mariyam_fvt_colors[0]="white"

print(suma_fvt_colors)
print(mariyam_fvt_colors)
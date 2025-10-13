words = ["listen","act","post","earth","silent","cat","stop","heart"]

#Exp/op {"listen":"silent","act":"cat","post":"stop","earth":"heart"}

#Real{'eilnst': ['listen', 'silent'], 'act': ['act', 'cat'], 'opst': ['post', 'stop'], 'aehrt': ['earth', 'heart']}


anagaram_dict={}

for w in words:

    all_keys=anagaram_dict.keys()

    if len(all_keys) ==0:

        anagaram_dict[w]=[]

    else:

        for k in all_keys:

            if "".join(sorted(k))=="".join(sorted(w)):

                anagaram_dict[k].append(w)

    print(anagaram_dict)
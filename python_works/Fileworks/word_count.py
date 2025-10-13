

file_path="C:\\Users\\Luminar\\Desktop\\development_journey_july_2k25\\python_works\\Fileworks\\news.txt"


lst=[100,200,300]

index=int(input("enter index"))


fr=open(file_path,"r")#error

all_words=[]

for line in fr:

    #line=Discipline is one of the most important qualities a person can develop in life.\n

    words=line.rstrip("\n").lower().split(" ")
    # words=['it', 'means', 'having', 'self-control,', 'following', 'rules,', '']

    for w in words:
        all_words.append(w)

word_count={w:all_words.count(w) for w in all_words}

print(word_count)


# read,write,append
# open()





# wakeup at 7:30am
# daily routien 7:45
# leave hostel by bike at 8:05
# 8:30 fuel empty => by bus,uber,online
# attend session at 9:30
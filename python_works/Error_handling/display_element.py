

lst=[100,10,20,30,40,50,60]
#     0   1  2  3   4  5  6

index1=int(input("enter index to display element"))

index2=int(input("enter index to display element"))

try:
    element1=lst[index1]
    element2=lst[index2]

    try:
        result=element1/element2
        print(result)

    except ZeroDivisionError as ze:
        print(ze)

except IndexError as ie:
    print(ie)


finally:
    # clean up processing
    print("write a data to file.....")

    print("database operation......")

    print("program completed....")
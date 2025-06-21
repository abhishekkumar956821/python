def convert2number(arr):
    number=0

    for item in arr:
        number=(number*10)+item

    return number

def convert2array(number,length):
    arr=list(str(number))

    if len(arr) < length + 1:

        for x in range (len(arr),length+1):
            arr.insert(0,"0")

    return arr

n=int(input())
arr1=[int(x) for x in input().split()]
m=int(input())
arr2=[int(x) for x in input().split()]
number1=convert2number(arr1)
number2=convert2number(arr2)
biggerArrSize = 0

if len(arr1) >= len(arr2):
    biggerArrSize = len(arr1)

else:
    biggerArrSize = len(arr2)

final_arr=convert2array(number1+number2,biggerArrSize)
for x in final_arr:
    print(x,end=" ")

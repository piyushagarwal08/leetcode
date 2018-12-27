#search insert position
print("don't repeat values:")
length = int(input("enter length of array"))
arr = []
for i in range(0,length):
    element = input("insert elements for array")
    arr.append(element)
arr.sort()
target = input("enter the value to search in array")
i = 0
while (i<length):
    if (arr[i] == target):
        print(i)
        break
    if(arr[i] > target):
        print(i)
        break
    i = i+1

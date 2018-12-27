#REMOVE ELEMENT
num_length = input("enter the length of array")
nums = []
for i in range(0,int(num_length)):
    element = input("enter element: ")
    nums.append(element)
print(nums)
val = input("enter a value")
i = 0
while(i<len(nums)):
    if(nums[i] == val):
        nums.remove(nums[i])
        i = i - 1
    i = i+ 1
print(len(nums))        


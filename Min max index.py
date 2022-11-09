arrSize = int(input("Enter an array size to evaluate indexes:"))
i = 0
maxIndex = 0
minIndex = 0
nums = []


while i < arrSize:
    nums.append(int(input(f"Type number {i+1}: ")))
    i += 1

i = 0

for i in range(0,arrSize-1,1):
    if nums[maxIndex]<nums[i+1]:
        maxIndex = i + 1
    if nums[minIndex]>nums[i+1]:
        minIndex = i + 1


print("Индекс максимального элемента:", maxIndex, "\nИндекс минимального элемента: ", minIndex)


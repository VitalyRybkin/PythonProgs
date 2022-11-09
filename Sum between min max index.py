arrSize = int(input("Enter an array size to be evaluated: "))
i = 0
maxIndex = 0
minIndex = 0
nums = []
sum = 0


while i < arrSize:
    nums.append(int(input(f"Type number {i+1}: ")))
    i += 1

i = 0

for i in range(0,arrSize-1,1):
    if nums[maxIndex]<nums[i+1]:
        maxIndex = i + 1
    if nums[minIndex]>nums[i+1]:
        minIndex = i + 1

if maxIndex > minIndex:
    while minIndex <= maxIndex:
        sum += nums[minIndex]
        minIndex += 1
else:
    while maxIndex <= minIndex:
        sum += nums[maxIndex]
        maxIndex += 1

print("That's what we've got for you: ", sum)


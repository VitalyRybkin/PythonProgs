from array import *
import random

arrSize = int(input("Enter an array size:"))
firstMaxInd = 0
secondMaxInd = 0
index = 0
nums = array('i')

#nums = list(map(int, input().split()))

for index in range(0, arrSize, 1):
    # nums.append(int(input(f"Enter num {index +1}:")))
    nums.append(random.randint(0, 100))

index = 0

if nums[0] > nums[1]:
    secondMaxInd = 1

while index < len(nums) - 1:
    if nums[firstMaxInd] < nums[index + 1]:
        secondMaxInd = firstMaxInd
        firstMaxInd = index + 1
    else:
        if nums[secondMaxInd] < nums[index + 1]:
            secondMaxInd = index + 1
    index += 1

print(nums, nums[firstMaxInd], nums[secondMaxInd], sep=':', end="\n that's all folks")

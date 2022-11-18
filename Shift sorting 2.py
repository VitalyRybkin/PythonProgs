from array import *
import random
import time

start = time.time()

nums = array('i')
maxIndex = 0
curIndex = 0
buffer = 0

#arrSize = int(input("Enter an array size:"))
arrSize = 10

#while curIndex < arrSize:
#    nums.append(int(input(f'Enter number {curIndex + 1}:')))
#    curIndex += 1

for curIndex in range(0, arrSize, 1):
    # nums.append(int(input(f"Enter num {index +1}:")))
    nums.append(random.randint(0, 100))

curIndex = 0

while arrSize > 1:
    for curIndex in range(arrSize):
        if nums[curIndex] > nums[maxIndex]:
            maxIndex = curIndex
        curIndex += 1

    print(maxIndex, arrSize)
    print(nums)
    # buffer = nums[arrSize-1]
    # nums[arrSize-1] = nums[maxIndex]
    # nums[maxIndex] = buffer
    nums[arrSize - 1], nums[maxIndex] = nums[maxIndex], nums[arrSize - 1]
    arrSize -= 1
    maxIndex = 0
    print(nums)

end = time.time()

print("Execution time of the program is- ", end-start)

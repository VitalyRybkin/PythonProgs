from array import *
import random
import time

start = time.time()

curIndex = 0
moveIndex = 0
maxIndex = 0
buffer = 0
nums = array('i')

#arrSize = int(input("Enter an array size:"))
arrSize = 1000


#for curIndex in range(0, arrSize, 1):
#    nums.append(random.randint(1,100))

while curIndex < arrSize:
    nums.append(random.randint(1, 100))
    curIndex += 1

curIndex = 0

while arrSize > 1:
    for curIndex in range(arrSize):
        if nums[curIndex] > nums[maxIndex]:
            maxIndex = curIndex
        curIndex += 1

    print(maxIndex, arrSize)
    print(nums)

    buffer = nums[maxIndex]
    del nums[maxIndex]
    nums.insert(arrSize-1, buffer)

    maxIndex = 0
    arrSize -= 1


print(maxIndex)
print(nums)

end = time.time()

print("Execution time of the program is- ", end-start)

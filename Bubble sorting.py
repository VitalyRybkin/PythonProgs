import random
from array import *
import time

start = time.time()

#arrSize = int(input("Enter an array size:"))
arrSize = 1000

ind = 0
nums = array('i')
prev_arr = array('i')
buffer = 0

while ind < arrSize:
    #nums.append(int(input(f"Type number {ind+1}: ")))
    nums.append(random.randint(1, 100))
    ind += 1

ind = 0

prev_arr = nums.__copy__()

while arrSize > 1:


    for ind in range(len(nums)-1):
        if nums[ind] > nums[ind + 1]:
            buffer = nums[ind]
            nums[ind] = nums[ind + 1]
            nums[ind + 1] = buffer

    print(ind, arrSize)
    print(nums)

    ind += 1
    arrSize -= 1


print("You've entered:", prev_arr, "\nWe've sorted:", nums)

end = time.time()

print("Execution time of the program is- ", end-start)

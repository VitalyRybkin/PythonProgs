import random
from array import *
import time


def main():
    start = time.time()
    nums = array('i')

# Creating an array
    MakeArray(nums)
    prev_arr = nums.__copy__()
    print("Old array", end=": ")
    for i in range(0, len(prev_arr), 1): print(prev_arr[i], end=' ')
# Sorting an array
    Sorting(nums)
    print("\nNew array", end=": ")
    for i in range(0, len(nums), 1): print(nums[i], end=' ')
# Program execution time
    end = time.time()
    print(f"\n\nExecution program time is: {end - start:.6f}")


def MakeArray(nums):
    # arrSize = int(input("Enter an array size:"))
    arr_size = 10
    ind = 0
    while ind < arr_size:
        # nums.append(int(input(f"Type number {ind+1}: ")))
        nums.append(random.randint(1, 100))
        ind += 1


def Sorting(nums):
    ind = 0
    arr_size = len(nums)
    while arr_size > 1:
        for ind in range(len(nums)-1):
            if nums[ind] > nums[ind + 1]: nums[ind], nums[ind + 1] = nums[ind + 1], nums[ind]
        ind += 1
        arr_size -= 1


main()

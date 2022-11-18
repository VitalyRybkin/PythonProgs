from array import *
import time
import random


def main():
    start = time.time()
# Creating an array
    nums = array('i')
    MakeArray(nums)
    print("Old array", end=": ")
    for i in range(0, len(nums), 1): print(nums[i], end=' ')
# Sorting an array
    Sorting(nums)
    print("\nNew array", end=": ")
    for i in range(0, len(nums), 1): print(nums[i], end=' ')
# Program execution time
    end = time.time()
    print(f"\n\nExecution program time is: {end - start:.6f}")


def MakeArray(nums):
    index = 0
    # arrSize = int(input('Enter an array size:'))
    arr_size = 6
    # nums = [5, 4, 11, 0, 1, 10]
    while index < arr_size:
        nums.append(random.randint(1, 100))
        index += 1


def Sorting(nums):
    index = 0
    while index < len(nums) - 1:
        if nums[index] > nums[index + 1]:
            change_index = index + 1
            for check in range(0, change_index, 1):
                if nums[check] > nums[change_index]:
                    nums.insert(check, nums[change_index])
                    del nums[change_index + 1]
                    break
        index += 1


main()

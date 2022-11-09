arrSize = int(input("Enter an array size to be evaluated:"))
i = 0
ave = 0
sum = 0
nums = []

while i < arrSize:
    nums.append(int(input(f"Type number {i+1}: ")))
    sum = sum + nums[i]
    i += 1

ave = sum / arrSize

print("We glad to introduce your arithmetic mean:", ave)


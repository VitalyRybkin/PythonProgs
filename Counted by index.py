quantity = int(input("Type the quantity of numbers to count:"))
ave = 0
index = 0
ave = 0
nums = []
sum = 0

while index < quantity:
    nums.append(int(input(f"Type number {index+1}: ")))
    index += 1

index = 0

while index < quantity:
    if index%2==0:
        print(nums[index])
        sum = sum + nums[index]
        index += 1
    else:
        index += 1

print(sum, nums)
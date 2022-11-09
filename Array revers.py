arrSize = int(input("Enter an array size to be reversed:"))
buffer = 0
forward_ind = 0
backward_ind = arrSize - 1
nums = []

while forward_ind < arrSize:
    nums.append(int(input(f"Type number {forward_ind+1}: ")))
    forward_ind += 1

forward_ind = 0
prev_nums = list (nums)

while forward_ind <= backward_ind:
    buffer = nums[forward_ind]
    nums[forward_ind] = nums[backward_ind]
    nums[backward_ind] = buffer
    forward_ind = forward_ind + 1
    backward_ind = backward_ind - 1

print("You have entered an array:", prev_nums, "\n... but we've reversed it:", nums)


safe = 0

def is_safe(nums):
    safe = True
    toggle = nums[0] > nums[1]
    for i in range(len(nums) - 1):
        if abs(nums[i]-nums[i+1]) <= 3 and abs(nums[i]-nums[i+1]) >= 1:
            if nums[i] > nums[i+1] and not toggle:
                safe = False
            if nums[i] < nums[i+1] and toggle:
                safe = False
        else:
            safe = False
    return safe

f = open("3.in")
for line in f.readlines():
    nums = list(map(int, line.split()))
    proven_safe = False
    if is_safe(nums):
        proven_safe = True
        safe += 1
    else:
        for possibility in range(len(nums)):
            nums_clone = nums.copy()
            del nums_clone[possibility]
            if is_safe(nums_clone):
                safe += 1
                break
print(safe)
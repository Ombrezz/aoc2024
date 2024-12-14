safe = 0
f = open("3.in")
for line in f.readlines():
    nums = list(map(int, line.split()))
    toggle = nums[0] > nums[1]
    unsafe = False
    for i in range(len(nums) - 1):
        if abs(nums[i]-nums[i+1]) <= 3 and abs(nums[i]-nums[i+1]) >= 1:
            if nums[i] > nums[i+1] and not toggle:
                unsafe = True
            if nums[i] < nums[i+1] and toggle:
                unsafe = True
        else:
            unsafe = True
    if not unsafe:
        safe += 1
        print("Safe")
    else:
        print("Unsafe")
print(safe)
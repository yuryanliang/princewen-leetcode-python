def f(nums, val):
    p = 0
    for i in range(0, len(nums)):
        k = nums[i]
        if k != val:
            nums[p] = k
            p += 1
    return nums[:p]


def f_1(nums, val):
    p = 0
    i = 0
    while i < len(nums):
        k = nums[i]
        if k != val:
            nums[p] = k
            p += 1
        i += 1
    return nums[:p]


nums = [1, 2, 2, 3, 4]
print(f_1(nums, 2))
nums = [1, 2, 2, 3, 4]

print(f(nums, 2))

1 == 1

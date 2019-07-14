# https://www.zhihu.com/question/36132386

# 即使区间为空、答案不存在、有重复元素、搜索开/闭的上/下界也同样适用：

# 返回[first, last)内第一个 >= value的值的位置
# 即从在 nums中的一个区间 [value, end of nums] 的 lower bound index.
def lower_bound(nums, target):  # target = 5
    if len(nums) == 0:
        return -1
    left = 0  # left = 0
    right = len(nums) - 1  # right = 5

    while left < right:
        mid = (left + right) // 2  # mid = 2
        if nums[mid] < target:
            left += 1
        else:
            right = mid
    return left if nums[left] == target else -1


# 返回[first, last)内最后一个不小于value的值的位置
def upper_bound(nums, target):  # target = 3
    if len(nums) == 0:
        return -1

    left = 0  # left = 3
    right = len(nums) - 1  # right = 3

    while left < right:
        mid = (left + right + 1) // 2  # mid = 4
        mid_val = nums[mid]  # mid_val = 4
        if mid_val > target:
            right = mid - 1
        else:
            left = mid

    if nums[left] == target:
        return left
    else:
        return -1


def main_lower():
    nums = [1, 3, 3, 3, 4, 5]
    for i in nums:
        ind = lower_bound(nums, i)
        print(ind)

    print(lower_bound(nums, 9))
    print(upper_bound([1], 1))

    print(lower_bound([], 9))


def main_upper():
    nums = [1, 3, 3, 3, 4, 5]
    for i in nums:
        ind = upper_bound(nums, i)
        print(ind)

    print(upper_bound(nums, 9))
    print(upper_bound([1], 1))
    print(upper_bound([], 9))


if __name__ == '__main__':
    main_upper()
    main_lower()

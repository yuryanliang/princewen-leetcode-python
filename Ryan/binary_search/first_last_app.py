
# http://www.codebelief.com/article/2018/04/completely-understand-binary-search-and-its-boundary-cases/



# find the first in the repeated
def bi_search_first_app(nums,target):
    left = 0
    right = len(nums) - 1
    # 这里说一下，为什么 while 里的条件是 <，而不是 <= 。
    # 一方面是我们想在循环外部判断最终的 left 位置是否是目标值，
    # 另一方面是如果循环条件允许 left = right， 那么最后 mid = left = right，
    # 如果该处正好是目标值，那么 right 将始终等于 mid，不会再左移，就会陷入死循环。
    while left < right:
        mid = left + (right - left) // 2
        mid_val = nums[mid]
        if mid_val < target:
            left = mid + 1 # mid is lean to left. So if left = mid, then left will always the same. infinite loop
        else:
            right = mid
            # 既然要寻找左边界，搜索范围就需要从右边开始，不断往左边收缩，也就是说即使我们找到了nums[mid] == target,
            # 这个mid的位置也不一定就是最左侧的那个边界，我们还是要向左侧查找，所以我们在nums[
            #     mid]
            # 偏大或者nums[mid]
            # 就等于目标值的时候，继续收缩右边界，算法模板如下
    if nums[left] == target:
        return left
    else:
        return -1

#find the last in the repeated
def bi_search_last_app(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        # in case left + right over int range.
        mid = left + (right - left+1) // 2

        mid_val = nums[mid]
        if nums[mid] > target:
            right = mid-1 #mid is lean to right. So if right = mid, then right will always the same. infinite loop
        else:
            left = mid
    if nums[left] ==  target:
        return left
    else:
        return -1


def main():
    # nums = [1, 2, 3, 4, 5, 6]
    # for i in nums:
    #     ind = bi_search_1(nums, i)
    #     print(ind)

    nums_first_app = [1, 2, 3, 3, 3, 5]

    # ind = bi_search_first_app(nums_first_app, 3)
    ind = bi_search_last_app(nums_first_app, 3)
    print(ind)
# main()






# in a desc order
def first_app(nums, target): # target = 3
    left = 0 # left = 1
    right = len(nums) - 1 # right = 1

    while left < right:
        mid = left + (right - left) // 2 # mid = 0
        val_mid = nums[mid] # val_mid = 5
        if val_mid > target:
            left = mid + 1
        else:
            right = mid #
    if nums[left] == target: #nums[left] = 3
        return left
    else:
        return -1

def last_app(nums, target): # target = 3
    left = 0 # left = 3
    right = len(nums) - 1 # right = 3

    while left < right:
        mid = left + (right - left + 1) // 2 # mid = 4
        val_mid = nums[mid] # val_mid = 2
        if val_mid < target:
            right = mid - 1
        else:
            left = mid
    if nums[left] == target:
        return left
    else:
        return -1

def main_desc():
    nums= [5, 3, 3, 3, 2, 1]
    print(first_app(nums, 3))
    print(last_app(nums,3))

main_desc()

def bi_search_1(nums, target):
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def bi_search_2(nums, target): # target = 3
    left = 0 # left = 2
    right = len(nums) - 1 # right = 2

    while left < right:
        mid = left + (right - left) // 2 # mid = 1
        val_mid = nums[mid] # val_mid = 2

        if val_mid < target:
            left = mid + 1
        else:
            right = mid
    if nums[left] == target:
        return left
    else:
        return -1

# for desc
def bi_search_3(nums, target): # target = 4
    left = 0 # left = 2
    right = len(nums) - 1 # right = 2

    while left < right:
        mid = left + (right - left + 1) // 2 # mid = 3
        val_mid = nums[mid] # val_mid = 3

        if val_mid < target:
            right = mid -1
        else:
            left = mid
    if nums[left] == target:
        return left
    else:
        return left



def main():
    nums = [1, 2, 3, 4, 5, 6]
    for i in nums:
        ind = bi_search_2(nums, i)
        # print(ind)


    nums_3 = [7, 6, 5, 3, 2, 1]
    print(bi_search_3(nums_3, 4))


main()

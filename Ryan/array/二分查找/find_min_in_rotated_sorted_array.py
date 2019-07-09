def findMin( nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1
    return nums[left]

nums=[3,4,1,2]
print(findMin(nums))


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def binarySearch(nums, left, right) :
            if left >= right : return nums[right]
            mid = (left+right) / 2
            if nums[mid] < nums[right] :
                return binarySearch(nums, left, mid)
            else :
                return binarySearch(nums, mid+1, right)
        return binarySearch(nums, 0, len(nums)-1)
#
# ---------------------
# 作者：Code_Granker
# 来源：CSDN
# 原文：https://blog.csdn.net/happyaaaaaaaaaaa/article/details/51525714
# 版权声明：本文为博主原创文章，转载请附上博文链接！
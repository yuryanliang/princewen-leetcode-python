# brute force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# 2 pointer
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        l = sorted(nums)
        left = 0
        right = len(l) - 1

        while left < right:
            if l[left] + l[right] == target:
                if l[left] == l[right]:
                    i_1 = nums.index(l[left])
                    import sys # [0, 4, 6, 0] for 0. [3, 3] for 6
                    nums[i_1] = sys.maxsize
                    i_2 = nums.index(l[right])
                    return [i_1, i_2]
                return [nums.index(l[left]), nums.index(l[right])]
            elif l[left] + l[right] < target:
                left += 1
            else:
                right -= 1
# hash table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range(len(nums)):
            if target - nums[i] in lookup:
                return [lookup.get(target - nums[i]), i]
            else:
                lookup[nums[i]] = i
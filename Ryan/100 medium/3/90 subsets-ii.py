"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

"""
用i + 1， 而不是start 加一。来略过已经用过的值
"""

class Solution:
    def subsetsWithDup(self, nums) :

        res = []
        alist =[]
        start = 0
        self.helper(nums, res, alist, start)
        return res
    def helper(self, nums, res, alist, start):
        temp = list(alist)
        res.append(temp)

        # temp.sort()
        # if temp not in res:
        #     res.append(temp)
        cur_index = start

        for i in range(start, len(nums)):
            alist.append(nums[i])
            self.helper(nums, res, alist, i + 1)
            alist.pop()
def main():
    nums = [1, 2, 2]
    print(Solution().subsetsWithDup(nums))


if __name__ == '__main__':
    main()
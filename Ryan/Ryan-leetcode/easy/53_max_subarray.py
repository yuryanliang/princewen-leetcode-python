# brute force
class Sol_1:
    def maxSubArray(self, nums) -> int:
        n = len(nums)
        max_sum = nums[0]
        for i in range(n):  # i = 3
            for j in range(i, n):  # j = 6
                cur_sum = self.subarray_sum(i, j, nums)
                max_sum = max(max_sum, cur_sum)
        return max_sum

    def subarray_sum(self, i, j, nums):  # i = 3, j = 6
        sum = 0
        for k in range(i, j + 1):
            sum += nums[k]
        return sum


# space complexity (n)
class Sol:
    def max_sub(self, nums):
        if not nums:
            return 0
        import sys
        max_sum = -sys.maxsize
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                max_sum = max(max_sum, sum(nums[i:j]))
        return max_sum


# brute force II
class Solution:
    def maxSubArray(self, nums):
        res = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                cur_sum = sum(nums[i:j])
                res.append(cur_sum)
        return max(res)


# best
class Sol_2:
    def max_subarray(self, nums):
        cur = nums[0]
        max_sum = cur

        for i in range(1, len(nums)):
            if cur < 0:  # 一旦前面总和<0,说明前面的加进去也是没用的，所以全部抛弃
                cur = 0
            cur += nums[i]
            max_sum = max(max_sum, cur)

        return max_sum


# a little modify from sol_2
class Sol_2_1:
    def max_subarray(self, nums):
        # cur = nums[0]
        cur = 0
        import sys
        max_sum = -sys.maxsize

        for i in range(0, len(nums)):
            # if cur < 0: # 一旦前面总和<0,说明前面的加进去也是没用的，所以全部抛弃
            #     cur = 0
            # cur += nums[i]
            cur = max(nums[i], cur + nums[i])  # 放弃cur，只取num，和不放弃cur，取num哪个大。
            max_sum = max(max_sum, cur)

        return max_sum


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    nums_1 = [-1, 2]
    # res = Sol_1().maxSubArray(nums)
    # res = Sol_2().max_subarray(nums)
    res_1 = Sol_2().max_subarray(nums)
    # res_1 = Sol().max_sub(nums)
    # print(res)
    print(res_1)


if __name__ == '__main__':
    main()

class Sol:
    def rem_ele(self, nums, val):
        if len(nums) == 0:
            return 0

        s = 0 # slow
        f = 0 # fast

        while f < len(nums):
            if nums[f] != val:
                nums[s] = nums[f]
                s += 1
            f += 1
        return s

c
class Sol:
    def rem_dup(self, nums) :
        if len(nums) < 2:
            return len(nums)
        s = 0 # slow
        f = 1 # fast
        while f < len(nums):
            if nums[s] != nums[f]:
                s += 1
                nums[s] = nums[f]
            f += 1
        return s + 1

def main():
    nums = [[1,2,2], [], [0,0,1,1,1,2,2,3,3,4]]
    for n in nums:
        length = Sol().rem_dup(n)
        print (n[:length])


if __name__ == '__main__':
    main()

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

class Sol:
    def remove(self, nums, target):

        s = 0
        f = 0

        while f < len(nums):
            if nums[f] != target:
                nums[s] = nums[f]
                s += 1
            f +=1
        return s


def main():
    nums = []
    print(Sol().remove(nums, 5))
    nums = [1,2,2,3]
    print(Sol().remove(nums, 2))

if __name__ == '__main__':
    main()

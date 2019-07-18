class Sol_1:
    def combine(self, n, k):
        nums=list(range(1,n+1))
        return self.helper(nums,k)

    def helper(self, nums,r):
        if r==1:
            return [[num] for num in nums]
        if len(nums)==r:
            return [nums]
        output=[]
        for index in range(len(nums)-r+1):
            for remainder in self.helper(nums[index+1:],r-1):
                output.append([nums[index]]+remainder)
        return output

class Sol_2:

    def combine(self, n, k):
        def _dfs(n, k, path, list_ret):
            # I am done with this combination, add to result
            if len(path) + 1 == k:
                list_ret.append([n] + path)
                return
            # Not done yet, construct path that includes this number
            for i in range(n - 1, 0, -1):
                _dfs(i, k, [n] + path, list_ret)

        list_ret = []
        if n < k or n == 0:
            return []
        k = 1 if k == 0 else k
        # Combinations may end from any number ranging from k to n
        # At the beginning, path is empty
        for i in range(k, n + 1):
            _dfs(i, k, [], list_ret)
        return list_ret

def main():
    n = 5
    k = 3
    print(Sol_2().combine(n, k))


if __name__ == '__main__':
    main()

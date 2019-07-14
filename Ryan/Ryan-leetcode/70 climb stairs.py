# brute force/ recursion
class Sol_1:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# two funcs; recursion
class Sol_1_1:
    def climbStairs(self, n):
        return self.climb(n)

    def climb(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return self.climb(n - 1) + self.climb(n - 2)

# two funcs; recursion + memo
class Sol_1_2:
    def climbStairs(self, n):
        dp = [-1 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        return self.climb(n, dp)

    def climb(self, n, dp):
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


# one func + memo -> dp
class Sol_1_3:
    def climbStairs(self, n):
        dp = [-1 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
    #     return self.climb(n, dp)
    #
    # def climb(self, n, dp):
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


def main_1():
    nums = [2, 3, 8]
    for n in nums:
        print(Sol_1().climbStairs(n))
        print(Sol_1_1().climbStairs(n))
        print(Sol_1_2().climbStairs(n))
        print(Sol_1_3().climbStairs(n))


# dp
# time complexity will be O(n) and our space will also be O(n), since we create a 1D array from 0 to n.
class Sol_2:
    def climbStairs(self, n: int) -> int:
        dp = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


def main_2():
    n = 3
    print(Sol_2().climbStairs(n))


# dp + space O(1)
# time complexity will be O(n)
class Sol_3:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1

        val_i_1 = 1
        val_i_2 = 1
        for i in range(2, n + 1):
            cur = val_i_1 + val_i_2
            val_i_2 = val_i_1
            val_i_1 = cur

        return cur



def main_3():
    nums = [2, 3, 8]
    for n in nums:
        print(Sol_3().climbStairs(3))


if __name__ == '__main__':
    # main_1()
    # main_2()
    main_3()

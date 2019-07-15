class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        x_str_rev = x_str[::-1]
        return x_str == x_str_rev

def main():
    nums = [121, -121, 10]
    for n in nums:
        print(Solution().isPalindrome(n))


class Sol_1:
    def is_palindrome(self, x):
        if x < 0:
            return False
        res = 0
        n = x
        while n:
            res = res * 10 + n % 10
            n = n // 10
        return res == x

def main_1():
    nums = [121, -121, 10]
    for n in nums:
        print(Sol_1().is_palindrome(n))

if __name__ == '__main__':
    # main()
    main_1()

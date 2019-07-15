# brute force
class Sol_1:
    def reverse(self, x): # x = -123
        positive = True
        if x < 0:
            positive = False # positive = False
            x = -x # x = 123

        # put x into str digit and then put into a stack
        x_str = str(x) # x_str = "123"
        stack = []
        while len(x_str) > 0:
            stack.append(x_str[0]) # stack = [ "1", "2", "3"]
            x_str = x_str[1:]
        # pop stack to form new str

        rev_x = ''
        while len(stack) > 0:
            rev_x = rev_x + stack.pop() # rev_x = "321"

        # back to int
        res = int(rev_x) if positive else -int(rev_x)
        if res < -2 ** 31 or res > 2 ** 31 -1:
            return 0
        else:
            return res

def main_1():
    x = [-123]
    for n in x:
        print(Sol_1().reverse(n))

class Solution(object):

    def reverse(self, x):
        n = x if x > 0 else -x # need to change to n, otherwise  the lower x sign check, x will be 0
        res = 0
        while n:
            res = res * 10 + n % 10
            n = n //10
        if res > 0x7fffffff:
            return 0
        else:
            return res if x > 0 else -res
def main():
    x = [-123]
    for n in x:
        print(Solution().reverse(n))
if __name__ == '__main__':
    # main_1()
    main()

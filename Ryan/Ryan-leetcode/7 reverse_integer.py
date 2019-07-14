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


if __name__ == '__main__':
    main_1()

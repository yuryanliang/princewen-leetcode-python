# brute force
class Sol_1:
    def pow(self, x, n):
        n1 = n if n > 0 else -n
        res = 1
        for i in range(n1 ):
            res = res *x
        return res if n > 0 else 1 / res


def main_1():
    print(Sol_1().pow(2.00000, -2))
    print(Sol_1().pow(2.10000, 3))
    print(Sol_1().pow(2.00000, 10))

# recursion
class Sol_2:
    def pow(self, x, n):
        if n == 0:
            return 1
        half = self.pow(x, n // 2)

        if n % 2 ==0:
            return half ** 2
        if x > 0:
            return half ** 2 * x
        return half ** 2 / x


def main_2():
    print(Sol_2().pow(2.00000, -2))
    print(Sol_2().pow(2.10000, 3))
    print(Sol_2().pow(2.00000, 10))


if __name__ == '__main__':
    main_1()
    main_2()

"""

5, 7

num instead of ind

when target = 5
nums = [ 1, 2, 3, 4, 5]

find a x where
small = x * x < 5, and large = (x + 1) * (x + 1) > 5

then x if abs(small - 5 ) < abs (large - 5) else x + 1

x in nums


"""

def sqrt(target): # target = 5

    temp = 1
    for x in range(1, target +1): # x = 2
        if 5 / x > x and 5 / (x + 1) < (x + 1):
            temp = x # temp = 2
            break
    print(temp, "temp", target)
    # temp = 2
    small = temp ** 2 # samll is 4
    large = (temp + 1) ** 2 # large is 9
    res = temp if abs(small - target) < abs(large - target ) else temp + 1
    return res

def sqrt_1(target):
    temp = 0
    while temp ** 2 <= target:
        temp +=1
    temp = temp - 1
    print(temp, "temp", target)

    small = temp ** 2 # samll is 4
    large = (temp + 1) ** 2 # large is 9
    res = temp if abs(small - target) < abs(large - target ) else temp + 1
    return res

def sqrt_bi(target): # target = 3
    left = 0 # left = 0
    right = target # right = 3

    temp = 0
    while left < right:
        mid = left + (right - left) // 2 # mid = 1

        small = mid ** 2 # small = 1
        large = (mid + 1) ** 2 # large = 4

        if small < target and target < large:
            temp = mid
            break
        elif target <= small:
            right = mid
        elif target >= large:
            left = mid + 1

    small = temp ** 2 # samll is 4
    large = (temp + 1) ** 2 # large is 9
    res = temp if abs(small - target) < abs(large - target ) else temp + 1
    return res





def main():
    # print(sqrt(5))
    # print(sqrt(6))
    # print(sqrt(7))
    # print(sqrt(8))
    #
    # print(sqrt_1(5))
    # print(sqrt_1(6))
    # print(sqrt_1(7))
    # print(sqrt_1(8))

    print(sqrt_bi(5))
    print(sqrt_bi(6))
    print(sqrt_bi(7))
    print(sqrt_bi(8))

main()
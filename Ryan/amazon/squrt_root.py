"""
[] 1, 2  is num

+ - verify

1*1=2, 2*2=4

n=6, i=2, i*i=4, i=3, i*i=9,

n=7, sol=2,; , sol=3, 9

n=5, sol=2

n=5, i=1, j=5

mid=(1+5)/2=3
mid*mid=9
j=mid-1
e


"""





def sqrt(n):  # n=7
    if n == 0: return 0
    if n < 0:
        print("the number can't be negative")
        return -1

    i = 1
    while i <= n:  # i=2<5
        if i * i == n:  # 4==5
            return i
        else:
            sol_i = i * i  # sol_i is 4
            sol_i1 = (i + 1) * (i + 1)  # sol_i1 is 9

            if sol_i < n and sol_i1 > n:  # 4<5 and 9>5
                if abs(sol_i - n) < abs(sol_i1 - n):  # 1<4
                    return i
                else:
                    return i + 1
        i += 1


# data=[3, 4, 5, 6, 7, 8, 9]
# for i in data:
#     print(i, sqrt(i))



def sqrt_binary(n):  # n =5
    if n == 0: return 0
    if n < 0:
        print("the number can't be negative")
        return -1

    start = 1
    end = n  # end=5

    while (start <= end):  # 1<=7   end =7, start=1
        mid = (start + end) // 2  # mid=4

        if (mid * mid) == n:  # 16==7
            return mid

        sol_mid = mid * mid  # 16
        sol_mid1 = (mid + 1) * (mid + 1)  # 25

        # if sol_i< n and sol_i1>n:
        #  i=2, sol_i=4, i=3, sol=9

        # n=5 ,return if abs(sol_i-n)<abs(sol_i1-n) return

        if (mid * mid < n):  # 16<7
            start = mid + 1  # start =
            # sol=mid #sol=2
        else:
            end = mid - 1  # end = 2

    #     i=end
    #     sol_i = i * i  # sol_i is 4
    #     sol_i1 = (i + 1) * (i + 1)  # sol_i1 is 9
    #
    #     if sol_i < n and sol_i1 > n:  # 4<5 and 9>5
    #         if abs(sol_i - n) < abs(sol_i1 - n):  # 1<4
    #             return i
    #         else:
    #             return i + 1
    #
    #
    # return i  # sol =2
    return end

def mySqrt( x):
    """
    :type x: int
    :rtype: int
    """
    if x < 2:
        return x

    left = 1
    right = x

    while left <= right:
        mid = (left + right) // 2
        if mid ** 2 > x:
            right = mid - 1
        else:
            left = mid + 1
    return right

def main():
    data=[3, 4, 5, 6, 7, 8, 9]

    for i in data:
        print(i, mySqrt(i))

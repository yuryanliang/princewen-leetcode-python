class Solution:
    def plusOne(self, digits) :
        carry = 1
        for i in range(-1, -len(digits) - 1, -1):
            if digits[i] + carry > 9:
                digits[i] = 0
                carry = 1
            else:
                digits[i] = digits[i] + carry
                carry = 0
        if carry == 1:
            digits.insert(0, 1)
        return digits

def main():
    digits = [1, 2, 3]
    print(Solution().plusOne(digits))

class Sol_1:
    def plus_one(self, d):
        for i in range(len(d)-1, -1,-1):
            if d[i]<9:
                d[i]+=1
                return d
            d[i]=0
        return [1]+d

def main_1():
    digits = [1, 2, 3]
    print(Sol_1().plus_one(digits))

if __name__ == '__main__':
    main()
    main_1()

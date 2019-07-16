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
            if d[i]<9: #结束条件，当 d[i] < 9, 把这位加一， 循环就结束。只有当前一位是9的时候，才能到这一步。除了第一步
                d[i]+=1
                return d
            d[i]=0
        return [1]+d

def main_1():
    digits = [1, 0, 9]
    print(Sol_1().plus_one(digits))

# 末尾取余数， 取进位
class Solution:
    def plusOne(self, digits) :
        carry = 1
        for i in range(-1, -len(digits)-1, -1):
     # for i in range(len(d) - 1, -1, -1):

            temp = digits[i]
            digits[i] = (digits[i] + carry) % 10
            carry = (temp + carry) // 10
        return [1] + digits if carry > 0 else digits

if __name__ == '__main__':
    main()
    main_1()


def Plus_one(d):
        for i in range(len(d)-1, -1,-1):
            if d[i]<9:
                d[i]+=1
                return d
            d[i]=0
        return [1]+d

if __name__=="__main__":
    Plus_one([1,2,3])

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        add = 1
        for i in range(len(digits)-1, -1, -1):
            num = digits[i]+add
            digits[i] = num%10
            add = int(num/10)
        if add != 0:
            digits = list(map(int, str(add))) + digits
        return digits
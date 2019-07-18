class Sol_1:
    def strStr(self, haystack, needle) :

        if not needle:
            return 0

        i = 0
        while i <= len(haystack) - len(needle):
            if haystack[i] == needle[0]:
                j=1
                while j < len(needle):
                    if haystack[i + j] != needle[j]:
                        break
                    j += 1
                if j == len(needle):
                    return i
            i += 1
        return -1

def main_1():
    haystack="aaabaaabbbabaa"
    needle="babb"
    needle="aba"
    print(Sol_1().strStr(haystack, needle))
    print(Sol().strstr(haystack,needle))

class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        elif needle in haystack:
            return haystack.index(needle)
        elif not needle in haystack:
            return -1
        
if __name__ == '__main__':
    main_1()

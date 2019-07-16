class Solution:
    def isValid(self, s):
        stack = []
        # arr = s.split()

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)

            elif c == ')' or c == ']' or c == '}':
                if len(stack) == 0:
                    return False
                else:
                    temp = stack.pop()
                    if (c == ')' and temp != '(') or (c == ']' and temp != '[') or (c == '}' and temp != '{'):
                        return False
        if len(stack) == 0:
            return True
        else:
            return False

def main():
    s="(]"
    print(Solution().isValid(s))


if __name__ == '__main__':
    main()

class Sol:
    def is_val(self, s):
        left = {"(": 1, "[" : 2, "{": 3}
        right = {")": 1, "]" : 2, "}": 3}

        if s[0] in right:
            return False

        if len(s) == 0:
            return True

        stack = []
        for c in s:
            if c in left:
                stack.append(c)
            elif c in right:
                if not stack:
                    return False
                else:
                    temp = stack.pop()
                    if left[temp] != right[c]:
                        return False
        if stack:
            return False
        else:
            return True



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

"""
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        lookup =defaultdict(list)
        for i, c in enumerate(s):
            lookup[c].append(i)
        less = [i for i in lookup.values() if len(i) < k]
        breakpt = []
        for j in less:
            for n in j:
                breakpt.append(n)


        1==1
if __name__ == '__main__':
    s = "aebabbc"
    k = 2
    print(Solution().longestSubstring(s, k))





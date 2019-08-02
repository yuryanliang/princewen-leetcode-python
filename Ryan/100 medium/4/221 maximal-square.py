"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""

# public:
#     int maximalSquare(vector<vector<char> >& matrix) {
#         int res = 0;
#         for (int i = 0; i < matrix.size(); ++i) {
#             vector<int> v(matrix[i].size(), 0);
#             for (int j = i; j < matrix.size(); ++j) {
#                 for (int k = 0; k < matrix[j].size(); ++k) {
#                     if (matrix[j][k] == '1') ++v[k];
#                 }
#                 res = max(res, getSquareArea(v, j - i + 1));
#             }
#         }
#         return res;
#     }
#     int getSquareArea(vector<int> &v, int k) {
#         if (v.size() < k) return 0;
#         int count = 0;
#         for (int i = 0; i < v.size(); ++i) {
#             if (v[i] != k) count = 0;
#             else ++count;
#             if (count == k) return k * k;
#         }
#         return 0;
#     }

class Solution:
    def maximalSquare(self, matrix):
        res = 0
        for i in range(len(matrix)):
            v = [0 for _ in range(len(matrix[i]))]
            for j in range(i, len(matrix)):
                for k in range(len(matrix[j])):
                    if matrix[j][k]=="1":
                        v[k]+=1
                res = max(res, self.getSquareArea(v, j-i+ 1))
        return res
    def getSquareArea(self, v, k):
        if len(v)<k:
            return 0
        count = 0
        for i in range(len(v)):
            if v[i] != k :
                count = 0
            else:
                count +=1
            if count ==k :
                return k * k
        return 0
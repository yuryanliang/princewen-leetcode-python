"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.


找到第k小个数。
"""
class Solution:
    def kthSmallest(self, matrix, k) :
        import heapq
        q = []
        heapq.heapify(q)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(q,matrix[i][j])
        for j in range(k):
            res = heapq.heappop(q)
        return res


import heapq


class Solution(object):
  def kthSmallest(self, matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    visited = {(0, 0)}
    heap = [(matrix[0][0], (0, 0))]

    while heap:
      val, (i, j) = heapq.heappop(heap)
      k -= 1
      if k == 0:
        return val
      if i + 1 < len(matrix) and (i + 1, j) not in visited:
        heapq.heappush(heap, (matrix[i + 1][j], (i + 1, j)))
        visited.add((i + 1, j))
      if j + 1 < len(matrix) and (i, j + 1) not in visited:
        heapq.heappush(heap, (matrix[i][j + 1], (i, j + 1)))
        visited.add((i, j + 1))


if __name__ == '__main__':
    matrix =[[1,5,9],[10,11,13],[12,13,15]]
    k = 8
    print(Solution().kthSmallest(matrix, k ))

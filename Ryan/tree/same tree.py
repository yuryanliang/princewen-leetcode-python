public class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        }
        if (p == null || q == null) {//p或者q只有一方是null
            return false;
        }
        if (p.val != q.val) {
            return false;
        }
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}


# Time:  O(n)
# Space: O(h), h is height of binary tree
#原题地址：https://oj.leetcode.com/problems/same-tree/

时间复杂度是O(n)，空间复杂度是O(logn)。

题意：判断两棵树是否是同一棵树。

解题思路：这题比较简单。用递归来做。首先判断两个根节点的值是否相同，如果相同，递归判断根的左右子树。

代码：

复制代码
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p == None and q is None: return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

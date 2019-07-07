# O(n)
# space O(log n)
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            #if sum==root.val:
            #    return True
            #else:
            #    return False
            return sum==root.val
        return self.hasPathSum(root.left, sum-root.val ) or self.hasPathSum(root.right, sum-root.val )

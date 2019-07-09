"""

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

"""

"""据前序的结果判定根结点，再根据中序遍历的结果确定左右子树的结点，如此递归。"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:root_index + 1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index + 1:], inorder[root_index + 1:])
        return root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.helper(0, 0, len(preorder) - 1, preorder, inorder)

    def helper(self, pre_start, in_start, in_end, preorder, inorder):
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root_val = preorder[0]
        root = TreeNode(root_val)

        # left branch
        # in-order
        root_index = inorder.index(root_val)
        left_inorder = inorder[in_start: root_index]
        left_branch_len = len(left_inorder)
        # pre-order
        left_preorder = preorder[pre_start + 1:left_branch_len + 1]

        root.left = self.helper(0, 0, left_branch_len - 1, left_preorder, left_inorder)

        # right branch
        # in-order
        right_inorder = inorder[root_index + 1:in_end + 1]
        right_branch_len = len(right_inorder)
        # pre-order
        right_preorder = preorder[left_branch_len + 1:in_end + 1]

        root.right = self.helper(0, 0, right_branch_len - 1, right_preorder, right_inorder)

        return root
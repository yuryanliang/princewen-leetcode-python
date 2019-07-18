# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        if not root:
            return True
        if abs(self.get_depth(root.left) - self.get_depth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def get_depth(self, root):
        if not root:
            return 0
        return 1 + max(self.get_depth(root.left), self.get_depth(root.right))

# class Solution {
# public:
#     bool isBalanced(TreeNode *root) {
#         if (checkDepth(root) == -1) return false;
#         else return true;
#     }
#     int checkDepth(TreeNode *root) {
#         if (!root) return 0;
#         int left = checkDepth(root->left);
#         if (left == -1) return -1;
#         int right = checkDepth(root->right);
#         if (right == -1) return -1;
#         int diff = abs(left - right);
#         if (diff > 1) return -1;
#         else return 1 + max(left, right);
#     }
# };

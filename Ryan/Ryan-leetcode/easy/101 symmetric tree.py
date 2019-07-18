# Definition for a binary tree node.
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return self.helper(root.left, root.right)

    def helper(self, left, right):
        if not left and not right:
            return True
        if (left and not right) or (right and not left) or (left.val != right.val):
            return False
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    print(Solution().isSymmetric(root))


# class Solution {
# public:
#     bool isSymmetric(TreeNode* root) {
#         if (!root) return true;
#         queue<TreeNode*> q1, q2;
#         q1.push(root->left);
#         q2.push(root->right);
#         while (!q1.empty() && !q2.empty()) {
#             TreeNode *node1 = q1.front(); q1.pop();
#             TreeNode *node2 = q2.front(); q2.pop();
#             if (!node1 && !node2) continue;
#             if((node1 && !node2) || (!node1 && node2)) return false;
#             if (node1->val != node2->val) return false;
#             q1.push(node1->left);
#             q1.push(node1->right);
#             q2.push(node2->right);
#             q2.push(node2->left);
#         }
#         return true;
#     }
# };

if __name__ == '__main__':
    main()

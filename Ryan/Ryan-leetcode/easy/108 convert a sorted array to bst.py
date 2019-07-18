# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        n = len(nums)

        if n == 0:
            return None
        else:
            root = TreeNode(nums[n // 2])
            root.left = self.sortedArrayToBST(nums[: n // 2])
            root.right = self.sortedArrayToBST(nums[n // 2 + 1:])
        return root


#
# class Solution {
# public:
#     TreeNode* sortedArrayToBST(vector<int>& nums) {
#         return helper(nums, 0 , (int)nums.size() - 1);
#     }
#     TreeNode* helper(vector<int>& nums, int left, int right) {
#         if (left > right) return NULL;
#         int mid = left + (right - left) / 2;
#         TreeNode *cur = new TreeNode(nums[mid]);
#         cur->left = helper(nums, left, mid - 1);
#         cur->right = helper(nums, mid + 1, right);
#         return cur;
#     }
# };
def main():
    nums = [1, 2, 3, 4]
    a = Solution().sortedArrayToBST(nums)
    1 == 1


if __name__ == '__main__':
    main()

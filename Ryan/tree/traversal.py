# https://segmentfault.com/a/1190000013766957
# https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45551/preorder-inorder-and-postorder-iteratively-summarization
# https://cloud.tencent.com/developer/article/1377666
# https://cloud.tencent.com/developer/article/1377662
# https://mp.weixin.qq.com/s?__biz=MzUyNjQxNjYyMg==&mid=2247483843&idx=1&sn=994bf0d42dd9941a879a3a3ed500a4d6&chksm=fa0e6e42cd79e75472404eb5da7ee98f20d303efe230eb4f41efec57164630f555e7111e62ff&scene=21#wechat_redirect

# Time:  O(n)
# Space: O(1)
#
# Given a binary tree, return the preorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].
#
# Note: Recursive solution is trivial, could you do it iteratively?
#

# Definition for a  binary tree node
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Morris Traversal Solution
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, curr = [], root
        while curr:
            if curr.left is None:
                result.append(curr.val)
                curr = curr.right
            else:
                node = curr.left
                while node.right and node.right != curr:
                    node = node.right

                if node.right is None:
                    result.append(curr.val)
                    node.right = curr
                    curr = curr.left
                else:
                    node.right = None
                    curr = curr.right

        return result


# Time:  O(n)
# Space: O(h)
# Stack Solution
class Solution2(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, stack = [], [(root, False)]
        while stack:
            root, is_visited = stack.pop()
            if root is None:
                continue
            if is_visited:
                result.append(root.val)
            else:
                stack.append((root.right, False))
                stack.append((root.left, False))
                stack.append((root, True))
        return result

    """
    模版　
    """

    # 下面这种写法使用了一个辅助结点p，这种写法其实可以看作是一个模版，对应的还有中序和后序的模版写法，形式很统一，方便于记忆。

    def pre_order_template(self, root):
        res = []
        stack = []
        p = root
        # 辅助结点p初始化为根结点，while循环的条件是栈不为空或者辅助结点p不为空
        while stack or p:
            # 在循环中首先判断如果辅助结点p存在，那么先将p加入栈中，然后将p的结点值加入结果res中，此时p指向其左子结点
            if p:
                stack.append(p)
                res.append(p.val)
                p = p.left
            # 否则如果p不存在的话，表明没有左子结点，我们取出栈顶结点，将p指向栈顶结点的右子结点
            else:
                temp = stack.pop()
                p = temp.right
        return res

    def in_order_template(self, root):
        res = []
        stack = []
        p = root
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                temp = stack.pop()
                res.append(temp.val)
                p = temp.right
        return res

    # pre order , root, left, right => root, right, left =reverse=> left, right, root
    def post_order_template(self, root):
        res = []
        stack = []
        p = root
        while p or stack:
            if p:
                stack.append(p)
                res.insert(0, p.val)  # reverse res
                p = p.right  # reverse pre order
            else:
                temp = stack.pop()
                p = temp.left  # reverse pre order
        return res

    def pre_stack(self, root):
        if not root:
            return []
        res = []
        stack = deque()
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            # because stack is LIFO, so first right, then left
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res


class Recursion:

    def pre_order(self, node):
        if not node:
            return
        print(node.val)
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, node):
        if not node:
            return
        self.in_order(node.left)
        print(node.val)
        self.in_order(node.right)

    def post_order(self, node):
        if not node:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.val)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    # root.left.right.left=TreeNode(6)

    # result = Solution().preorderTraversal(root)
    # result = Solution2().pre_stack(root)
    # result = Solution2().in_order_template(root)
    result = Solution2().post_order_template(root)

    print(result)

    print("pre order")
    Recursion().pre_order(root)

    print("in order")
    Recursion().in_order(root)

    print("post order")
    Recursion().post_order(root)

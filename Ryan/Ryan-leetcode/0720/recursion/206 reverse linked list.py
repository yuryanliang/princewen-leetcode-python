"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Recursion:
    def rev(self, head):
        if head == None or head.next == None:
            return head
        newlist = self.rev(head.next)

        t2 = head.next
        t2.next = head
        head.next = None
        return newlist


def main_1():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    rev_head = Recursion().rev(head)
    1 == 1



# Iterative solution.
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        dummy = ListNode(float("-inf"))
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next

if __name__ == '__main__':
    main_1()

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

"""
my solution
两个指针，一个记录当前的头节点，一个记录将要称为头节点的节点
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        p = head
        q = head.next

        while q:
            head.next = q.next
            q.next = p
            p = q
            q = head.next
        return p



if __name__ == '__main__':
    main_1()

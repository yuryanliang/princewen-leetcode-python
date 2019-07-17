# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def display(node):
    elem = []
    cur = node
    while cur:
        elem.append(cur.val)
        cur = cur.next
    print(elem)
# iteration
class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head

        while head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return dummy.next

def main():
    l1 = ListNode(1)
    l1.next = ListNode(1)
    l1.next.next = ListNode(4)

    head = Solution().deleteDuplicates(l1)
    display(head)

# recursion
class Sol_1:
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        if head.val == head.next.val:
            return head.next
        else:
            return head
        head.next = self.deleteDuplicates(head.next)


def main_1():
    l1 = ListNode(1)
    l1.next = ListNode(1)
    l1.next.next = ListNode(4)

    head = Solution().deleteDuplicates(l1)
    display(head)
if __name__ == '__main__':
    main()
    main_1()

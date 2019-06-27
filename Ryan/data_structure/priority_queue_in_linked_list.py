# https://www.geeksforgeeks.org/priority-queue-using-linked-list/

# The list is so created so that the highest priority element is always at the head of the list.
# The list is arranged in descending order of elements based on their priority.
# This allow us to remove the highest priority element in O(1) time.
# To insert an element we must traverse the list and find the proper position to insert the node
# so that the overall order of the priority queue is maintained.
# This makes the push() operation takes O(N) time.
# The pop() and peek() operations are performed in constant time.
class node:
    def __init__(self, val):
        self.val = val
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.head = node(None)

    def push(self, val):
        new = node(val)
        if not self.head.val:
            self.head = new
            return
        if self.head.val < new.val:
            new.next = self.head
            self.head = new
            return
        temp = self.head
        while temp.next and temp.next.val > new.val:
            temp = temp.next

        #  Either at the ends of the list
        # or at required position
        new.next = temp.next
        temp.next = new

    def peek(self, val):
        pass

    def pop1(self):
        temp = self.head
        self.head = self.head.next
        return temp.val

    def __str__(self):
        list = []
        node = self.head
        if not node.val:
            return ""
        list.append(node.val)
        while node.next:
            list.append(node.next.val)
            node = node.next

        return " ".join(str(val) for val in list)


if __name__ == "__main__":
    pq = PriorityQueue()
    # pq.pop1()
    # print("empty pq", pq, "pop1 is ", pq.pop1())
    pq.push(5)

    # pq.push(4)
    # pq.push(3)
    print(pq)
    pq.push(3)
    print(pq)
    pq.push(1)
    print(pq)
    pq.push(2)
    print(pq)
    pq.push(3)
    print(pq)

    print(pq.pop1())
    print(pq)

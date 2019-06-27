class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next is not None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            elems.append(cur.data)
        print (elems)

    def get(self, index):
        if index >= self.length():
            print ("Error, index out of range")
            return None
        cur_idx = 0
        cur_node = self.head

        while cur_node.next is not None:
            cur_node = cur_node.next
            if cur_idx == index: return cur_node.data
            cur_idx += 1

    def erase(self, index):
        if index>=self.length():
            print ("Error, index out of range")
            return None
        cur_idx = 0
        cur_node = self.head

        while cur_node.next is not None:
            last_node=cur_node
            cur_node=cur_node.next
            if cur_idx==index:
                last_node.next=cur_node.next
                return
            cur_idx+=1



if __name__ == "__main__":
    my_list = linked_list()
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)

    print("length", my_list.length())
    my_list.display()

    print( my_list.get(1))
    my_list.erase(0)
    my_list.display()
    1 == 1

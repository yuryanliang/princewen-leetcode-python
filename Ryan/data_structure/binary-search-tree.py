import sys


class node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child is None:
                cur_node.left_child = node(value)
                cur_node.left_child.parent = cur_node
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child is None:
                cur_node.right_child = node(value)
                cur_node.right_child.parent = cur_node
            else:
                self._insert(value, cur_node.right_child)
        else:  # equal
            print ("value alreay in tree")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left_child)
            print (str(cur_node.value))
            self._print_tree(cur_node.right_child)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        left_height = self._height(cur_node.left_child, cur_height + 1)
        right_height = self._height(cur_node.right_child, cur_height + 1)
        return max(left_height, right_height)

    # return the node of the value
    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, cur_node):
        if cur_node.value == value:
            return cur_node
        elif value < cur_node.value and cur_node.left_child is not None:
            return self._find(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child is not None:
            return self._find(value, cur_node.right_child)
        else:
            return None

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):
        def min_value_node(node):
            cur = node
            while cur.left_child is not None:
                cur = cur.left_child
            return cur

        def num_children(node):
            num_children = 0
            if node.left_child is not None:
                num_children += 1
            if node.right_child is not None:
                num_children += 1
            return num_children

        node_parent = node.parent
        node_children = num_children(node)

        # case 1,
        if node_children == 0:
            if node_parent.left_child == node:
                node_parent.left_child = None
            else:
                node_parent.right_child = None

        # case 2
        if node_children == 1:
            # get the child
            if node.left_child is not None:
                child = node.left_child
            else:
                child = node.right_child
            # put the child back
            if node_parent.left_child == node:
                node_parent.left_child = child
            else:
                node_parent.right_child = child
            child.parent = node_parent

        # case 3
        if node_children == 2:
            # get the inorder successor of the deleted node
            successor = min_value_node(node.right_child)
            # copy the inorder successor's value to the node we formerly holding the value we wish to delete
            node.value = successor.value

            self.delete_node(successor)

    # return true of false
    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, cur_node):
        if cur_node.value == value:
            return True
        elif (value < cur_node.value) and (cur_node.left_child is not None):
            return self._search(value, cur_node.left_child)
        elif (value > cur_node.value) and (cur_node.right_child is not None):
            return self._search(value, cur_node.right_child)
        return False


def fill_tree(tree, num_elems=3, max_int=10):
    from random import randint
    for _ in range(num_elems):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree


def validate_bst(root, min=-sys.maxsize, max=sys.maxsize):
    if root is None:
        return True
    if (root.value > min) and (root.value < max) and (validate_bst(root.left_child, min, root.value)) and (
    validate_bst(root.right_child, root.value, max)):
        return True
    else:
        return False


if __name__ == '__main__':
    tree = binary_search_tree()
    tree = fill_tree(tree, 5, 10)
    tree.insert(4)
    tree.print_tree()

    # tree.print_tree()
    # print tree.height()
    # tree.print_tree()
    #
    print ("search :", tree.search(4))
    # n = tree.find(10)
    tree.delete_value(4)
    tree.print_tree()
    1 == 1

    root = node(10)
    root.left_child = node(9)
    root.right_child = node(12)
    print(validate_bst(root))

# adding the classes and functions for inserting into a binary search tree
class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f'|- Value: {self.value}, Left: {self.left}, Right: {self.right} -|'


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        inserted = False
        current_node = self.root
        while not inserted:
            if self.root == None:
                self.root = new_node
                inserted = True
            else:
                if new_node.value <= current_node.value:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = new_node
                        inserted = True
                elif new_node.value > current_node.value:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = new_node
                        inserted = True
        return self.root


# n1 = Node(8)
# print(n1.left)
# bst1 = BinarySearchTree()
# print(bst1.insert(10))
# print(bst1.insert(3))
# print(bst1.insert(15))
# print(bst1.insert(8))
# print(bst1.insert(2))
# print(bst1.root.value)

# tbd
from queue import Queue
from binary_search_tree_insert import Node


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

    def breadth_first_search(self, val):
        # val = value we are searching for in the treee
        tree_queue = Queue()
        if not self.root:
            return 'Not found'
        tree_queue.enqueue(self.root)
        while tree_queue.size:
            popped_node = tree_queue.dequeue()
            print(popped_node)
            print(f"value: {popped_node.value.value}")
            if val == popped_node.value.value:
                # return popped_node.value
                return f'Node found {popped_node.value}'
            else:
                if popped_node.value.right:
                    tree_queue.enqueue(popped_node.right)
                if popped_node.value.left:
                    tree_queue.enqueue(popped_node.left)
            print('yes')
            print(tree_queue)
        return 'Not found'


bst1 = BinarySearchTree()
bst1.insert(8)
print(bst1.root)
print(bst1.breadth_first_search(8))

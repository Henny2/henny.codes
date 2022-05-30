class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None

    def __repr__(self) -> str:
        return f"| Node: {self.value}, next: {self.next} |"

# Stack = genral idea of a LIFO data structure, multiple ways to implement it
# push and pop both from head
# using singly linked list
# if doubly linked list, operations on tail would work as well
# better than array, as we do not need the indexing etc


class Stack:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, value):
        # adds new node to the beginning of the linked list
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.tail == None:
            self.tail = new_node
        self.size += 1
        return new_node

    def pop(self):
        # returns the node that was last added to the stack
        if self.head == None:
            return None
        if self.size == 1:
            self.tail = None
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        popped_node.next = None
        return popped_node

    def __repr__(self) -> str:
        return f'Head: {self.head}, Tail: {self.tail}, Size: {self.size}'


paper_stack = Stack()
print(paper_stack.pop())
print(paper_stack.push(3))
print(paper_stack.push(11))
print(paper_stack.push(2))
print(paper_stack.push(6))
print("----------------------------")
print(paper_stack.pop())
print(paper_stack)

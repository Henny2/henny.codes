class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return f'|- Value: {self.value}, Next: {self.next} -|'


class Queue:
    """
        First in, first out data structure. 
    """

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self) -> str:
        return f'|- Head: {self.head}, Tail: {self.tail}, Size: {self.size} -|'

    def enqueue(self, value):
        """we are enqueueing at the tail

        Args:
            value (any): value that will be added to the queue
        """
        new_node = Node(value)

        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        return new_node

    def dequeue(self):
        """We are dequeueing from the beginning (head)
        """
        # if self.size == 0:
        #     # return ExecError('The queue is empty. Nothing to dequeue.')
        #     return None
        dequeued_node = self.head
        if self.size > 0:
            self.size -= 1
        if self.size <= 1:
            self.head = None
            self.tail = None
        else:
            self.head = dequeued_node.next
        return dequeued_node


q = Queue()
print(q.enqueue(1))
print(q.enqueue(8))

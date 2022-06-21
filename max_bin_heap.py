class MaxBinaryHeap:
    def __init__(self) -> None:
        self.values = []

    def swap(self, pos1, pos2):
        temp = self.values[pos1]
        self.values[pos1] = self.values[pos2]
        self.values[pos2] = temp

    def insert(self, value):
        self.values.append(value)
        pos_new_item = len(self.values)-1
        # new_item = self.values[pos_new_item]
        pos_parent = int((pos_new_item - 1)/2)
        parent = self.values[pos_parent]
        while parent < value:
            # swap items
            self.swap(pos_new_item, pos_parent)
            pos_new_item = pos_parent
            pos_parent = int((pos_new_item - 1)/2)
            parent = self.values[pos_parent]
        print(self.values)


mbh = MaxBinaryHeap()
mbh.insert(10)
mbh.insert(1)
mbh.insert(3)
mbh.insert(12)
mbh.insert(33)
mbh.insert(22)

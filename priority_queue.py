class Node:
    def __init__(self, prio, val) -> None:
        self.priority = prio
        self.value = val


class PriorityQueue:
    def __init__(self) -> None:
        self.values = []

    def swap(self, pos1, pos2):
        temp = self.values[pos1]
        print('swap')
        print(pos1, pos2)
        self.values[pos1] = self.values[pos2]
        self.values[pos2] = temp

    def insert(self, node):
        self.values.append(node)
        pos_new_item = len(self.values)-1
        # new_item = self.values[pos_new_item]
        pos_parent = int((pos_new_item - 1)/2)
        parent_prio = self.values[pos_parent].priority
        while parent_prio < node.priority:
            # swap items
            self.swap(pos_new_item, pos_parent)
            pos_new_item = pos_parent
            pos_parent = int((pos_new_item - 1)/2)
            parent = self.values[pos_parent]
        print(self.values)

    def extractMax(self):
        print(self.values)
        if self.values:
            high_pri_item = self.values[0]
        else:
            raise SyntaxError('MBH does not exist, cannot extract Max.')
        # put last element in first place
        sinking_node = self.values.pop()
        sinking_node_index = 0
        self.values[0] = sinking_node
        # sink down the first element
        child1_index = 2*sinking_node_index + 1
        child2_index = 2*sinking_node_index + 2
        child1 = self.values[child1_index]
        child2 = self.values[child2_index]
        print(self.values)
        while sinking_node < child1 or sinking_node < child2:
            if child1 > child2:
                print(f'{sinking_node_index}, {child1_index}, here')
                self.swap(sinking_node_index, child1_index)
                sinking_node_index = child1_index
            else:
                print(f'{sinking_node_index}, {child2_index}, here2')
                self.swap(sinking_node_index, child2_index)
                sinking_node_index = child2_index
            child1_index = 2*sinking_node_index + 1
            child2_index = 2*sinking_node_index + 2
            print(child1_index, child2_index)
            if child1_index > len(self.values)-1:
                child1 = 0
            if child2_index > len(self.values)-1:
                child2 = 0
            print(self.values)
        return high_pri_item

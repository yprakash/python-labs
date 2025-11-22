# @author: yprakash

import math

class PriorityQueue(object):
    def __init__(self):
        self.heap = []

    def __str__(self):
        return ' '.join([str(i) for i in self.heap])

    def _parent(self, index):
        return math.floor((index - 1) / 2)

    def _left_child(self, index):
        return 1 + 2 * index

    def _right_child(self, index):
        return 2 + 2 * index

    def _get_bigger_child_index(self, p):
        li = self._left_child(p)
        if li >= self.size():
            return None
        ri = self._right_child(p)
        if ri >= self.size():
            return li
        return ri if self.heap[li] < self.heap[ri] else li

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        return self.heap[0]

    def pop(self):
        if self.is_empty():
            return None  # raise "EMPTY PriorityQueue"
        if self.size() <= 2:
            return self.heap.pop(0)

        elem = self.heap[0]
        self.heap[0] = self.heap.pop(0)
        p, c = 0, self._get_bigger_child_index(0)

        while c and self.heap[p] < self.heap[c]:
            self.heap[p], self.heap[c] = self.heap[c], self.heap[p]
            p, c = c, self._get_bigger_child_index(c)

        return elem

    def push(self, item):
        c = self.size()
        self.heap.append(item)
        # heapify
        while c > 0:
            p = self._parent(c)
            if self.heap[c] <= self.heap[p]:  # adhering to heap property
                break

            # Swap the nodes at parent, child indexes if they break max heap property
            self.heap[p], self.heap[c] = self.heap[c], self.heap[p]
            c = p

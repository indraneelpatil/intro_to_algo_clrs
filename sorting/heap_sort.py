#!/usr/bin/env python3

# Created by  Indraneel on 12/09/21

from numpy import inf
from heap_ds import BinaryHeapDS

class HeapSort(BinaryHeapDS):
    def __init__(self,input):
        super(HeapSort, self).__init__()
        self.result = []
        for i in input:
            self.heap_insert(i)
        self.print_data()
        self.run_sort_algorithm()
        self.print_result()

    def print_result(self):
        print(*self.result)

    def run_sort_algorithm(self):
        
        while(self.heap_size>0):
            self.result.append(self.heap_get_max())
            self.heap_pop()



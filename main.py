#!/usr/bin/env python3

# Created by  Indraneel on 2/09/21

from sorting.insertion_sort import InsertionSort
from sorting.selection_sort import SelectionSort
from sorting.merge_sort import MergeSort
from sorting.bubble_sort import BubbleSort
from sorting.heap_sort import HeapSort
from maximum_subarray import MaximumSubarray

from heap_ds import BinaryHeapDS

if __name__ == '__main__':
    data = [1,3,2,6,4,7,5]
    data = [1,2,3,4,5,6,7]
    data = [7,6,5,4,3,2,1]
    data = [10,11,7,10,6]
    #data = [-2,1,-3,4,-1,2,1,-5,4]
    HeapSort(data)
    #MaximumSubarray(data)

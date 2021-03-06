#!/usr/bin/env python3

# Created by  Indraneel on 2/09/21

from sorting.insertion_sort import InsertionSort
from sorting.selection_sort import SelectionSort
from sorting.merge_sort import MergeSort
from sorting.bubble_sort import BubbleSort
from sorting.heap_sort import HeapSort
from sorting.quick_sort import QuickSort
from maximum_subarray import MaximumSubarray
from selection_nth_element import SelectionNthElement

from heap_ds import BinaryHeapDS
from deque_ds import DequeDS

if __name__ == '__main__':
    data = [1,3,2,6,4,7,5]
    data = [1,2,3,4,5,6,7]
    #data = [7,6,5,4,3,2,1]
    #data = [10,11,7,10,6]
    #data = [2,2,2,2,2,2,2]
    #data = [-2,1,-3,4,-1,2,1,-5,4]
    #SelectionNthElement(data,5)
    #MaximumSubarray(data)
    deque_obj = DequeDS(10)
    deque_obj.insertLast(5)
    deque_obj.insertLast(6)
    deque_obj.insertLast(7)
    deque_obj.insertLast(8)
    deque_obj.insertLast(5)
    deque_obj.deleteLast()
    print(deque_obj.getLast())
    print("**")
    deque_obj.print_data()

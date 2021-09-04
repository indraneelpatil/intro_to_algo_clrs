#!/usr/bin/env python3

# Created by  Indraneel on 2/09/21

from insertion_sort import InsertionSort
from selection_sort import SelectionSort
from merge_sort import MergeSort
from bubble_sort import BubbleSort

if __name__ == '__main__':
    data = [1,3,2,6,4,7,5]
    data = [1,2,3,4,5,6,7]
    data = [7,6,5,4,3,2,1]
    testSort = BubbleSort(data)
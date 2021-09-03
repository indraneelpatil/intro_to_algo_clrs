#!/usr/bin/env python3

# Created by  Indraneel on 3/09/21

from numpy import inf

class SelectionSort:
    def __init__(self,input):
        self.data = input
        self.print_data()
        self.run_reverse_sort_algorithm()
        self.print_data()

    def print_data(self):
        print(*self.data)

    def run_sort_algorithm(self):
        
        
        for i in range(len(self.data)-1):
            min_element = inf
            min_element_ind = -1
            for j in range(i,len(self.data)):
                #print(j)
                min_element = min(self.data[j],min_element)
                min_element_ind = j if self.data[j] == min_element else min_element_ind 

            # Assign min element to iteration index
            temp = self.data[i]
            self.data[i] = min_element
            self.data[min_element_ind] = temp

    
    def run_reverse_sort_algorithm(self):
        
        for i in range(len(self.data)-1):
            max_element = -inf
            max_element_ind = -1
            for j in range(i,len(self.data)):
                #print(j)
                max_element = max(self.data[j],max_element)
                max_element_ind = j if self.data[j] == max_element else max_element_ind 

            # Assign min element to iteration index
            temp = self.data[i]
            self.data[i] = max_element
            self.data[max_element_ind] = temp


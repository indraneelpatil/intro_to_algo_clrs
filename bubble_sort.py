#!/usr/bin/env python3

# Created by  Indraneel on 5/09/21

from numpy import inf

class BubbleSort:
    def __init__(self,input):
        self.data = input
        self.print_data()
        self.run_optimized_bubble_sort()
        self.print_data()

    def print_data(self):
        print(*self.data)

    def run_optimized_bubble_sort(self):
        i=0
        
        while(i<len(self.data)-1):
            print(i)
            j=len(self.data)-1
            last_bubble_swap = len(self.data)-1
            while(j>i):
                if(self.data[j]<self.data[j-1]):
                    # Exchange
                    temp=self.data[j-1]
                    self.data[j-1] = self.data[j]
                    self.data[j] = temp
                    last_bubble_swap=j-1
                j=j-1
            i = last_bubble_swap
            i=i+1

    def run_sort_algorithm(self):
        
        for i in range(len(self.data)-1):
            j=len(self.data)-1
            while(j>i):
                if(self.data[j]<self.data[j-1]):
                    # Exchange
                    temp=self.data[j-1]
                    self.data[j-1] = self.data[j]
                    self.data[j] = temp
                j=j-1

    
    def run_reverse_sort_algorithm(self):
        
         for i in range(len(self.data)-1):
            j=len(self.data)-1
            while(j>i):
                if(self.data[j]>self.data[j-1]):
                    #Exchange
                    temp=self.data[j-1]
                    self.data[j-1] = self.data[j]
                    self.data[j] = temp
                j=j-1

    def run_recursive_sort_algorithm(self):

        self.data = self.sort_and_add(self.data)
    
    def sort_and_add(self,input):
        if(len(input)>1):

            min_val = self.get_minimum(input)
            input.remove(min_val)

            return [min_val] + self.sort_and_add(input)
        else:
            return input

    def get_minimum(self,input_list):
        min_val = inf
        for i in range(len(input_list)):
            if(input_list[i]<min_val):
                min_val = input_list[i]

        return min_val

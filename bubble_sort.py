#!/usr/bin/env python3

# Created by  Indraneel on 5/09/21

from numpy import inf

class BubbleSort:
    def __init__(self,input):
        self.data = input
        self.print_data()
        self.run_sort_algorithm()
        self.print_data()

    def print_data(self):
        print(*self.data)

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


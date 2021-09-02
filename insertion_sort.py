#!/usr/bin/env python3

# Created by  Indraneel on 2/09/21

class InsertionSort:
    def __init__(self,input):
        self.data = input
        self.print_data()
        self.run_sort_algorithm()
        self.print_data()

    def print_data(self):
        print(*self.data)

    def run_sort_algorithm(self):
        
        for i in range(1,len(self.data)):
            key = self.data[i]
            j=i-1
        
            while(self.data[j]>key and j>=0):
                self.data[j+1]=self.data[j]
                j=j-1

            j=j+1
            self.data[j]=key


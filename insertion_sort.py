#!/usr/bin/env python3

# Created by  Indraneel on 2/09/21

class InsertionSort:
    def __init__(self,input):
        self.data = input
        self.print_data()
        self.run_recursive_sort_algorithm()
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
    
    def run_reverse_sort_algorithm(self):
        
        for i in range(1,len(self.data)):
            key = self.data[i]
            j=i-1
        
            while(self.data[j]<key and j>=0):
                self.data[j+1]=self.data[j]
                j=j-1

            j=j+1
            self.data[j]=key

    def run_recursive_sort_algorithm(self):

        self.data = self.sort_and_insert(self.data)

    def sort_and_insert(self,input):

        if(len(input)>1):
            sorted_list = self.sort_and_insert(input[:len(input)-1])

            return self.insert_key(sorted_list,input[-1])

        else:
            return input
    
    def insert_key(self,sorted_list,key):
        dummy = 0
        sorted_list.append(dummy)
        j=len(sorted_list)-2
        while(sorted_list[j]>key and j>=0):
        
            sorted_list[j+1] = sorted_list[j]
            j=j-1

        j=j+1
        sorted_list[j] = key
        return sorted_list






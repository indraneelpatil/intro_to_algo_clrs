#!/usr/bin/env python3

# Created by  Indraneel on 12/09/21

from numpy import inf
import random

class QuickSort:
    def __init__(self,input):
        self.data = input
        self.print_data()
        self.run_randomised_sort_algorithm()
        self.print_data()

    def print_data(self):
        print(*self.data)

    def run_sort_algorithm(self):
        self.quick_sort_recursive(0,len(self.data)-1)    
        
    def quick_sort_recursive(self,left_ptr,right_ptr):
        if(left_ptr<right_ptr):
            divider_ptr = self.quick_sort_partition(left_ptr,right_ptr)
            self.quick_sort_recursive(left_ptr,divider_ptr-1)
            self.quick_sort_recursive(divider_ptr+1,right_ptr)

    def run_randomised_sort_algorithm(self):
        self.quick_randomised_sort_recursive(0,len(self.data)-1)    
        
    def quick_randomised_sort_recursive(self,left_ptr,right_ptr):
        if(left_ptr<right_ptr):
            # Generate random index
            rand_ind = random.randint(left_ptr,right_ptr)

            # Exchange this index with pivot
            temp = self.data[right_ptr]
            self.data[right_ptr] = self.data[rand_ind]
            self.data[rand_ind] = temp

            # Call partition
            divider_ptr = self.quick_sort_partition(left_ptr,right_ptr)
            self.quick_sort_recursive(left_ptr,divider_ptr-1)
            self.quick_sort_recursive(divider_ptr+1,right_ptr)
    
    def quick_sort_partition(self,left_ptr,right_ptr):

        pivot = self.data[right_ptr]
        divider_ptr = left_ptr-1 # Initially empty

        for it_ptr in range(left_ptr,right_ptr):
            if(self.data[it_ptr]<=pivot):
                divider_ptr = divider_ptr+1
                temp = self.data[divider_ptr]
                self.data[divider_ptr] = self.data[it_ptr]
                self.data[it_ptr]=temp
            else:
                # Dont do anything already in order
                pass
        
        # Put pivot in the middle
        temp = self.data[divider_ptr+1]
        self.data[divider_ptr+1] = pivot
        self.data[right_ptr] = temp

        return divider_ptr+1

    def quick_sort_partition_reverse(self,left_ptr,right_ptr):

        pivot = self.data[right_ptr]
        divider_ptr = left_ptr-1 # Initially empty

        for it_ptr in range(left_ptr,right_ptr):
            if(self.data[it_ptr]>=pivot):
                divider_ptr = divider_ptr+1
                temp = self.data[divider_ptr]
                self.data[divider_ptr] = self.data[it_ptr]
                self.data[it_ptr]=temp
            else:
                # Dont do anything already in order
                pass
        
        # Put pivot in the middle
        temp = self.data[divider_ptr+1]
        self.data[divider_ptr+1] = pivot
        self.data[right_ptr] = temp

        return divider_ptr+1


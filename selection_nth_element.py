#!/usr/bin/env python3

# Created by  Indraneel on 14/09/21

from numpy import inf
import random

class SelectionNthElement:
    def __init__(self,input,n):
        self.data = input
        self.n = n
        self.print_data()
        self.run_randomised_select_algo()
        self.print_data()

    def print_data(self):
        print(*self.data)

    def run_randomised_select_algo(self):
        
        if(n<len(self.data)):
            result = self.randomised_select(0,len(self.data)-1)
            print(result)
        else:
            print("Invalid inputs!")
        
    
    def randomised_select(left_ptr,right_ptr):

        if(left_ptr==right_ptr)
            return self.data[left_ptr]
        
        # Generate random index
        rand_ind = random.randint(left_ptr,right_ptr)

        # Exchange this index with pivot
        temp = self.data[right_ptr]
        self.data[right_ptr] = self.data[rand_ind]
        self.data[rand_ind] = temp

        divider_ptr = self.quick_sort_partition(left_ptr,right_ptr)
        if(self.n == divider_ptr):
            return self.data[divider_ptr]
        elif(self.n<divider_ptr):
            self.randomised_select(left_ptr,divider_ptr-1)
        else:
            self.randomised_select(divider_ptr+1,right_ptr)
    
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


'''
    
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

'''

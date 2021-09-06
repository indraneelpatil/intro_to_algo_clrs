#!/usr/bin/env python3

# Created by  Indraneel on 5/09/21

class MergeSort:
    def __init__(self,input):
        self.data = input
        self.print_data()
        self.run_sort_algorithm()
        self.print_data()

    def print_data(self):
        print(*self.data)

    def run_sort_algorithm(self):

        self.data = self.merge_sort(self.data)

    def merge_sort(self,input_data):
        if(len(input_data)>1):
            mid_ind = int(len(input_data)/2 if len(input_data)%2==0 else (len(input_data)-1)/2)
            first_half = self.merge_sort(input_data[:mid_ind])
            second_half = self.merge_sort(input_data[mid_ind:])
            
            return self.merge(first_half,second_half)
        else:
            return input_data

    def merge(self,list_one,list_two):

        #print("{} {} ^^^".format(list_one,list_two))

        merged_list = []
        while(len(list_one)>0 and len(list_two)>0):
            if(list_one[0]<list_two[0]):
                merged_list.append(list_one[0])
                list_one = list_one[1:]
            else:
                merged_list.append(list_two[0])
                list_two = list_two[1:]

        merged_list +=list_one
        merged_list +=list_two
        
        return merged_list
    
    def merge_reverse(self,list_one,list_two):

        #print("{} {} ^^^".format(list_one,list_two))

        merged_list = []
        while(len(list_one)>0 and len(list_two)>0):
            if(list_one[0]>list_two[0]):
                merged_list.append(list_one[0])
                list_one = list_one[1:]
            else:
                merged_list.append(list_two[0])
                list_two = list_two[1:]
            

        merged_list +=list_one
        merged_list +=list_two
        return merged_list


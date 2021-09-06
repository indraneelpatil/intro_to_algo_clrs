#!/usr/bin/env python3

# Created by  Indraneel on 6/09/21

from numpy import inf

class MaximumSubarray:
    def __init__(self,input):
        self.data = input
        self.print_data()
        self.run_brute_force_algorithm()
        self.run_divide_and_conquer_algo()
        self.run_kadanes_algorithm()

    def print_data(self):
        print(*self.data)

    def run_brute_force_algorithm(self):
        
        result = [0,0]
        max_profit = -inf
        # All possible buying dates
        for i in range(len(self.data)-1):
            #All possible selling dates
            for j in range(i+1,len(self.data)):

                profit = self.data[j]-self.data[i]
                if(profit>max_profit):
                    max_profit = profit
                    result[0] = i
                    result[1] = j
        
        print(result)

    def run_divide_and_conquer_algo(self):

        diff_array = []
        for i in range(len(self.data)-1):
            diff_array.append(self.data[i+1]-self.data[i])

    def run_kadanes_algorithm(self):

        diff_array = []
        for i in range(len(self.data)-1):
            diff_array.append(self.data[i+1]-self.data[i])

        current_running_sum = 0
        start_ind = 0
        max_sum = 0
        max_ind = [0,0]
        for i in range(len(diff_array)):
            current_running_sum = current_running_sum + diff_array[i]
            #print(current_running_sum)
            if(current_running_sum<0):
                current_running_sum = 0
                start_ind = i+1
            else:
                if(current_running_sum>max_sum):
                    max_sum = current_running_sum
                    max_ind[0]=start_ind
                    max_ind[1]=i
        max_ind[1] = max_ind[1]+1
        print(max_ind)


                

    



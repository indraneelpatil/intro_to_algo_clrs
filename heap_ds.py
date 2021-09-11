#!/usr/bin/env python3

# Created by  Indraneel on 11/09/21

from numpy import inf

class BinaryHeapDS:
    def __init__(self,heap_type='max'):

        # Binary heap as a list
        self.data = []
        self.type = heap_type
        self.print_data()
        self.heap_size = len(self.data)

    def print_data(self):
        print(*self.data)

    def node_parent(self,ind):
        return (int)(ind/2)

    def node_left(self,ind):
        if(2*ind<self.heap_size):
            return 2*ind
        else:
            return -1

    def node_right(self,ind):
        if(2*ind+1<self.heap_size):
            return 2*ind + 1
        else:
            return -1


    def heap_insert(self,element):

        self.data.append(element)
        self.heap_size = len(self.data)

        if(self.heap_size>1):
        
            ind = self.heap_size-1
            while(ind>=0 and self.data[self.node_parent(ind)]<self.data[ind]):
                temp = self.data[self.node_parent(ind)]
                self.data[self.node_parent(ind)] = self.data[ind]
                self.data[ind] = temp
                ind = self.node_parent(ind)
        self.print_data()

    def heap_get_max(self):

        if(self.heap_size>0):
            return self.data[0]
        else:
            return -1

    
    def heap_pop(self):

        if(self.heap_size>0):
            self.data = self.data[1:]
            self.heap_size = self.heap_size -1
            self.heapify(0)

    def heapify(self,ind):
        l = self.node_left(ind)
        r = self.node_right(ind)

        largest = ind

        if(l>0 and self.data[largest]<self.data[l]):
            largest = l

        if(r>0 and self.data[largest]<self.data[r]):
            largest = r

        if(largest!=ind):
            temp = self.data[ind]
            self.data[ind] = self.data[largest]
            self.data[largest] = temp
            self.heapify(largest)



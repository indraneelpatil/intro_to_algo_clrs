#!/usr/bin/env python3

# Created by  Indraneel on 21/09/21

from numpy import inf
import array as arr

class DequeDS:
    def __init__(self,max_size):

        # Binary heap as a list
        self.data = arr.array('i',[0]*max_size)
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.print_data()
        #self.heap_size = len(self.data)

    def print_data(self):
        i = self.head
        while(i!=self.tail):
            print(self.data[i])
            i=self.inc_index(i)

    def inc_index(self,ind):
        return (ind+1)%self.max_size

    def dec_index(self,ind):
        return ((ind-1)+self.max_size)%self.max_size

    def insertLast(self,element):
        if(self.inc_index(self.tail)==self.head):
            raise 'Deque Overflow'
        
        self.data[self.tail] = element
        self.tail = self.tail+1
        

    def deleteLast(self):
        if(self.head == self.tail):
            raise 'Deque Underflow'

        self.tail = self.dec_index(self.tail)

    def insertFront(self,element):
        if(self.dec_index(self.head)==self.tail):
            raise 'Deque Overflow'

        self.head = self.dec_index(self.head)
        self.data[self.head] = element

    def deleteFront(self):
        if(self.head == self.tail):
            raise 'Deque Underflow'
        
        self.head = self.inc_index(self.head)

    def getFront(self):
        if(self.head == self.tail):
            raise 'Deque empty'

        return self.data[self.head]

    def getLast(self):
        if(self.head == self.tail):
            raise 'Deque empty'

        return self.data[self.dec_index(self.tail)]

   


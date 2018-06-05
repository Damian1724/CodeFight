/*
Author: Damian Cruz
source: CodeFight (https://codefights.com)
problem name:InterviewPractice>LinkedList>removeKfromlist
problem url: https://codefights.com/interview-practice/task/gX7NXPBrYThXZuanm
cost of algorithm: N
*/


# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    if l is None:return l
    if l.value ==k:
        while l.next is not None and l.next.value == k:
            l=l.next
        l=l.next
    pointer=l
    if l is not None:
        aux=l
        while aux.next is not None:
            if aux.next.value == k:
                while aux.next is not None and aux.next.value ==k:
                    aux=aux.next
            aux=aux.next
            l.next=aux
            l=l.next
            if aux is None:break
    return pointer
        
    

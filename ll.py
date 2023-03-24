
import numpy as np

# so wake me up when its all over 
#  when im wiser and im older
# arr=[2,5,7,1,4,0,3,6]

# y=max(arr)
# res = [[] for i in range(len(arr))]
# k=0
# for i in arr:
#     if i<0:
#         raise TypeError('Value can not be less than 0')
#     for j in range(i):
#         res[k].append("*")
#     k+=1
# for i in range(len(arr)):
#     print(*res[i])

# print(res)

# from matplotlib import pyplot

# # plt=pyplot.plot(arr,(0,9))
# pyplot.hist(arr)
# pyplot.show()

# class Node:
#     def __init__(self, value, next = None) -> None:
#         self.value = value
#         self.next =next

# class LinkedList:
#     def __init__(self) -> None:
#         self.head= None

#     def append(self, value):
#         if self.head is None:
#             self.head = Node(value)
#         else:
#             current = self.head
#             while current.next is not None:
#                 current=current.next
#             current.next = Node(value)

#     def show(self):
#         current = self.head
#         if current is None:
#             return None
#         while current is not None:
#             print(current.value, end=" => ")
#             current=current.next
    
#     def insertatFirst(self, value):
#         current = self.head
#         temp= Node(value)
#         temp.next=current
#         self.head=temp

#     def findMiddle(self):
#         count = 0
#         current = self.head
#         while current is not None:
#             current=current.next
#             count+=1
#         return count//2

#     def MiddleElement(self):
#         index = self.findMiddle()
#         current = self.head
#         count = 0
#         while count!=index:
#             current=current.next
#             count+=1
#         return current.value
    
#     def insertatMiddle(self, value):
#         pass

#     def floyd(self):
#         fast= self.head
#         slow = self.head

#         while fast is not None and fast.next is not None:
#             slow = slow.next
#             fast = fast.next.next
#         return slow.value   

#     def reverse(self):
#         prev = None
#         current = self.head
#         while current is not None:
#             next = current.next
#             current.next = prev
#             prev=current
#             current=next
#         self.head=prev

#     def findLength(self):
#         current = self.head
#         count = 0
#         while current is not None:
#             current = current.next
#             count+=1
#         return count

#     def dequeue(self, index=0):
#         if index == -1:
#             index=self.findLength()-1
#         current = self.head
#         if index>self.findLength():
#             print('Invalid Index')
#             return
#         if index == 0:
#             self.head = self.head.next
#         currentIndex = 0
#         while currentIndex<index-1:
#             current= current.next
#             currentIndex+=1
#         current.next=current.next.next

#     def reverse2(self, left, right):
#         current = self.head
#         count = 0
#         prev=None
#         if current is None:
#             return None
#         while count!=left:
#             prev=current
#             current=current.next
#             count+=1

#         while count!=right:
#             # print(current.value, end="=>")
#             next = current.next
#             current.next = prev
#             prev=current
#             current=next
#             count+=1
        # while count!=right:
        #     next = current.next
        #     current.next = prev
        #     prev = current
        #     current = next
        #     count+=1
        # self.head=prev


        





# list1 = LinkedList()
# list2 = LinkedList()

# l1=[9,5,4,2,1,3]
# l2=[5,7,4,1,2,3,0,1]

# for i in l1:
#     list1.append(i)

# for i in l2:
#     list2.append(i)
# list1.reverse()
# list2.reverse()
# list1.show()
# print()
# list2.show()

# def createNumber(lists):
#     current = lists.head
#     result = []
#     while current is not None:
#         result.append(current.value)
#         current=current.next
#     return int("".join(list(map(str,result))))


# sumofList=[int(i) for i in str(createNumber(list1)+createNumber(list2))[::-1]]
# newList = LinkedList()
# for i in sumofList:
#     newList.append(i)

# newList.show()




# list1.show()
# print("Middle Element is: ",list1.floyd())



# from math import ceil

# piles = []
# if not piles:
#     exit(0)
# k = 2
# piles.sort()
# piles=piles[::-1]
# i=0
# while k>0:
#     piles[i]=ceil(piles[i]/2)
#     if len(piles)>1 and piles[i+1]>=piles[i]:
#         i+=1
#     k-=1
# print(sum(piles))

# word='Google'
# word='leetcode'
# word='g'
# def detectCapitalUse(word: str) -> bool:
#     if len(word)==1:
#         return True
#     if word[0].islower():
#         if word[1:].islower():
#             return True
#         else:
#             return False
#     if word[0].isupper():
#         if word[1:].isupper() or word[1:].islower():
#             return True
#         else:
#             return False
# # print(word.islower())
# print(detectCapitalUse(word))
def maximum(arr:list):
    temp=float('-inf')
    for i in arr:
        if i>temp:
            temp=i
    return temp

arr=[[-1,5,4,3,2],[5,-1,5,4,2],[7,2,554,5,2],[5,2,6,9,-1]]
# for i in arr:
#     for j in range(len(arr)):
#         if i[j]==-1:
#             i[j]=maximum(i)
# print(arr)

arr=np.array(arr)
print(arr)
arr=arr.T
arr=arr.tolist()
for i in arr:
    for j in range(len(i)):
        if i[j]==-1:
            i[j]=max(i)
arr=np.array(arr)
arr=arr.T
print()
print(arr)
# class Matrix:
#     def __init__(self, mat: list) -> None:
#         self.mat=mat
    
#     # def maxColumn(self):
#     #     temp=[]
#     #     for i in range(len(max(self.mat))):
#     #         temp=[i for ]
#     #         if self.mat[i][0]==-1:
#     #             self.mat[i][0]=max([i for i in self.mat[]])
        
    
#     def __repr__(self):
#         for i in self.mat:
#             for j in range(len(self.mat)):
#                 print(i[j], end=" | ")
#             print()
#         return ""
    
#     def __str__(self) -> str:
#         return self.__repr__()

# mat1=Matrix(arr)
# print(mat1)


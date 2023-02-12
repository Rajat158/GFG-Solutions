'''
You are given the head of a linked list. You have to replace all the values of the nodes with the nearest prime number. If more than one prime number exists at an equal distance, choose the smallest one.

Example 1:

Input:
2 → 6 → 10
Output:
2 → 5 → 11
Explanation:
The nearest prime of 2 is 2 itself.
The nearest primes of 6 are 5 and 7,
since 5 is smaller so, 5 will be chosen.
The nearest prime of 10 is 11.
 

Example 2:

Input:
1 → 15 → 20
Output:
2 → 13 → 19
Explanation:
The nearest prime of 1 is 2.
The nearest primes of 15 are 13 and 17,
since 13 is smaller so, 13 will be chosen.
The nearest prime of 20 is 19.
Your Task:
The task is to complete the function primeList() which contains a reference to the head as the only argument. This function should return the head of the modified linked list.

Expected Time Complexity: O(number of nodes * sqrt(value of node)).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ Number of Nodes ≤ 104
1 ≤ Value on Node ≤ 104
'''
from typing import Optional

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

You can also use the following for printing the link list.
printList(node)
"""
class Solution:
    def primeList(self, head : Optional['Node']) -> Optional['Node']:
        # code here
        mat = [True]*(100001)
        i= 2
        mat[1]=False
        mat[0]=False
    
        while i*i<=len(mat):
            if mat[i]:
                for j in range(i*i,len(mat)+1,i):
                    try:
                        mat[j]=False
                    except:
                        continue
        
            i+=1
      
        temp = head
        while temp:
            val = temp.data
            if mat[val]:
                temp=temp.next
            
            else:
                i=val
              
                while mat[i]!=True:
                    i-=1
                diff = abs(val-i)
                j = val
                
                while mat[j]!=True:
                    j+=1
            
                diff1=abs(val-j)
              
                if diff1>=diff:
                    temp.data = i
                else:
                    temp.data=j
                temp=temp.next
        return head
                    

'''
You are given two arrays A and B each of length N. You can perform the following operation on array A zero or more times. 

Select any two indices i and j, 1 <= i , j <= N and i != j
Set A[i] = A[i] + 2 and A[j] = A[j]-2
Find the minimum number of operations required to make A and B equal.

Note :

Two arrays are said to be equal if the frequency of each element is equal in both of them.
Arrays may contain duplicate elements.
Example 1:

Input:
N = 3
A[] = {2, 5, 6}
B[] = {1, 2, 10}
Output: 2
Explanation: 
Select i = 3, j = 2, A[3] = 6 + 2 = 8 and A[2] = 5 - 2 = 3
Select i = 3, j = 2, A[3] = 10 - 2 = 8 and A[2] = 3 - 2 = 1
Now A = {2, 1, 10} and B = {1, 2, 10}
Example 2:

Input:
N = 2
A[] = {3, 3}
B[] = {9, 8}
Output: -1
Explanation: 
It can be shown that A cannot be made equal to B.
Your Task: 
You don't need to read input or print anything. Your task is to complete the function solve() which takes the 2 arrays A[], B[] and their size N as
input parameters and returns the minimum number of moves to make A and B equal if possible else return -1.

Expected Time Complexity: O(NlogN)
Expected Auxiliary Space: O(N)

Constraints:
1 <= N <= 105
-109 <= A[i] <= 109
-109 <= B[i] <= 109

 
'''
from typing import List
from collections import defaultdict

class Solution:
    def solve(self, N: int, A: List[int], B: List[int]) -> int:
        A.sort()
        B.sort()
        evens_A, odds_A = [], []
        evens_B, odds_B = [], []
        sum_A, sum_B = sum(A), sum(B)
        
        for ele_A, ele_B in zip(A, B):
            if ele_A & 1:
                odds_A.append(ele_A)
            else:
                evens_A.append(ele_A)
            
            if ele_B & 1:
                odds_B.append(ele_B)
            else:
                evens_B.append(ele_B)
        
        if sum_A != sum_B or len(evens_A) != len(evens_B):
            return -1
        
        ops = 0
        for ea, eb in zip(evens_A, evens_B):
            ops += abs(ea - eb) >> 1
        for oa, ob in zip(odds_A, odds_B):
            ops += abs(oa - ob) >> 1
        
        return ops >> 1

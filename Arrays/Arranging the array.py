'''
You are given an array of size N. Rearrange the given array in-place such that all the negative numbers occur before all non-nagative numbers.(Maintain the order of all -ve and non-negative numbers as given in the original array).
Example 1:

Input:
N = 4
Arr[] = {-3, 3, -2, 2}
Output:
-3 -2 3 2
Explanation:
In the given array, negative numbers
are -3, -2 and non-negative numbers are 3, 2. 
Example 1:

Input:
N = 4
Arr[] = {-3, 1, 0, -2}
Output:
-3 -2 1 0
Explanation:
In the given array, negative numbers
are -3, -2 and non-negative numbers are 1, 0.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function Rearrange() which takes the array Arr[] and its size N as inputs and returns the array after rearranging with spaces between the elements of the array.
Expected Time Complexity: O(N. Log(N))
Expected Auxiliary Space: O(Log(N))

Constraints:
1 ≤ N ≤ 105
-109 ≤ Elements of array ≤ 109
'''

from typing import List


class Solution:
    def Rearrange(self, n : int, A : List[int]) -> None:
        def _solve(L, R)->int:
            if R-L<=0: return 1 if A[L]<0 else 0
            M = (L+R)//2
            L0, R0 = _solve(L, M), _solve(M+1, R)
            if (M-L+1)>L0 and R0 > 0:
                A[L+L0:M+1] = reversed(A[L+L0:M+1])
                A[M+1:M+1+R0]  = reversed(A[M+1:M+1+R0])
                A[L+L0:M+1+R0] = reversed(A[L+L0:M+1+R0])
            return L0+R0

        _solve(0, n-1)

'''
You are given an array A of N integers and an integer K, and your task is to find the total number of cuts that you can make such that for each cut these two conditions are satisfied
1. A cut divides an array into two parts equal or unequal length (non-zero).
2. Sum of the largest element in the left part and the smallest element in the right part is greater than or equal to K.

Example 1:

Input:
N=3
K=3
A[]={1,2,3}
Output:
2
Explanation:
Two ways in which array is divided to satisfy above conditions are:
{1} and {2,3} -> 1+2>=3(satisfies the condition)
{1,2} and {3} -> 2+3>=3(satisfies the condition)
Example 2:

Input:
N=5
K=5
A[]={1,2,3,4,5}
Output:
3
Explanation:
{1,2} and {3,4,5} -> 2+3>=5
{1,2,3} and {4,5} -> 3+4>=5
{1,2,3,4} and {5} -> 4+5>=5
Your Task:
You don't need to read input or print anything. Your task is to complete the function totalCuts() which takes two integers N, K, and an array A of size N as input parameters, and returns an integer representing the total number of cuts that satisfy both conditions.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 <= N <= 10^6
0 <= K <= 10^6
0 <= A[i] <= 10^6
'''
from typing import List
class Solution:
    def totalCuts(self, N : int, K : int, A : List[int]) -> int:
        left = []
        right = [0]*N
        left.append(A[0])
        mx = A[0]
        for i in range(1,N):
            if A[i]>mx:
                mx = A[i]
                left.append(mx)
            else:
                left.append(mx)
        right[-1] = A[-1]
        mi = A[-1]
        
        for i in range(N-2, -1, -1):
            if mi > A[i]:
                mi = A[i]
                right[i] = mi
            else:
                right[i] = mi
        count = 0
        
        for i in range(N-1):
            a = left[i]
            b = right[i+1]
            if a + b >= K:
                count += 1
        return count


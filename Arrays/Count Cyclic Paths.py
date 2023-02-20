'''
Given a triangular pyramid with its vertices marked as O, A, B and C and a number N, the task is to find the number of ways such that a person starting from the origin O initially, reaches back to the origin in N steps. In a single step, a person can go to any of its adjacent vertices.

Lightbox


Example 1:

Input:
N = 1
Output: 0
Explanation: The minimum length of
a cyclic path is 2.
Example 2:

Input:
N = 2
Output: 3
Explanation: The three paths are :
O-A-O, O-B-O, O-C-O

Your Task:  
You don't need to read input or print anything. Your task is to complete the function countPaths() which takes an integer N as input parameter and returns the number of possible paths. Since the answer may be big, return it modulo (10^9+7). 


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N ≤ 106
'''
#User function Template for python3

class Solution:

    def countPaths (self, N):

        if N==1:

            return 0

        mod = 10**9+7

        

        t1=1

        t2=0

        

        for i in range(2,N):

            t2, t1 = t1, (2*t1 + 3*t2)%mod

        ans = (3*t1)%mod

        

        return ans
        

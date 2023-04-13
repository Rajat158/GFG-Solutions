'''
Given an array A[] of N integers. The task is to partition the array into four non-empty contiguous subarrays P, Q, R, and S such that each element
of the array A[] should be present in any subarray.
Let W, X, Y, and Z be the sum of the elements in P, Q, R, and S respectively.
Find the smallest absolute difference between the maximum and the minimum among W, X, Y, and Z.

Example 1:

Input:
N = 5
A[] = [4,2,2,5,1]
Output: 4
Explanation: let partition the array 
P,Q,R,S = [4],[2,2],[5],[1]
W = 4, X = 4, Y = 5, Z = 1 
Differnce = max(W,X,Y,Z)-min(W,X,Y,Z)= 5-1 = 4 
Example 2:

Input:
N = 4
A[] = {4,4,4,4}
Output: 0
Explanation: 
There is only one way to partition 
the array. P,Q,R,S = [4],[4],[4],[4]
Your Task:
You don't need to read input or print anything. The task is to complete the function minDifference() which takes the integer N and the array A[] 
as inputs and returns the smallest absolute difference.

Expected Time Complexity: O(NLogN)
Expected Auxiliary Space: O(N)

Constraints:
4 < N < 105
1 < A[i] < 109
'''
#User function Template for python3
class Solution:
    def minDifference(self, N, A): 
        def _split(L, R):
            LSUM = (acc[L-1] if L > 0 else 0)
            tot = acc[R] - LSUM
            goal = tot//2
            while L<R:
                m = (L+R)//2
                if acc[m] - LSUM < goal: L=m+1
                else: R=m
            v1, v2 = acc[L]-LSUM, tot-(acc[L]-LSUM)
            if L>0:
                v3, v4 = acc[L-1]-LSUM, tot-(acc[L-1]-LSUM)
                if abs(v2-v1) > abs(v4-v3): return (v3,v4)
            return (v1,v2) 
        
        from itertools import accumulate
        acc = list(accumulate(A))
        ans = 10**9
        for i in range(1, N-2):
            W, X = _split(0, i)
            Y, Z = _split(i+1, N-1)
            vs = sorted((W,X,Y,Z))
            ans = min( ans, vs[3]-vs[0] )
        return ans


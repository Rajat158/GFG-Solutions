'''
Given an array A[] of N integers and an integer M. The task is to count the number of subarrays which have median M.
Median of an array is defined as below:

1. If N is odd, the median value is the number that is in the middle after sorting the array.
2. if N is even, the median value is the left of the two middle numbers after sorting the array. 

Example 1:

Input:
N = 5, M = 2
A[] = {2, 1, 3, 5, 4}
Output: 
3
Explanation: 
The subarrays which has median equal to M
are [2], [2,1,3] and [2,1,3,5]

Example 2:

Input:
N = 1, M = 1
A[] = {1}
Output: 
1
Explanation: 
The subarrays which has median equal to M
is [1].

Your Task: 
You don't need to read input or print anything. Complete the function countSubarray( ) which takes the integer N , the array A[], and the integer
M as input parameters and returns the number of subarays. 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 105
1 ≤ A[] ≤ 105
1 ≤ M ≤ N
'''
#User function Template for python3
class Solution:
    def countSubarray(self, N, A, M): 
        # code here
        def fn( n, A, m):
            mp = [0]*(2*n+1)
            cur,tot,ans = n, 0, 0
            mp[cur]+=1
            
            for i in range(n) :
                x = -1
                if (A[i] >= m) :
                    x = 1
                if (x == -1) :
                    tot -= mp[(cur+x)]
                else :
                    tot += mp[cur]
                
                cur += x
                ans += tot
                mp[cur]+=1
                
            return ans
        
        return fn(N, A, M) - fn(N, A, M+1)

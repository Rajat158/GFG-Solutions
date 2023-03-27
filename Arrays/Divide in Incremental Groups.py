'''
Given two integers N and K, the task is to count the number of ways to divide N into K groups of positive integers such that their sum is N and the number
of elements in groups follows a non-decreasing order (i.e. group[i] <= group[i+1]).

Example 1:

Input:
N = 8
K = 4
Output:
5
Explanation:
There are 5 groups such that their sum is 8 
and the number of positive integers in each 
group is 4. The 5 groups are [1, 1, 1, 5], 
[1, 1, 2, 4], [1, 1, 3, 3], [1, 2, 2, 3] and 
[2, 2, 2, 2].
Example 2:

Input: 
N = 4
K = 3
Output:
1
Explanation: 
The only possible grouping is {1, 1, 2}. Hence,
the answer is 1 in this case.
Your Task:
Complete the function countWaystoDivide() which takes the integers N and K as the input parameters, and returns the number of ways to divide the sum N into K groups.

Expected Time Complexity: O(N2*K)
Expected Auxiliary Space: O(N2*K)

Constraints:
1 ≤ K ≤ N ≤ 100
'''
class Solution:
    def countWaystoDivide(self, N, K):
        # Code here
        a=[]
        for i in range(1,N+1):
            a.append(i)
        n=N
        k=K
        dp=[]
        for i in range(N+1):
            c=[]
            for j in range(N+1):
                d=[]
                for k in range(k+1):
                    d.append(-1)
                c.append(d)
            dp.append(c)
        def coin(i,su,a1):
            if(su==n):
                if(a1==k):
                    return 1
                else:
                    return 0
            if(su>n or i>=n or a1>k):
                return 0
            if(dp[i][su][a1]!=-1):
                return dp[i][su][a1]
            a3=coin(i,su+a[i],a1+1)
            a2=coin(i+1,su,a1)
            dp[i][su][a1]=(a3+a2)
            return dp[i][su][a1]
        return(coin(0,0,0))

'''
Given two numbers n and x, find out the total number of ways n can be expressed as the sum of the Xth power of unique natural numbers. As the total number of ways can be very large, so return the number of ways modulo 109 + 7. 

Example 1:

Input: 
n = 10, x = 2
Output: 
1 
Explanation: 
10 = 12 + 32, Hence total 1 possibility. 
Example 2:

Input: 
n = 100, x = 2
Output: 
3
Explanation: 
100 = 102 
62 + 82 and 12 + 32 + 42 + 52 + 72 
Hence total 3 possibilities. 
Your Task:  
You don't need to read input or print anything. Complete the function numOfWays() which takes n and x as input parameters and returns the total number of ways n can be expressed as the sum of xth power of unique natural numbers.

Expected Time Complexity: O(n2logn)
Expected Auxiliary Space: O(n)

Constraints:
1 <= n <= 103
1 <= x <= 5
'''
#User function Template for python3
class Solution:
	def numOfWays(self, n, x):
        powers = []
        for i in range(1, n+1):
            v = i**x
            if v > n:
                break
            powers.append(i**x)
        
        dp = [0]*(n+1)
        dp[0] = 1
        
        for c in powers:
            for j in range(n, c-1, -1):
                dp[j] += dp[j-c]
        return dp[n]%(10**9+7)

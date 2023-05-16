'''
Given a string s containing 0's and 1's. You have to return the smallest positive integer C, such that the binary string can be cut into C pieces and each piece should be of the power of 5  with no leading zeros.
Note: The string s is a binary string. And if no such cuts are possible, then return -1.

Example 1:

Input:
s = "101101101"
Output: 
3
Explanation: 
We can split the given string into 
three 101s, where 101 is the binary 
representation of 5.
Example 2:

Input:
s = "00000"
Output: 
-1
Explanation: 
0 is not a power of 5.
Your Task:
Your task is to complete the function cuts() which take a single argument(string s). You need not take any input or print anything. Return an int C if the cut is possible else return -1.

Expected Time Complexity: O(|s|*|s|*|s|).
Expected Auxiliary Space: O(|s|).

Constraints:
1<= |s| <=50
'''

class Solution:

    def cuts(self, s):
        
        def ok(ss):
            n = int(ss, 2)
            while n > 1 and n%5 == 0:
                n //= 5
            return n == 1
            
        n = len(s)
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        
        for i in range(n):
            for k in range(i, -1, -1):
                if s[k] != '0' and ok(s[k:i+1]):
                    dp[i+1] = min(dp[i+1], dp[k]+1)
        return dp[n] if dp[n] != float('inf') else -1

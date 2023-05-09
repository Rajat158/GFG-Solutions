'''
Given an integer N. Your task is to find the number of binary strings of length N having no consecutive 1s.
As the number can be large, return the answer modulo 10^9+7.

Example 1:

Input:
N = 3
Output:
5
Explanation:
All the binary strings of length 3 having
no consecutive 1s are "000", "001", "101",
"100" and "010".
Example 2:

Input: 
N = 2
Output:
3
Explanation: 
All the binary strings of length 2 having no 
consecutive 1s are "10", "00" and "01".
Your Task:
You dont need to read input or print anything. Complete the function countStrings() which takes the integer N as the input parameter, and returns the number of binary strings of length N with no consecutive 1s.

Expected Time Complexity: O(log(N))
Expected Auxiliary Space: O(Height of the recursive call stack)

Constraints:
1 ≤ N ≤ 1018
'''
class Solution:
    m=1000000007
    def f(self,n):
        if n==0:
            return 0,1;
        a,b=self.f(n//2)
        c=(a*(b*2-a))%self.m
        d=(a*a+b*b)%self.m
        if n%2==1:
            return d,c+d
        return c,d
        
    def countStrings(self, N): 
        # Code here
        ans,_= self.f(N+2)
        return ans%self.m

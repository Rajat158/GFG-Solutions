'''
Given a positive integer n, find the nth fibonacci number. Since the answer can be very large, return the answer modulo 1000000007.

Example 1:

Input: 
n = 2
Output: 
1 
Explanation: 
1 is the 2nd number of fibonacci series.
Example 2:

Input: 
n = 5
Output: 
5
Explanation: 
5 is the 5th number of fibonacci series.
Your Task:  
You dont need to read input or print anything. Complete the function nthFibonacci() which takes n as input parameter and returns nth fibonacci number.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1<= n <=105


'''
class Solution:
    def nthFibonacci(self, n: int) -> int:
        if n < 2:
            return n
        if n == 2:
            return 1
        a, b = 1, 1
        for i in range(2, n):
            temp = a
            a = (a + b) % 1000000007
            b = temp
        return a

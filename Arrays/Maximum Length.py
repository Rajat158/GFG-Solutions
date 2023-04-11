'''
Given the maximum occurrences of a, b, and c in a string. Your task is to make the string containing only a, b, and c such that no three consecutive 
characters are the same.

Example 1:

Input:
a = 3, b = 3, c = 3
Output: 
9
Explanation: 
No three consecutive character of
the string "abcabcabc" is same.
Example 2:

Input:
a = 11, b = 2, c = 2
Output: 
-1
Explanation: 
If we build a string of these character's,
the string will be"aabaacaabaacaaa", here
we can see that there will be three consecutive a. So
there is no solution exist.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function solve( ) which takes integers a, b, and c as input parameters and
returns the string length. If there is no possible answer return -1.

Expected Time Complexity: O(a+b+c)
Expected Auxiliary Space: O(1)

Constraints:
0 ≤ a, b, c ≤ 105
0 < (a + b + c) 
'''

class Solution():
    def solve(self, a, b, c):
        x=(b+c+1)*2
        if(a>x):
            return(-1)
        y=(a+c+1)*2
        if(b>y):
            return(-1)
        z=(a+b+1)*2
        if(c>z):
            return(-1)
        return(a+b+c)

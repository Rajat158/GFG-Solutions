'''
Given a number in its binary form find if the given binary number is a multiple of 3. It is recommended to finish the task using one traversal of input binary number.

Example 1:

Input: S = "0011"
Output: 1
Explanation: "0011" is 3, which is divisible by 3.
Example 2:

Input: S = "100"
Output: 0
Explanation: "100"'s decimal equivalent is 4, which is not divisible by 3.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function isDivisible() which takes the string s as inputs and returns 1 if the given number is divisible by 3 otherwise 0.

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ |S| ≤ 105
'''
from functools import reduce

class Solution:
    def isDivisible(self, s):
	    s = [int(i) for i in s]
	    res = reduce(lambda a, b: a*2+b, s)
	    return 1 if not res%3 else 0

'''
Given a string str, find the minimum characters to be added at front of the string to make it a palindrome.


Example 1:

Input:
str = ABCD
Output: 3
Explanation: The resultant string 
after adding 3 characters is DCBABCD.
The minimum possible answer is 3.
Example 2:

Input:
str = ABA
Output: 0
Explanation: The given string
is already a palindrome.

Your Task:  
You don't need to read input or print anything. Your task is to complete the function addMinChar() which takes the string str as input parameters and returns the minimum number of characters to be added to make it a palindrome.


Expected Time Complexity: O(|str|)
Expected Auxiliary Space: O(|str|)


Constraints:
1 ≤  |str| ≤ 105
str contains only uppercase english alphabets
'''
#User function Template for python3

class Solution:
    def addMinChar (self, str1):
        s = str1 + "@" + str1[::-1]
        n = len(s)
        p = [0]*(n+1)
        p[0] = -1
        for i in range(1, n+1):
            k = p[i-1]
            while k > 0 and s[k] != s[i-1]:
                k = p[k]
            p[i] = k+1
        return len(str1) - p[n]

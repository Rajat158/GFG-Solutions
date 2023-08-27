'''
You are given a string s. You need to reverse the string.

Example 1:

Input:
s = Geeks
Output: skeeG
Example 2:

Input:
s = for
Output: rof
Your Task:

You only need to complete the function reverseWord() that takes s as parameter and returns the reversed string.

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).

Constraints:
1 <= |s| <= 10000
'''
#User function Template for python3

class Solution:
    def reverseWord(self,s):
        i,n,s=0,len(s),list(s)
        while i<n//2:
            s[i],s[n-1-i]=s[n-1-i],s[i]
            i+=1
        return "".join(s)

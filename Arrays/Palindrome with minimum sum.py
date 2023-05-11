'''
Given a string, S.The string can contain small case English letters or '?'. You can replace '?' with any small English letter. Now if it is possible to make the string S a palindrome after replacing all '?' then find the palindromic string with a minimum ascii sum of the absolute difference of adjacent characters. Otherwise, return -1.

Example 1:

Input: S = a???c??c????
Output: 4
Explanation:
We can see that we can make the string
palindrome. Now to get minimum ascii sum we should
replace all the '?' between 'a' and 'c' with
'b' and all the '?' between two 'c' with 'c'.
So after replacing all the '?' the string: 
abbbccccbbba.
The sum of differences of adjacent characters is 4.   
Example 2:

Input: S = a???c??c???c
Output: -1
Explanation:
It is not possible to make the string palindrome.
Your Task:
You don't need to read input or print anything. Your task is to complete the function minimumSum() which takes a string S input parameter and returns an integer denoting the sum of differences of adjacent characters. If it is not possible to make string palindrome, return -1. 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= |S| <= 105
'''

import math
class Solution:
    def minimumSum(self, s : str) -> int:
        # code here
        i,j = 0,len(s)-1
        count = 0
        while(i<j):
            if s[i]!='?':count +=1
            if s[j]!='?':count +=1
            if s[i]!=s[j] and (s[j]!='?' and s[i]!='?'):
                return -1
            else:
                if s[i]!='?' and s[j]=='?':
                    s = s[:j]+s[i]+s[j+1:]
                elif s[i]=='?' and s[j]!='?':
                    s = s[:i]+s[j]+s[i+1:]
            i +=1
            j -=1
        l,ch,sum = len(s),'',0
        if count ==0 or count ==1:
            return 0

        for i in range(l):
            if s[i]!='?':
                ch = s[i]
                break
            
        for i in range(l):
            if s[i]!='?':
                ch = s[i]
            if s[i]=='?':
                if i <= l-2:
                    s = s[:i]+ch+s[i+1:]
                else:
                    s = s[:i]+ch
               
        for i in range(l-1):
            sum += abs(ord(s[i])-ord(s[i+1]))
        return sum 

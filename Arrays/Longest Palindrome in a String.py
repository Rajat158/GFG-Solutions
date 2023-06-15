'''
Given a string S, find the longest palindromic substring in S. Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S). Palindrome string: A string that reads the same backward. More formally, S is a palindrome if reverse(S) = S. In case of conflict, return the substring which occurs first ( with the least starting index).

Example 1:

Input:
S = "aaaabbaa"
Output: aabbaa
Explanation: The longest Palindromic
substring is "aabbaa".
Example 2:

Input: 
S = "abc"
Output: a
Explanation: "a", "b" and "c" are the 
longest palindromes with same length.
The result is the one with the least
starting index.
Your Task:
You don't need to read input or print anything. Your task is to complete the function longestPalin() which takes the string S as input and returns the longest palindromic substring of S.

Expected Time Complexity: O(|S|2).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ |S| ≤ 103
'''

class Solution:
    def longestPalin(self, S):
        # code here
        res=""
        s2=0
        if(S==S[::-1]):
            return (S)
        for i in range(len(S)):
            st=''
            s1=0
            for j in range(i,len(S)):
                st+=S[j]
                s1+=1
                if(st==st[::-1]):
                    if(s1>s2):
                        res=st
                        s2=s1
        return res
            

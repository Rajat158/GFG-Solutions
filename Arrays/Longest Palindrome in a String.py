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
        def get(l,h):
            while l>=0 and h<len(S):
                if S[l]!=S[h]:
                    break
                l-=1
                h+=1
            return l+1,h-1
        maxi=0;v=[0,0]
        for i in range(len(S)):
            ff,fl=get(i,i)
            sf,sl=get(i,i+1)
            if fl-ff+1>(maxi):
                maxi=fl-ff+1
                v[0]=ff
                v[1]=fl
            if sl-sf+1>(maxi):
                maxi=sl-sf+1
                v[0]=sf
                v[1]=sl
        return S[v[0]:v[1]+1]

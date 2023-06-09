'''
Given a string S. The task is to print all unique permutations of the given string in lexicographically sorted order.

Example 1:

Input: ABC
Output:
ABC ACB BAC BCA CAB CBA
Explanation:
Given string ABC has permutations in 6 
forms as ABC, ACB, BAC, BCA, CAB and CBA .
Example 2:

Input: ABSG
Output:
ABGS ABSG AGBS AGSB ASBG ASGB BAGS 
BASG BGAS BGSA BSAG BSGA GABS GASB 
GBAS GBSA GSAB GSBA SABG SAGB SBAG 
SBGA SGAB SGBA
Explanation:
Given string ABSG has 24 permutations.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function find_permutaion() which takes the string S as input parameter and returns a vector of string in lexicographical order.

Expected Time Complexity: O(n! * n)
Expected Space Complexity: O(n! * n)

Constraints:
1 <= length of string <= 5
'''
class Solution:
    def find_permutation(self, S):

        factos = [1, 1, 2, 6, 24, 120, 720]
        l = len(S)
        wordset = set()
        words = []
        sortedchars = [ch for ch in S]
        sortedchars.sort()
        
        for w in range(1, factos[l] + 1):
            chars = [ch for ch in sortedchars]
            word = ""
            for i in range(1, l + 1):
                word += chars.pop(((w - 1) // factos[l - i]) % len(chars))
            if word not in wordset:
                wordset.add(word)
                words.append(word)
        
        return words

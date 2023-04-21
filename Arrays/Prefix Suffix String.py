'''
Given two Lists of strings s1 and s2, you have to count the number of strings in s2 which is either a suffix or prefix of at least one string of s1.

Example 1:

Input:
s1 = ["cat", "catanddog", "lion"]
s2 = ["cat", "dog", "rat"]
Output: 
2
Explanation: 
String "cat" of s2 is prefix of "catanddog"
& string "dog" of s2 is suffix of "catanddog" 
Example 2:

Input: 
s1 = ["jrjiml", "tchetn", "ucrhye", "ynayhy", 
       "cuhffd", "cvgpoiu", "znyadv"]
s2 = ["jr", "ml", "cvgpoi", "gpoiu", "wnmkmluc", 
      "geheqe", "uglxagyl", "uyxdroj"] 
Output: 
4
Explanation: 
String "jr" of s2 is prefix of "jrjiml", 
"ml" of s2 is suffix of "jrjiml", 
"cvgpoi" of s2 is prefix of "cvgpoiu" &
"gpoiu" of s2 is suffix of "cvgpoiu"
Your Task:
You don't need to read input or print anything. Your task is to complete the function prefixSuffixString(), which takes 2 strings s1 and s2 as input
and returns an integer value as the number of strings in s2 which is a prefix or suffix in s1.

Expected Time Complexity: O(max(len(s1) , len(s2) ))
Expected Space Complexity: O(1)

Constraints:
   1 <= s1,s2 < 5 * 10^3
   5 <= len(s1[i]), len(s2[i]) < 25
'''
class Node:
    def __init__(self):
        self.nod=dict()
class Trie:
    def __init__(self):
        self.root=Node()
    def insert(self,val):
        tem=self.root
        for i in val:
            if i not in tem.nod:
                tem.nod[i]=Node()
            tem=tem.nod[i]
    def search(self,val):
        tem=self.root
        for i in val:
            if i not in tem.nod:
                return False
            tem=tem.nod[i]
        return True    
            
            
class Solution:
    def prefixSuffixString(self, s1, s2) -> int:
        #code here
        root1=Trie()
        root2=Trie()
        for word in s1:
            root1.insert(word)
            root2.insert(word[::-1])
        ans=0
        for word in s2:
            if root1.search(word) or root2.search(word[::-1]):
                ans+=1
        return ans 

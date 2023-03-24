'''
Given a string S which consists of only lowercase English alphabets, you have to perform the below operations:
If the string S contains any repeating character, remove the first repeating character and reverse the string and again perform the above operation on
the modified string, otherwise, you stop.
You have to find the final string.

Example 1:

Input: S = "abab"
Output: ba
Explanation:
In 1st operation: The first repeating 
character is a. After Removing the first 
character, S = "bab". After Reversing the 
string, S = "bab".
In 2nd operation: The first non repeating 
character is b. After Removing the first 
character, S = "ab". After Reversing the 
string, S = "ba".
Now the string S does not contain any 
repeating character.
Example 2:

Input: S = "dddd"
Output: d
Your Task:  
You don't need to read input or print anything. Your task is to complete the function removeReverse( ) which accepts a string S input parameter and returns
the modified string.

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(K), K <= 26.

Constraints:
The string contains only lowercase English alphabets.
1 < |S| < 105
|S| denotes the length of the string S.
'''
from typing import List
from array import array

class Solution:
    def removeReverse(self, s: str) -> str:
        
        counter = array('I', [0] * 128)
        
        s_len = len(s)
        included = [True] * s_len
        
        for c in s:
            counter[ord(c)] += 1
        
        left = 0
        right = s_len - 1
        rev = False
        
        while left <= right:
            first = s[left]
            last = s[right]
            
            if not rev:
                if counter[ord(first)] > 1:
                    counter[ord(first)] -= 1
                    rev = not rev
                    included[left] = False
                left += 1
            else:
                if counter[ord(last)] > 1:
                    counter[ord(last)] -= 1
                    rev = not rev
                    included[right] = False
                right -= 1
        
        res = ''
        for i in range(s_len):
            if included[i]:
                res += s[i]
        
        if rev:
            res = res[::-1]
        
        return res

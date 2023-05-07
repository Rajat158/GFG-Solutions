'''
You are given a string str of length n. You want to choose a non-zero integer k (k<=n), such that you can perform the following operation:
Take the prefix of the string of length k and append the reverse of it to itself.
Your task is to find the lexicographically smallest string you can get.

Example 1:

Input:
str = "bvdfndkn"
Output:
bb
Explanation:
"bb" is the lexicographically smallest string you can get. If you choose k>1 the order of the resulting string will increase.

Example 2:

Input:
str = "casd"
Output:
caac
Explanation:
"caac" is the lexicographically smallest string you can get.
Your Task:
You don't need to read input or print anything. Your task is to complete the function stringMirror() which takes a String str as input, and returns the lexicographically smallest string.

Expected Time Complexity: O(|str|)
Expected Space Complexity: O(|str|)

Constraints:
1 <= |str| <= 105
'''
class Solution:
    def stringMirror(self, str : str) -> str:
        ans = ""
        ans = ans + str[0]
        for i in range(1,len(str)):
            if ord(str[i-1])>ord(str[i]) or (i>1 and str[i-1]==str[i]):
                ans=ans+str[i]
            else:
                break
        ans = ans+ans[::-1]
        return ans
        

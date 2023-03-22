'''
Given a string S. In one operation, you can remove the substring "pr" from the string S and get amount X or you can remove the substring "rp" and get the amount Y. 
Find the maximum amount you can get if you perform zero or more such operations optimally. 

Note : 

Substring of a string S is defined as a continuous sequence of characters in S.
After removing pr or rp, the order of remaining letters should remain the same.

Example 1:

Input:
X = 5, Y = 4
S = "abppprrr"
Output: 15
Explanation: 
Here, S = "abppprrr" 
X= 5, Y=4.
Remove "pr", new string S = "abpprr".
Remove "pr", new string S = "abpr".
Remove "pr", new string S = "ab".
In total, we removed "pr" 3 times, 
so total score is 3*X + 0*Y = 3*5 =15.
 

 

Example 2:

Input:
X = 7, Y = 7
S = "prpptppr"
Output: 14
Explanation: 
Here, S = "prpptppr" 
X= 7, Y=7.
As both have the same amount we can first 
remove either pr or rp. Here we start with pr
Remove "pr", new string S = "pptppr".
Remove "pr", new string S = "pptp".
In total, we removed "pr" 2 times, 
so total score is 2*X + 0*Y = 2*7 =14.

Your Task: 
You don't need to read input or print anything. Your task is to complete the function solve() which takes the X ,Y and string S as input
parameters and returns the maximum amount you can get after performing the above operations.


Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(|S|)


Constraints:
1 ≤ |S| ≤ 105
1 ≤ X,Y ≤ 105
S contains lowercase English letters only.
'''
class Solution:
    def solve (self, X, Y, S):
        
        def rp(string, x, y, ans, flag):
            stack = []
            for char in string:
                if char == 'p':
                    if stack and stack[-1] == 'r':
                        ans[0] += y
                        stack.pop()
                    else:
                        stack.append(char)
                else:
                    stack.append(char)
            if flag:
                pr("".join(stack), x, y, ans, False)
        def pr(string, x, y, ans, flag):
            stack = []
            for char in string:
                if char == 'r':
                    if stack and stack[-1] == 'p':
                        ans[0] += x  
                        stack.pop()
                    else:
                        stack.append(char)
                else:
                    stack.append(char)
            if flag:
                rp("".join(stack), x, y, ans, False)
        ans = [0]
        if X  > Y:
            pr(S, X, Y, ans, True)
        else:
            rp(S, X, Y, ans, True)
        return ans[0]


'''
The task is to find the second smallest number with a given sum of digits as S and the number of digits as D.
Example 1:

Input:
S = 9 
D = 2
Output:
27
Explanation:
18 is the smallest number possible with sum = 9
and total digits = 2, Whereas the second
smallest is 27.
Example 2:

Input:
S = 16
D = 3
Output:
178
Explanation:
169 is the smallest number possible with sum is
16 and total digits = 3, Whereas the second
smallest is 178.

Your Task:
You don't need to read input or print anything. Your task is to complete the function secondSmallest() which takes the two integers S and D
respectively and returns a string which is the second smallest number if possible, else return "-1".

Expected Time Complexity: O(D)
Expected Space Complexity: O(1)

Constraints:
1 ≤ S ≤ 105
1 ≤ D ≤ 105
'''
class Solution:

    def secondSmallest(self, S, D):

        ans=["0"]*D

        if D*9<=S:

            return "-1"

        S=S-1

        e=D-1

        for i in range(D-1,0,-1):

            if S>=9:

                ans[i]="9"

                S=S-9

                e=i

            else:

                ans[i]=str(S)

                S=0

        ans[0]=str(1+S)

        ans[e]=str(int(ans[e])-1)

        ans[e-1]=str(int(ans[e-1])+1)

        return ''.join(ans)

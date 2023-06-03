'''
Given three stacks S1, S2 & S3 of size N1, N2 & N3 respectively, having only Positive Integers. The task is to find the possible equal maximum sum of the stacks with the removal of top elements allowed. Stacks are represented as an array, and the first index of the array represents the top element of the stack.

Example 1:

Input:
N1 = 3, N2 = 4, N3 = 2
S1 = {4,2,3}
S2 = {1,1,2,3}
S3= {1,4}
Output:
5
Explanation:
We can pop 1 element from the 1st stack, and 2
elements from the 2nd stack. Now remaining elements
yield the equal sum of the three stacks, that is 5.
Example 2:

Input:
N1 =2, N2 = 1, N3 = 3
S1 = {4,7}
S2 = {10}
S3 = {1,2,3}
Output:
0
Explanation:
We will never get an equal sum after popping
some elements, so the answer will be 0.
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxEqualSum() which takes the arrays S1[], S2[], and S3[] and their sizes N1, N2, and N3 as inputs and returns the maximum equal sum we can obtain.

Expected Time Complexity: O(N1+N2+N3)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N1, N2, N3 <= 105
1 <= S1[i], S2[i], S3[i] <= 103
The sum, N1+N2+N3 doesn't exceed 106
'''
from typing import List

class Solution:
    def maxEqualSum(self, N1:int,N2:int,N3:int, S1 : List[int], S2 : List[int], S3 : List[int]) -> int:
        suffix_sums = []
        for nums in [S1,S2,S3]:
            nums = nums[::-1]
            curr_suff_sum = [0]
            for num in nums:
                curr_suff_sum.append(curr_suff_sum[-1] + num)
            
            suffix_sums.append(curr_suff_sum)
            
        
        #find intersection
        first = set(suffix_sums[0])
        second = set()
        for num in suffix_sums[1]:
            if num in first:
                second.add(num)
        
        all_three = []
        for num in suffix_sums[-1]:
            if num in second:
                all_three.append(num)
        
        return max(all_three)

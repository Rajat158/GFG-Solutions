'''
Given n ranges of the form [p, q] which denotes all the numbers in the range [p, p + 1, p + 2,...q].  Given another integer q denoting the number of queries. The task is to return the kth smallest element for each query (assume k>1) after combining all the ranges.
In case the kth smallest element doesn't exist return -1. 

Example 1:

Input:
n = 2, q = 3
range[] = {{1, 4}, {6, 8}}
queries[] = {2, 6, 10}
Output: 
2 7 -1
Explanation: 
After combining the given ranges, 
the numbers become 1 2 3 4 6 7 8. As here 2nd 
element is 2, so we print 2. As 6th element is 
7, so we print 7 and as 10th element doesn't 
exist, so weprint -1.
Example 2:

Input:
n = 2, q = 2
range[] = {{2, 6}, {5, 7}} 
queries[] = {5, 8}
Output: 
6 -1
Explantion: 
After combining the ranges, we'll take Union of 
range= {2,3,4,5,6,7}, here  5th smallest number 
will be 6 and 8th smallest number does not exists.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function kthSmallestNum() which takes a n * 2 array denoting the ranges and an array denoting the queries.

Expected Time Complexity: O(nlogn+q*n)
Expected Auxiliary Space: O(q)

Constraints:
1 <= n <= 103
1 <= range[i][0] <= range[i][1] <= 2*109
1 <= q <= 500
1 <= queries[i] <= 2*109
'''
from typing import List

class Solution:
    def kthSmallestNum(self, n : int, ranges : List[List[int]], q : int, queries : List[int]) -> List[int]:
        # Sort ranges based on the start value
        ranges.sort()

        # Find missing elements to determine skip and
        # count the number of unique elements in each interval
        skip = [0] * n
        count = [0] * n

        if ranges[0][0] > 1:
            skip[0] = ranges[0][0] - 1

        count[0] = ranges[0][1] - ranges[0][0] + 1

        for i in range(1, n):
            gap = ranges[i][0] - ranges[i - 1][1] - 1
            skip[i] = skip[i - 1] + max(0, gap)

            count[i] = count[i - 1]

            # Check for overlap
            if ranges[i - 1][1] >= ranges[i][0]:
                count[i] += ranges[i][1] - ranges[i - 1][1] + 1
            else:
                count[i] += ranges[i][1] - ranges[i][0] + 1

        # Serve each query and determine the interval in which the kth element lies
        ans = [-1] * q

        for i in range(q):
            idx = -1

            # Find the interval where the ith element belongs, if it exists
            for j in range(n):
                if queries[i] <= count[j]:
                    idx = j
                    break

            # If the interval exists, find the target value
            if idx != -1:
                ans[i] = skip[idx] + queries[i]

        return ans

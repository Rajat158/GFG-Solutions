'''
Given a Binary Tree having positive and negative nodes. Find the maximum sum of a level in the given Binary Tree.

Example 1:

Input :               
             4
          /    \
         2     -5
        / \    / \
      -1   3  -2  6

Output: 6

Explanation :
Sum of all nodes of 0'th level is 4
Sum of all nodes of 1'th level is -3
Sum of all nodes of 2'th level is 6
Hence maximum sum is 6

Example 2:

Input :          
            1
          /   \
         2     3
        / \     \
       4   5     8
                / \
               6   7  

Output :  17

Explanation: Maximum sum is at level 2.

Your Task:  
You dont need to read input or print anything. Complete the function maxLevelSum() which takes root node as input parameter and returns the maximum sum
of any horizontal level in the given Binary Tree.

Expected Time Complexity: O(N), where N is no of node.
Expected Auxiliary Space: O(W), Where W is the max width of the tree.


Constraints:
1 ≤ N ≤ 104
'''
from collections import deque

class Solution:
    def maxLevelSum(self, root):
        # Code here
        q=deque()
        
        max_sum=-float('inf')
        q.append(root)
        # q.append(None)
        while q:
            curr_sum=0
            n=len(q)
            for i in range(n):
                curr=q.popleft()
                curr_sum+=curr.data
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            max_sum=max(curr_sum, max_sum)

        return max_sum

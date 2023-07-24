'''
Given a Binary Tree, find Right view of it. Right view of a Binary Tree is set of nodes visible when tree is viewed from right side.

Right view of following tree is 1 3 7 8.

          1
       /     \
     2        3
   /   \      /    \
  4     5   6    7
    \
     8

Example 1:

Input:
       1
    /    \
   3      2
Output: 1 2
Example 2:

Input:
     10
    /   \
  20     30
 /   \
40  60 
Output: 10 30 60
Your Task:
Just complete the function rightView() that takes node as parameter and returns the right view as a list. 

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 ≤ Number of nodes ≤ 105
0 ≤ Data of a node ≤ 105
'''
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class Solution:
    # Function to return list containing elements of right view of binary tree.
    def rightView(self, root):
        result = []
        
        if root is None:
            return result

        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            last_node = None

            for i in range(level_size):
                current = queue.popleft()

                last_node = current  # Update last node for this level

                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)

            # After processing each level, the lastNode will be the rightmost node at that level.
            result.append(last_node.data)

        return result

'''
Two of the nodes of a Binary Search Tree (BST) are swapped. Fix (or correct) the BST by swapping them back. Do not change the structure of the tree.
Note: It is guaranteed than the given input will form BST, except for 2 nodes that will be wrong.
 
Example 1:
Input:
       10
     /    \
    5      8
   / \
  2   20
Output: 1
Explanation:
 
Example 2:

Input:
         11
       /    \
      3      17
       \    /
        4  10
Output: 1 
Explanation: 
By swapping nodes 11 and 10, the BST 
can be fixed.
Your Task:
You don't need to take any input. Just complete the function correctBst() that takes root node as parameter. The function should return the root of corrected BST.
BST will then be checked by driver code and 0 or 1 will be printed.

Expected Time Complexity : O(Number of nodes)
Expected Auxiliary Space : O(logN), N = number of nodes
 
Constraints:
1 <= Number of nodes <= 10^5
'''
#User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        
'''

class Solution:
    def correctBST(self, root):
        def _solve(nd):
            if not nd: return
            nonlocal first, prev
            if _solve(nd.left): return True
            if not first:
                if prev and prev.data > nd.data: 
                    first = prev
            elif first.data < nd.data:
                first.data, prev.data = prev.data, first.data
                return True
            prev = nd
            if _solve(nd.right): return True
            return False
        
        first, prev = None, None
        if not _solve(root): 
            first.data, prev.data = prev.data, first.data
        return root

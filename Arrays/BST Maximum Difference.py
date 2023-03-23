'''
You are given a Binary Search Tree and a target value. You must find the maximum difference between the sum of node data from root to target and
from target to a child leaf node (target exclusive). Initially, you are at the root node.
Note: If the target node is not present in the tree then return -1.

Example 1:

Input:


Target = 20
Output: 10
Explanation: From root to target the sum of node data is 25 and from target to the children leaf nodes the sums of the node data are 15 and 25. So,
the maximum difference will be (25-15) = 10.
Example 2:

Input:

Target = 50
Output: -1
Explanation: The target node is not present in the tree.

Your Task:
You don't need to read input or print anything. Your task is to complete the function maxDifferenceBST() which takes BST(you are given the root node of the BST )
and target as input, and returns an interger value as the required answer. If the target is not present in the BST then return -1.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(H), H - Height of the Tree.


Constraints:
1 <= n < 10^4
1 <= node.data < 10^5
1 <= target < 10^5
'''
class Solution:
    def maxDifferenceBST(self,root, target):
        def result(root):
            if root==None:
                return 1e9
            if root.left==None and root.right==None:
                return root.data
            l=result(root.left)
            r=result(root.right)
            return min(l,r)+root.data
            
        
        val=[0]
        def solve(root,t):
            if root==None:
                return -1
            if root.data==t:
                val[0]=min(result(root.left),result(root.right))
                return 0
            
            if root.data>t:
                ans=solve(root.left,t)
            else:
                ans=solve(root.right,t)
            if ans!=-1:
                return ans+root.data
            else:
                return -1
        
        res=solve(root,target)
        if val[0]==1e9:
            return res
        return res-val[0]

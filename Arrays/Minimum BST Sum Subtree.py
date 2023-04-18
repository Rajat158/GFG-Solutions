'''
Given a binary tree and a target, find the number of node in the minimum sub-tree with the given sum equal to the target which is also a binary search tree.

Example 1:

Input:
           13
         /    \
       5       23
      / \      / \
     N   17   N   N
         /
        16
Target: 38
Output: 3
Explanation: 5,17,16 is the smallest subtree
with length 3.
 

Example 2:

Input:
             7
           /   \
          N    23
             /   \
            10    23
           /  \   / \
          N   17 N   N
Target: 73
Output: -1
Explanation: No subtree is bst for the given target.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function minSubtreeSumBST() which takes the tree root and target as
input parameters which is a binary Tree and returns the length of the minimum subtree having a sum equal to the target but which is a binary search tree.

Expected Time Complexity: O(N), where N is no. of nodes
Expected Space Complexity: O(h), where h is the height of the tree

Constraints:
1 <= N <= 10^5
'''
class Solution:
    def check(self,node,mini,maxi):
        
        if node is None:
            return True
 
    # False if this node violates min/max constraint
        if node.data < mini or node.data > maxi:
           return False
 
    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
        return (self.check(node.left, mini, node.data - 1) and
            self.check(node.right, node.data+1, maxi))
     
    def solve(self,root,ans,target,k):
        maxi=4294967296
        mini = -4294967296
        if root==None:
            return (0,0)
        left,l=self.solve(root.left,ans,target,k)
        right,r=self.solve(root.right,ans,target,k)
        
        if left+right+root.data==target and self.check(root,mini,maxi)==True :
            if self.s  > l+r+1:
                self.s=l+1+r
                
            
         
        return (left+right+root.data, l+r+1 )   
    def minSubtreeSumBST(self, target, root):
        
        self.s=10000   
        ans,s=self.solve(root,0,target,0)
        
        if self.s==10000:
            return -1
        return self.s
        

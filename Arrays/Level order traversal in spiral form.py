'''
Given a binary tree and the task is to find the spiral order traversal of the tree.

Spiral order Traversal mean: Starting from level 0 for root node, for all the even levels we print the node's value from right to left and for all the odd levels we print the node's value from left to right. 

For below tree, function should return 1, 2, 3, 4, 5, 6, 7.


 
 

Example 1:

Input:
      1
    /   \
   3     2
Output:1 3 2

Example 2:

Input:
           10
         /     \
        20     30
      /    \
    40     60
Output: 10 20 30 60 40 
Your Task:
The task is to complete the function findSpiral() which takes root node as input parameter and returns the elements in spiral form of level order traversal as a list. The newline is automatically appended by the driver code.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= Number of nodes <= 105
0 <= Data of a node <= 105
'''

#Function to return a list containing the level order traversal in spiral form.
def findSpiral(root):
    # Code here
    if root == None:
        return []
    q = [root]
    ans = []
    flag = 1
    while len(q) != 0:
        size = len(q)
        temp = []
        while size != 0:
            cur = q.pop(0)
            temp.append(cur.data)
            if cur.left != None:
                q.append(cur.left)
            if cur.right!=None:
                q.append(cur.right)
            size -= 1
        
        if flag % 2 != 0:
            temp = temp[::-1]
        for i in temp:
            ans.append(i)
        flag += 1
            
    return ans

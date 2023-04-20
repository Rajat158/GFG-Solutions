'''
Chhota Bheem wants to eat the maximum number of ladoos in Dholakpur on Independence Day. The houses in Dholakpur are arranged in the form of a binary 
tree and have ladoos the same as their house number. Chhota Bheem is standing at his home initially. Find the maximum ladoos he can eat if he can go 
to houses within a maximum distance k from his house. The number of ladoos at his home should also be included in the sum.

Note: Every house has distinct ladoos in it. 
Example 1:

Input:
                   1
                 /    \
                2      9
               /      /  \
              4      5     7
            /   \         /  \
           8     19     20    11
          /     /  \
         30   40   50
home = 9, K = 1
Output:
22
Explanation:
Initially Bheem at 9, so sum = 9
In 2nd move he went to 5, sum=9+5=14
In 3rd move he went to 7, sum=14+7=21
In 4th move he went to 1, sum=21+1=22
So within K distance bheem can get 22 ladoos.  
Example 2:

Input:
                   1
                 /    \
                2      9
               /      /  \
              4      5     7
            /   \         /  \
           8     19     20    11
          /     /  \
         30   40   50
home = 40, K = 2
Output:
113
Explanation:
Initially Bheem at 40, so sum = 40
In 2nd move he went to 19, sum=40+19=59
In 3rd move he went to 4, sum=59+4=63
In 4th move he went to 50, sum=63+50=113
So within K distance bheem can get 113 ladoos.
Your Task:
You don't need to read input or print anything. Complete the function ladoos() which takes the root of the tree, home, and K  as input parameters and 
returns the maximum number of ladoos he can eat.

Expected Time Complexity: O(N), where N is no. of nodes
Expected Space Complexity: O(1)

Constraints:
1 ≤ N, Home ≤ 105
1 ≤ K ≤ 20
'''
from collections import deque

class Solution:
    def ladoos(self, root, home, k):
        if root is None: return 0
        
        if not root.left and not root.right:
            if root.data==home: return root.data
            return 0

        temp, q, pos, len1, node = {}, deque(), 0, 1, None
        q.append(root)
        
        while pos<len1:
            if q[pos].data==home:
                node=q[pos]
                break

            if q[pos].left:
                q.append(q[pos].left)
                temp[q[pos].left], len1 = q[pos], len1+1
            
            if q[pos].right:
                q.append(q[pos].right)
                temp[q[pos].right], len1 = q[pos], len1+1
            
            pos+=1

        q, sum1,temp1 = deque(), 0, set()
        q.append([node, 0])
        while q:
            node, k1 = q.popleft()
            sum1+=node.data
            temp1.add(node)
            if node.left and k1<k and node.left not in temp1:q.append([node.left, k1+1])
            if node.right and k1<k and node.right not in temp1:q.append([node.right, k1+1])
            if node in temp and k1<k and temp[node] not in temp1:q.append([temp[node], k1+1])
        return sum1

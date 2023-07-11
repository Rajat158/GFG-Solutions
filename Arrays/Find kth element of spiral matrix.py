'''
Given a matrix with n rows and m columns. Your task is to find the kth element which is obtained while traversing the matrix spirally. You need to complete the method findK which takes four arguments the first argument is the matrix A and the next two arguments will be n and m denoting the size of the matrix A and then the forth argument is an integer k. The function will return the kth element obtained while traversing the matrix spirally.

Example 1:

Input:
n = 4, m = 4, k = 10
A[][] = {{1  2  3  4},
         {5  6  7  8},
         {9  10 11 12},
         {13 14 15 16}}
Output:
13
Explanation:

The spiral order of matrix will look like 1->2->3->4->8->12->16->15->14->13->9->5->6->7->11->10. So the 10th element in this order is 13. 
Example 2:

Input:
n = 3, m = 3, k = 4
A[][] = {{1 2 3},
         {4 5 6},
         {7 8 9}}
Output:
6
Explanation:
The spiral order of matrix will look like 1->2->3->6->9->8->7->4->5. So the 4th element in this order is 6.
Your Task:
You only need to implement the given function findK(). Do not read input, instead use the arguments given in the function. Return the K'th element obtained by traversing matrix spirally.

Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n*m)

Constraints:
1<=n,m<=103
1<=k<=n*m
'''
class Solution:
    def findK(self, a, n, m, k):
        # Write Your Code here
        left =0
        right=m-1
        top=0
        bottom = n-1
        traversal=0
        count=0
        while left<=right and top<=bottom:
            if traversal==0:
                for i in range(left,right+1):
                    count+=1
                    if count==k:
                        return a[top][i]
                top+=1
                traversal=1
            elif traversal==1:
                for i in range(top,bottom+1):
                    count+=1
                    if count==k:
                        return a[i][right]
                right-=1
                traversal=2
            elif traversal == 2:  
                for i in range(right, left - 1, -1):
                    count+=1
                    if count==k:
                        return a[bottom][i]
                bottom -=1
                traversal= 3
            else: 
                for i in range(bottom, top - 1, -1):
                    count+=1
                    if count==k:
                        return a[i][left]
                left+=1
                traversal= 0
        
        return -1  

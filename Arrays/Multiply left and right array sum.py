'''
Pitsy needs help with the given task by her teacher. The task is to divide an array into two sub-array (left and right) containing n/2 elements each and do the sum of the subarrays and then multiply both the subarrays.

Note: If the length of the array is odd then the right half will contain one element more than the left half.

Example 1:

Input : arr[ ] = {1, 2, 3, 4}
Output : 21
Explanation:
Sum up an array from index 0 to 1 = 3
Sum up an array from index 2 to 3 = 7
Their multiplication is 21.

Example 2:

Input : arr[ ] = {1, 2} 
Output :  2 
 

Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function multiply() that takes an array (arr), sizeOfArray (n), and return the sum of the subarrays and then multiply both the subarrays. The driver code takes care of the printing.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).


Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 1000
1 ≤ A[i] ≤ 100
'''
#Solution-->
#User function Template for python3

def multiply (arr, n) : 
    a=0
    b=0
    if(n%2==0):
        for i in range(0,n//2):
            a=a+arr[i]
        for i in range(n//2,n):
            b=b+arr[i]
        return(a*b)
    else:
        for i in range(0,n//2):
            a=a+arr[i]
        for i in range(n//2,n):
            b=b+arr[i]
        return(a*b)

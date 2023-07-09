'''
You are given an array arr[] of N integers including 0. The task is to find the smallest positive number missing from the array.

Example 1:

Input:
N = 5
arr[] = {1,2,3,4,5}
Output: 6
Explanation: Smallest positive missing 
number is 6.
Example 2:

Input:
N = 5
arr[] = {0,-10,1,3,-20}
Output: 2
Explanation: Smallest positive missing 
number is 2.
Your Task:
The task is to complete the function missingNumber() which returns the smallest positive missing number in the array.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 106
-106 <= arr[i] <= 106
'''
class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        #Your code here
        pos_arr = []
        for num in arr:
            if num > 0:
                pos_arr.append(num)
    
    # Mark visited numbers by negating the corresponding index
        for num in pos_arr:
            index = abs(num) - 1
            if index < len(pos_arr):
                pos_arr[index] = -abs(pos_arr[index])
    
    # Find the first positive number
        for i in range(len(pos_arr)):
            if pos_arr[i] > 0:
                return i + 1
    
    # If all positive numbers are present, return the next number
        return len(pos_arr) + 1

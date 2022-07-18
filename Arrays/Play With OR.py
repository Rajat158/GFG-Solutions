'''
 You are given an array arr[], you have to re-construct an array arr[].
The values in arr[] are obtained by doing OR(bitwise or) of consecutive elements in the array.

Example 1:

Input : arr[ ] = {10, 11, 1, 2, 3}
Output : 11 11 3 3 3
Explanation:
At index 0, arr[0] or arr[1] = 11
At index 1, arr[1] or arr[2] = 11
At index 2, arr[2] or arr[3] = 3
...
At index 4, No element is left So, it will 
remain as it is.
New Array will be {11, 11, 3, 3, 3}.

Example 2:

Input : arr[ ] = {5, 9, 2, 6} 
Output :  13 11 6 6 
 

Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function game_with_number() that takes an array (arr), sizeOfArray (n), and return the array re-constructed array arr. The driver code takes care of the printing.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

 

Constraints:

1 ≤ N ≤ 105
1 ≤ arr[i] ≤ 107
'''
#Solution-->
#User function Template for python3

def game_with_number (arr,  n) : 
    #Complete the function
    l1=[]
    for i in range(1,n):
        l1.append(arr[i-1]|arr[i])
    l1.append(arr[-1])
    return(l1)

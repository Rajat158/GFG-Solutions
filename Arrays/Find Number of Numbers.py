'''
Given an array A[]  of n elements. Your task is to complete the Function num which returns an integer denoting the total number of times digit k appears in the whole array.

For Example:
Input:
A[]={11,12,13,14,15}, k=1
Output:
6

Explanation: Here digit 1 appers 
the whole array 6 times.
Your Task:

You don't need to read input or print anything. Complete the function Num() which accepts an integer N and array A as input parameter and return the desire output.

Constraints:
1<=T<=100
1<=n<=20
1<=A[]<=1000
'''
#Solution-->
# Your task is to complete this function
# Function should return an integer
def num(arr, n, k):
    # Code here
    w=""
    a=[str(x) for x in arr]
    s=w.join(a)
    return(s.count(str(k)))

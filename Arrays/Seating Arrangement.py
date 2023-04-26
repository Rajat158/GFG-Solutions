'''
You are given an integer n, denoting the number of people who needs to be seated, and a list of m integers seats, where 0 represents a vacant seat 
and 1 represents an already occupied seat.

Find whether all n people can find a seat, provided that no two people can sit next to each other.

Example 1:

Input:
n = 2
m = 7
seats[] = {0, 0, 1, 0, 0, 0, 1}
Output:
Yes
Explanation:
The two people can sit at index 0 and 4.
Example 2:

Input:
n = 1
m = 3
seats[] = {0, 1, 0}
Output:
No
Explanation:
There is no way to get a seat for one person.
Your Task:

You don't have to input or print anything. Complete the function is_possible_to_get_seats() which takes the input parameters and return a boolean value,
indicating whether all people can find a seat.

Expected Time Complexity: O(m)
Expected Space Complexity: O(1)

Constraints:

0 <= n <= 105
1 <= m <= 105
seats[i] == 0 or seats[i] == 1
'''
from typing import List
class Solution:
    def is_possible_to_get_seats(self, n : int, m : int, seats : List[int]) -> bool:
        # code here
        if m==1 and n==1 and seats[0]==0:
            return True
        if m==1 and n==1 and seats[0]==1:
            return False
        
        for i in range(m):
            if seats[i]==0:
                if i-1<0:
                    if seats[i]==0 and seats[i+1]==0 and n!=0:
                        seats[i]=1
                        n-=1
                elif i+1==m:
                    if seats[i]==0 and seats[i-1]==0 and n!=0:
                        seats[i]=1
                        n-=1
                else:
                    if seats[i-1]==0 and seats[i]==0 and seats[i+1]==0 and n!=0:
                        seats[i]=1
                        n-=1
        if n==0:
            return True
        return False

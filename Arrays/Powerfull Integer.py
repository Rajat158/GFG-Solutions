'''
Your are given an 2D integer array  intervals whose length is n where intervals[i]=[start,end] means all integers from start to  end inclusive start and end are also present and also we are given an integer k . We have to return the Powerfull Integer.Powerfull Integer is that integer that occurs at least k times and if multiple integers  have at least k  occurences we have to return the maximum integer out of all those elements . 

Note: If no integer occurs at least k times return -1 in that case .

Example 1:

Input :
n=3
intervals={{1,3},{4,6},{3,4}}
k=2
Output: 4
Explanation:
As we can see that 3 and 4 are the 2 integers 
that have 2 occurences(2>=k) so we have 4 
in this case as the Powerfull integer as it 
is the maximum element which satisfies the condition.
Example 2:

Input :
n=4
intervals={{1,4},{12,45},{3,8},{10,12}}
k=3
Output: -1
Explanation:
As we can see that no integer occurs 
3 times so in that case we have to 
return -1 (see Note).

Your Task:
You don't need to read input or print anything. Your task is to complete the function powerfullInteger() which takes an integer n, a 2d array intervals  and an integer k respectively and you have to return powerfull Integer if it exists else return -1.

Expected Time Complexity: O(NlogN)
Expected Space Complexity: O(N)

Constraints:
1<=n<=105
1<=intervals[i][0]<=intervals[i][1]<=109
1<=k<=105
The sum of n over all test cases won't exceed 106
'''
from typing import List


class Solution:
    def powerfullInteger(self, n : int, intervals : List[List[int]], k : int) -> int:
        # code here
        l=[]
        for n1,n2 in intervals:
            l.append((n1,-1))
            l.append((n2,1))
        l.sort()
        
        n=0
        ans=-1
        for n1,n2 in l:
            if n2==-1:
                n+=1
            else:
                if n>=k:
                    ans=max(ans,n1)
                n-=1
        return ans
        


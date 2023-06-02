'''
Santa is still not married. He approaches a marriage bureau and asks them to hurry the process. The bureau checks the list of eligible girls of size N and hands it over to Santa. Santa being conscious about his marriage is determined to find a girl with maximum connections so that he can gather more information about her. Accordingly, he looks to figure out the maximum number of girls (from the list) who know each other to achieve the above purpose.

In order to finalize the girl, he needs to find the Kth prime. Where k = largest group of girls who know each other. Considering Santa's poor knowledge of Maths, he seeks Banta's help for the answer. Now you, a fan of Santa Banta Jokes, take this prestigious opportunity to solve the problem.

In case no of connections is zero, print "-1". Here the connection between girls is represented by a 2-D array arr of dimension M*2, where M is the number of connections.

Note :
1. Suppose girl "a" knows girl "b" and girl "b" knows girl "c", then girl "a" also knows girl "c". Transitivity holds here.
2. Consider 1 as a composite number.
3. For precompute function given in the template you just have to complete it and use it wherever required, do not call it again and again, it is already being called by driver function before executing test cases. 

Example 1:

Input : 
arr[] = {{1,2},{2,3},{3,4},{4,5},{6,7},{9,10}}
N = 10 and M = 6
Output : 
11
Explanation:
Here in this graph there are 4 groups. 
In 1st group: (1 -> 2 -> 3 -> 4 -> 5) are 
there. In 2nd group: (6 -> 7) are there.
In 3rd group: (8) is there.
In 4th group: (10 -> 9) are there.
In these 4 group the maximum number of 
value is 5. So, K = 5 and the 5th prime number 
is 11. Return 11.
Example 2:

Input : 
arr[ ] = {{1, 2}}
N = 2 and M = 1 
Output : 
3
Explanation:
In this Example there will only be a 
single group of 2 girls, and hence the 
value of K is 2, The 2nd prime is 3.
Your Task:

This is a function problem. The input is already taken care of by the driver code. You only need to complete the function helpSanta() that takes a number of girls (n), a number of connections (m), an adjacency list of girls connections (g), and return the Kth prime no if there are no connections then return -1. The driver code takes care of the printing.

Expected Time Complexity: O(N + M).
Expected Auxiliary Space: O(N + M).

Constraints:

1 ≤ n ≤ 105
0 ≤ m ≤ 105
1 ≤ u, v ≤ n
'''
#User function Template for python3

class Solution:
    def precompute(self):
        primes = [True]*(10**6)
        primes[0] = False
        primes[1] = False
        for i in range(len(primes)):
            if not primes[i]:
                continue
            for j in range(i*i, len(primes), i):
                primes[j] = False
        self.primes = [i for i, t in enumerate(primes) if t]
        
    
    def helpSanta (self, n, m, g) : 
        from collections import defaultdict
        if m == 0:
            return -1
            
        arr = [i for i in range(n+1)]
        
        def find(i):
            if arr[i] != i:
                arr[i] = find(arr[i])
            return arr[i]
            
        for i, grp in enumerate(g):
            if i > n:
                break
            
            rx = find(i)
            for y in grp:
                ry = find(y)
                if rx != ry:
                    arr[ry] = rx
                
        num = 0
        cnt = defaultdict(int)
        for i in range(1, n+1):
            r = find(i)
            cnt[r] += 1
            num = max(num, cnt[r])
        return self.primes[num-1]

'''
Elena is the topper of the class. Once her teacher asked her a problem. He gave Elena an array of integers of length n. He calls a subset of array arr
good if its product can be represented as a product of one or more distinct prime numbers. He asked her to find the number of different good subsets in
arr modulo 109 + 7.

As a good friend of Elena help her to solve the problem.

Example 1:

Input:
N: 4
arr: {1,2,3,4}
Output: 6
Explanation: 
The good subsets are:
- [1,2]: product is 2, which is the product of distinct
prime 2.
- [1,2,3]: product is 6, which is the product of 
distinct primes 2 and 3.
- [1,3]: product is 3, which is the product of distinct
prime 3.
- [2]: product is 2, which is the product of distinct
 prime 2.
- [2,3]: product is 6, which is the product of distinct
primes 2 and 3.
- [3]: product is 3, which is the product of distinct
prime 3.
Example 2:

Input:
N : 3
arr : {2, 2, 3}
Output: 5
Explanantion:
The good subsets are : {2}, {2}, {2, 3}, {2, 3}, {3}
Your Task:
The task is to complete the function goodSubsets() which takes an integer n and an array arr as the input parameters and should return the number of
different good subsets.

Expected Time Complexity: O(NlogN)
Expected Space Complexity: O(N)

Constraints:

1 <= N <= 105
1< = arr[i] <= 30
'''
from typing import List


class Solution:
      def goodSubsets(self, n : int, arr : List[int]) -> int:
        from functools import reduce
        MOD = 10**9+7
        primes = [2,3,5,7,11,13,17,19,23,29]
        A = [0]*31
        for v in arr: A[v] += 1
        # process valid composites numbers
        def exc(*ex): return [v for v in primes if v not in ex and A[v]>0]
        mp = {
            (6,): exc(2,3), (10,): exc(2,5), (14,): exc(2,7), 
            (15,): exc(3,5), (15,14): exc(2,3,5,7),
            (21,): exc(3,7), (21,10): exc(2,3,5,7),
            (22,): exc(2,11), (22,15): exc(2,3,5,11), (22,21): exc(2,3,7,11),
            (26,): exc(2,13), (26,15): exc(2,3,5,13), (26,21): exc(2,3,7,13), 
            (30,): exc(2,3,5)
        }
        ans = 0
        for v in primes:
            ans = (ans + A[v] * (1+ans) ) % MOD
        for cvs, targets in mp.items():
            if any( A[v]==0 for v in cvs ): continue
            prod = reduce(lambda a,b: (a*b)%MOD, (A[v] for v in cvs))
            tmp = 0
            for v in targets:
                tmp = (tmp + A[v] * (1 + tmp)) % MOD
            ans = (ans + (tmp+1)*prod) % MOD
            
        K1 = pow(2, A[1], MOD) # \sum_{i=0}^{n} \binom{n}{i}
        ans = (ans * K1) % MOD
        return ans

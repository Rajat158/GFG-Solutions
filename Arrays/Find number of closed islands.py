'''
Given a binary matrix mat[][] of dimensions NxM such that 1 denotes land and 0 denotes water. Find the number of closed islands in the given matrix.

Note: A closed island is a group of 1s surrounded by only 0s on all the boundaries (except diagonals). In simple words, a closed island is an island whose none of the 1s lie on the edges of the matrix.

Example 1:

Input:
N = 5, M = 8
mat[][] = {{0, 0, 0, 0, 0, 0, 0, 1}, 
           {0, 1, 1, 1, 1, 0, 0, 1}, 
           {0, 1, 0, 1, 0, 0, 0, 1}, 
           {0, 1, 1, 1, 1, 0, 1, 0}, 
           {1, 0, 0, 0, 0, 1, 0, 1}}
Output:
2
Explanation:
mat[][] = {{0, 0, 0, 0, 0, 0, 0, 1}, 
           {0, 1, 1, 1, 1, 0, 0, 1}, 
           {0, 1, 0, 1, 0, 0, 0, 1}, 
           {0, 1, 1, 1, 1, 0, 1, 0}, 
           {1, 0, 0, 0, 0, 1, 0, 1}} 
There are 2 closed islands. The islands in dark are closed because they are completely surrounded by 0s (water). There are two more islands in the last column of the matrix, but they are not completely surrounded by 0s. Hence they are not closed islands. 
Example 2:

Input:
N = 3, M = 3
mat[][] = {{1, 0, 0},
           {0, 1, 0},
           {0, 0, 1}}
Output: 
1
Explanation:
mat[][] = {{1, 0, 0},
          {0, 1, 0},
          {0, 0, 1}}
There is just a one closed island.
Your task:
You dont need to read input or print anything. Your task is to complete the function closedIslands() which takes two integers N and M, and a 2D binary matrix mat as input parameters and returns the number of closed islands.

Expected Time Complexity: O(N*M)
Expected Auxiliary Space: O(N*M)

Constraints:
1 ≤ N,M ≤ 500
'''
class Solution:
    def dfs(self, x, y, matrix, N, M):
        if x < 0 or y < 0 or x >= N or y >= M or matrix[x][y] == 0:
            return
        
        matrix[x][y] = 0
        
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        for i in range(4):
            self.dfs(x + dx[i], y + dy[i], matrix, N, M)
    
    def closedIslands(self, matrix, N, M):
        ans = 0
        
        for i in range(N):
            for j in range(M):
                if (i == 0 or j == 0 or i == N-1 or j == M-1) and matrix[i][j] == 1:
                    self.dfs(i, j, matrix, N, M)
        
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 1:
                    self.dfs(i, j, matrix, N, M)
                    ans += 1
        
        return ans

'''
Geeks Island is represented by an N * M matrix mat. The island is touched by the Indian Ocean from the top and left edges and the Arabian Sea from the right and bottom edges. Each element of the matrix represents the height of the cell.

Due to the rainy season, the island receives a lot of rainfall, and the water can flow in four directions(up, down, left, or right) from one cell to another one with height equal or lower.

You need to find the number of cells from where water can flow to both the Indian Ocean and the Arabian Sea.

Example 1:

Input:
N = 5, M = 5
mat[][] =    {{1, 3, 3, 2, 4},
               {4, 5, 6, 4, 4},
               {2, 4, 5, 3, 1},
               {6, 7, 1, 4, 5},
               {6, 1, 1, 3, 4}}
Output:
8
Explanation:
Indian    ~   ~   ~   ~   ~
Ocean  ~  1   3   3   2  (4) *
        ~  4   5  (6) (4) (4) *
        ~  2   4  (5)  3   1  *
        ~ (6) (7)  1   4   5  *
        ~ (6)  1   1   3   4  *           
           *   *   *   *   * Arabian Sea
Water can flow to both ocean and sea from the cells
denoted by parantheses().For example at index(1,2), the height of that island is 6. If a water drop falls on that island, water can flow to up direction(as 3<=6) and reach to Indian Ocean. ALso, water can flow to right direction(as 6>=4>=4) and reach to Arabian Sea.
Example 2:

Input:
N = 3, M = 2
mat[][] =    {{1, 1, 1},
               {1, 1, 1}}
Output:
6 
Explanation:
Water can flow from all cells to both Indian Ocean and Arabian Sea as the height of all islands are same.
Your Task:

Your task is to complete the function water_flow() which takes an integer array mat, integer N and integer M as the input parameter and returns an integer, denoting the number of cells from which water can to both ocean and sea.

Expected Time Complexity : O(N*M)
Expected Auxiliary Space : O(N*M)

Constraints:

1 <= N, M <= 103
1 <= mat[i][j] <= 106
'''
#User function Template for python3

from collections import deque
class Solution():
    def bfs(self, mat, n, m, src):
        Q = deque(src)
        visited = set(src)
        while Q:
            x, y = Q.popleft()
            for nx, ny in [[x, y+1], [x, y-1], [x+1, y], [x-1, y]]:
                if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] >= mat[x][y] and (nx,ny) not in visited:
                    Q.append((nx, ny))
                    visited.add((nx,ny))
        return visited
            
        
    def water_flow(self, mat, n, m):
        visited1 = self.bfs(mat, n, m, [(i,0) for i in range(n)] + [(0,j) for j in range(m)])
        visited2 = self.bfs(mat, n, m, [(i,m-1) for i in range(n)] + [(n-1,j) for j in range(m)])
        return len(visited1 & visited2)

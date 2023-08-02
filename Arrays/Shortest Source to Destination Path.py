'''
Given a 2D binary matrix A(0-based index) of dimensions NxM. Find the minimum number of steps required to reach from (0,0) to (X, Y).
Note: You can only move left, right, up and down, and only through cells that contain 1.

Example 1:

Input:
N=3, M=4
A=[[1,0,0,0], 
   [1,1,0,1],
   [0,1,1,1]]
X=2, Y=3 
Output:
5
Explanation:
The shortest path is as follows:
(0,0)->(1,0)->(1,1)->(2,1)->(2,2)->(2,3).
Example 2:

Input:
N=3, M=4
A=[[1,1,1,1],
   [0,0,0,1],
   [0,0,0,1]]
X=0, Y=3
Output:
3
Explanation:
The shortest path is as follows:
(0,0)->(0,1)->(0,2)->(0,3).
Your Task:
You don't need to read input or print anything. Your task is to complete the function shortestDistance() which takes the integer N, M, X, Y, and the 2D binary matrix A as input parameters and returns the minimum number of steps required to go from (0,0) to (X, Y).If it is impossible to go from (0,0) to (X, Y),then function returns -1. If value of the cell (0,0) is 0 (i.e  A[0][0]=0) then return -1.

Expected Time Complexity:O(N*M)
Expected Auxillary Space:O(N*M)

Constraints:
1 <= N,M <= 250
0 <= X < N
0 <= Y < M
0 <= A[i][j] <= 1


'''
from collections import deque

class Solution:
    def isvalid(self, N, M, x, y):
        if x >= N or x < 0:
            return False
        if y >= M or y < 0:
            return False
        return True

    def shortestDistance(self, N, M, A, X, Y):
        movements = [(1, 0), (0, -1), (0, 1), (-1, 0)]
        vis = [[False for _ in range(M)] for _ in range(N)]
        lev = [[-1 for _ in range(M)] for _ in range(N)]
        q = deque()
        q.append((0, 0))
        lev[0][0] = 0
        vis[0][0] = True

        while q:
            vx, vy = q.popleft()
            if vx == X and vy == Y:
                return lev[X][Y]

            for movement in movements:
                child_x = vx + movement[0]
                child_y = vy + movement[1]
                if self.isvalid(N, M, child_x, child_y) and A[child_x][child_y] and not vis[child_x][child_y]:
                    lev[child_x][child_y] = lev[vx][vy] + 1
                    vis[child_x][child_y] = True
                    q.append((child_x, child_y))

        return -1

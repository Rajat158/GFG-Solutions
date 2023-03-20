'''
Give a N*M grid of characters 'O', 'X', and 'Y'. Find the minimum Manhattan distance between a X and a Y.

Manhattan Distance :
| row_index_x - row_index_y | + | column_index_x - column_index_y |


Example 1:

Input:
N = 4, M = 4
grid  = {{X, O, O, O}
         {O, Y, O, Y}
         {X, X, O, O}
         {O, Y, O, O}}
Output:
1
Explanation:
{{X, O, O, O}
{O, Y, O, Y}
{X, X, O, O}
{O, Y, O, O}}
The shortest X-Y distance in the grid is 1.
One possible such X and Y are marked in bold
in the above grid.
Example 2:

Input:
N = 3, M = 3
grid = {{X, X, O}
        {O, O, Y}
        {Y, O, O}}
Output :
2
Explanation:
{{X, X, O}
 {O, O, Y}
 {Y, O, O}}
The shortest X-Y distance in the grid is 2.
One possible such X and Y are marked in bold
in the above grid.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function shortestXYDist() which takes two integers N, and M and an 2D list
of size N*M as input and returns the shortest Manhattan Distance between a X and a Y.

Expected Time Complexity: O(N*M)
Expected Auxiliary Space: O(N*M)


Constraints:
1 ≤ N*M ≤ 105 

There exists at least one 'X' and at least one 'Y' in the grid.
'''
from collections import deque
class Solution:
    def shortestXYDist(self, grid, N, M):
        # code here 
        vis=[[-1]*M for i in range(N)]
        q=deque()
        for i in range(N):
            for j in range(M):
                if grid[i][j]=="X":
                    q.append(([i,j],0))
                    vis[i][j]=1
        while q:
            coord,step=q.popleft()
            r=coord[0]
            c=coord[1]
            if grid[r][c]=="Y":
                return step
            dr=[-1,1,0,0]
            dc=[0,0,-1,1]
            for i in range(4):
                nr=r+dr[i]
                nc=c+dc[i]
                if nr>=0 and nr<N and nc>=0 and nc<M and vis[nr][nc]!=1:
                    q.append(([nr,nc],step+1))
                    vis[nr][nc]=1
        return -1

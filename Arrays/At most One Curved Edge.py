'''
Given an undirected connected graph of n vertices and list of m edges in a graph and for each pair of vertices that are connected by an edge. 

There are two edges between them, one curved edge and one straight edge i.e. the tuple (x, y, w1, w2) means that between vertices x and y, there is a straight edge with weight w1 and a curved edge with weight w2.

You are given two vertices a and b and you have to go from a to b through a series of edges such that in the entire path you can use at most 1 curved edge. Your task is to find the shortest path from a to b satisfying the above condition. If there is no path from a to b, return -1.

 

Example 1:

Input:
n = 4, m = 4
a = 2, b = 4
edges = {{1, 2, 1, 4}, {1, 3, 2, 4},
         {1, 4, 3, 1}, {2, 4, 6, 5}}
Output:
2

Explanation:
We can follow the path 2 -> 1 -> 4.
This gives a distance of 1+3 = 4 if we follow
all straight paths. But we can take the curved
path  from 1 -> 4, which costs 1. This
will result in a cost of 1+1 = 2
Example 2:
Input:
n = 2, m = 1
a = 1, b = 2
edges = {{1, 2, 4, 1}}
Output :
1

Explanation:
Take the curved path from 1 to 2 which costs 1. 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function shortestPath() which takes 4 integers n, m, a, and b, and a list of lists named edges of size m as input and returns the cost of shortest path from a to b.


Expected Time Complexity: O((m+n)log(n))
Expected Auxiliary Space: O(n+m)


Constraints:
1 ≤ n,m ≤ 105
1 ≤ a,b ≤ n
weight of edges ≤ 104
'''
import heapq

class Solution:
    def shortestPath(self, n, m, a, b, edges):
        # code here 
        adj = [[] for _ in range(2 * n + 1)]
        for [x, y, w1, w2] in edges:
            adj[x].append((y, w1))
            adj[y].append((x, w1))
            adj[x].append((y + n, w2))
            adj[y].append((x + n, w2))
            adj[x + n].append((y + n, w1))
            adj[y + n].append((x + n, w1))
            
        visited = [False] * (n * 2 + 1)
        visited[a + n] = True
        heap = [(0, a)]
        while heap:
            d, i = heapq.heappop(heap)
            if i == b or i == b + n:
                return d
            if visited[i]:
                continue
            
            visited[i] = True
            for j, w in adj[i]:
                if not visited[j]:
                    heapq.heappush(heap, (d + w, j))
        return -1

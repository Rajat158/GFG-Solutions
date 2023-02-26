'''
Given an undirected graph with V vertices(numbered from 1 to V) and E edges. Find the number of good components in the graph.
A component of the graph is good if and only if the component is a fully connected component.
Note: A fully connected component is a subgraph of a given graph such that there's an edge between every pair of vertices in a component, the given graph can be a disconnected graph. Consider the adjacency list from index 1.

Example 1:

Input: 

Output: 1
Explanation: We can see that there is only one 
component in the graph and in this component 
there is a edge between any two vertces.
Example 2:

Input:

Output: 2
Explanation: We can see that there are 3 components
in the graph. For 1-2-7 there is no edge between
1 to 7, so it is not a fully connected component.
Rest 2 are individually fully connected component.
Your Task:
You don't need to read input or print anything. Your task is to complete the function
findNumberOfGoodComponent() which takes an integer V and an adjacency list adj as input parameters and returns an integer denoting the number of good components.

Expected Time Complexity: O(V+E)
Expected Auxiliary Space: O(depth of the graph)

Constraints:
1 ≤ V, E ≤ 104
'''
#User function Template for python3

import collections
from collections import deque
from collections import defaultdict

def fun(i,visit,adj):

    visit[i]=1

    

    q=deque()

    t=0

    q.append(i)

    

    while q:

        t+=1

        

        u=q.popleft()

        

        for j in adj[u]:

            if visit[j]==0:

                q.append(j)

                visit[j]=1

    return t

        

 

class Solution:

    def findNumberOfGoodComponent(self, V, adj):

         

        visit=[0]*(V+1)

         

        c=0

        for i in range(1,V+1):

            if visit[i]==0:

                p=False

                a=fun(i,visit,adj)

                

                if a-1 == len(adj[i]):

                    for j in adj[i]:

                        if a-1 != len(adj[j]):

                            p=True

                    if p==False:

                        c+=1

        

        return c

'''
Given a string s whose length is n and array queries of length q where each elements of queries is either of type 1 query or type 2 query which is explained ahead.

There are two types of query.

Query type 1 : ["1",ind,char]  "1" denotes this is type 1 query. In this query you have to change the character at index ind in s to character char.
(Data type of ind,char is string in input)

Query Type 2: ["2",left,right,k]  "2" denotes this is type 2 query. In this query you have to return kth lexographically largest character  in the
subtring of s (it is the kth largest character in sorted order , not the kth distinct character) starting from index left and ending at index right
both left and right are inclusive. (Data type of left,right,k is string in input)

You have to perform each query in the same order as given in  queries and return an array res such that res array contains the answer for each type2 query in same order as it appeared in queries.

Note : 0 based indexing is used.

Example 1:

Input:
n=4
s="abab"
q=2
queries={{"1","2","d"},{"2","1","3","1"}}
Output: 
{"d"}
Explanation:
First query is of type 1 so after changing character at index 2 
to d  s becomes abdb . Now Second query is of type 2 in which 
the 1st(k=1) lexographically largest character is "d" in substring "bdb"(s[1:3]). So we 
returned a array with result of type 2 query {"d"}.
Example 2:

Input:
n=3
s="aaa"
q=3
queries={{"1","1","e"},{"1","2","c"},{"2","1","2","2"}}
Output:
{"c"}
Explanation:
After applying first two queries s becomes aec. Now for 
the last query which is a type 2 second largest character 
in subtring s starting from index 1 to ending at index 2 is "c".
Your Task:
You don't need to read input or print anything. Your task is to complete the function easyTask() which takes an integer n,string s,an integer q and an array queries which contains  queries of type1 and type2  respectively and returns an array res such that res array contains the answer for each type2 query in same order as it appeared in queries.

Expected Time Complexity: O(N+(Q*logN))
Expected Space Complexity: O(N)


Constraints:
1<=n<=5*10^4
1<=q<=10^5
0<=int(left)<=int(right)<=n-1
0<=int(index)<=n-1
1<=int(k)<=right-left+1
s and char contains lowercase english letters
The sum of n over all test cases won't exceed 5*10^4.

 
'''
class SegmentTree:
    def __init__(self, s):
        n = len(s)
        self.tree = [[0]*(26) for _ in range(4*n)]
        self.buildTree(s, 0, n - 1, 0)

    def buildTree(self, s, left, right, index = 0):
        if left == right:
            self.tree[index][ord(s[left])-ord("a")]+=1
            return

        mid = (left + right) // 2
        self.buildTree(s, left, mid, 2 * index + 1)
        self.buildTree(s, mid + 1, right, 2 * index + 2)
        for c in range(26):
            
            self.tree[index][c] = self.tree[2 * index + 1][c] + self.tree[2 * index + 2][c]
    def update(self, s,left, right, pos, char,index = 0):
        if pos < left or pos > right:
            return

        if left == right:
            self.tree[index][ord(s[pos])-ord("a")] -=1
            s[pos]=char
            self.tree[index][ord(s[pos])-ord("a")] +=1
            return

        mid = (left + right) // 2
        if pos <= mid:
            self.update(s,left, mid, pos, char,2 * index + 1)
        else:
            self.update(s,mid + 1, right, pos, char,2 * index + 2)

        for c in range(26):
            
            self.tree[index][c] = self.tree[2 * index + 1][c] + self.tree[2 * index + 2][c]
    def query(self, left, right, i, j, index = 0):
        if right < i or left > j:
            return [0]*26

        if i <= left and right <= j:
            return self.tree[index]

        mid = (left + right) // 2
        temp=[0]*(26)
        
        res1=self.query(left, mid, i, j, 2 * index + 1)
        res2=self.query(mid + 1, right, i, j,2 * index + 2)
        for c in range(26):
            temp[c]=res1[c]+res2[c]
        return temp
class Solution:
    def easyTask(self,n,s,q,queries):
        s=[el for el in s]
        seg=SegmentTree(s)
        res=[]
        for quer in queries:
            if quer[0]=="1":
                seg.update(s,0,n-1,int(quer[1]),quer[2])
            else:
                char_freq=seg.query(0,n-1,int(quer[1]),int(quer[2]))
                k=int(quer[3])
                for c in range(25,-1,-1):
                    k-=min(k,char_freq[c])
                    if k==0:
                        res.append(chr(ord("a")+c))
                        break
        return res


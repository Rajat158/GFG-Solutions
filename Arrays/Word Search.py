'''
Given a 2D board of letters and a word. Check if the word exists in the board. The word can be constructed from letters of adjacent cells only. ie - horizontal or vertical neighbors. The same letter cell can not be used more than once.

Example 1:

Input: board = {{a,g,b,c},{q,e,e,l},{g,b,k,s}},
word = "geeks"
Output: 1
Explanation: The board is-
a g b c
q e e l
g b k s
The letters which are used to make the
"geeks" are colored.
Example 2:

Input: board = {{a,b,c,e},{s,f,c,s},{a,d,e,e}},
word = "sabfs"
Output: 0
Explanation: The board is-
a b c e
s f c s
a d e e
Same letter can not be used twice hence ans is 0
Your Task:
You don't need to read or print anything. Your task is to complete the function isWordExist() which takes board and word as input parameter and returns boolean value true if word can be found otherwise returns false.

Expected Time Complexity: O(N * M * 4L) where N = No. of rows in board, M = No. of columns in board, L = Length of word
Expected Space Compelxity: O(L), L is length of word.

Constraints:
1 ≤ N, M ≤ 100
1 ≤ L ≤ N*M
'''
class Solution:
    def isWordExist(self, board, word):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        def dfs(row, col, idx):
            if idx == len(word):
                return True

            visited[row][col] = True

            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy

                if (
                    0 <= new_row < len(board)
                    and 0 <= new_col < len(board[0])
                    and not visited[new_row][new_col]
                    and board[new_row][new_col] == word[idx]
                ):
                    if dfs(new_row, new_col, idx + 1):
                        return True

            visited[row][col] = False

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1):
                        return True

        return False

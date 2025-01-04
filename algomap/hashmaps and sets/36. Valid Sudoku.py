from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        matrix = {}
        for c in range(9):
            rows[c] = set()
            cols[c] = set()

        for r in range(3):
            matrix[r] = {}
            for k in range(3):
                matrix[r][k] = set()

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != ".":
                    if board[i][j] in rows[i]:
                        return False
                    rows[i].add(board[i][j])

                    if board[i][j] in cols[j]:
                        return False
                    cols[j].add(board[i][j])
                    if board[i][j] in matrix[i//3][j//3]:
                        return False
                    matrix[i//3][j//3].add(board[i][j])
        return True


                # print(i // 3)


s = Solution()
s.isValidSudoku(board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
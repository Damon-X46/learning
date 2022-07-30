

def isValidSudoku(board):
    """
        有效的数独
    """
    rows = [[] * 9 for _ in range(9)]
    cols = [[] * 9 for _ in range(9)]
    boxs = [[] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            tmp = board[i][j]
            if not tmp.isdigit():
                continue
            if tmp in rows[i]:
                return False
            if tmp in cols[j]:
                return False
            # if tmp in boxs[(j // 3) * 3 + (i // 3)]:
            if tmp in boxs[(i // 3) * 3 + (j // 3)]:
                return False
            rows[i].append(tmp)
            cols[j].append(tmp)
            # boxs[(j // 3) * 3 + (i // 3)].append(tmp)
            boxs[(i // 3) * 3 + (j // 3)].append(tmp)
    return True

aaa = isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
print(aaa)
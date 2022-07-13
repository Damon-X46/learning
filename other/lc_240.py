


def findNumberIn2DArray(matrix, target):
    """
        搜索二维矩阵II
        每行的元素从左到右升序排列。
        每列的元素从上到下升序排列。
        
        （用到线性搜索/Z字查找）（从右上角开始）
    """
    if not matrix:
        return False
    rows = len(matrix)
    cols = len(matrix[0])
    row = 0
    col = len(matrix[0]) - 1
    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
    return False

aaa = findNumberIn2DArray([[-5]], -5)
print(aaa)
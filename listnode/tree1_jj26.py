"""
    树的子结构
    输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A, B):
        if not A or not B:
            return False

        def recur(A, B):
            if not B: 
                return True
            if not A or A.val != B.val: 
                return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

# node1, node2, node3, node4, node5 = TreeNode(4), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
# node6, node7, node8, node9 = TreeNode(6), TreeNode(7), TreeNode(8), TreeNode(9)
# node1.left, node1.right = node2, node3
# node2.left, node2.right = node4, node5
# node3.left, node3.right = node6, node7
# node4.left, node4.right = node8, node9

# node11, node22, node33 = TreeNode(4), TreeNode(8), TreeNode(9)
# node11.left, node11.right = node22, node33

node1, node2, node3, node4, node5 = TreeNode(1), TreeNode(0), TreeNode(1), TreeNode(-4), TreeNode(3)
node1.left, node1.right = node2, node3
node2.left, node2.right = node4, node5

node11, node22 = TreeNode(1), TreeNode(-4)
node11.left = node22

aaa = Solution()
bbb = aaa.isSubStructure(node1, node11)
print(bbb)
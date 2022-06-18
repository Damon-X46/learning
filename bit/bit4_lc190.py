
# 看不懂
def reverseBits(n):
    """
        颠倒二进制位
        颠倒给定的 32 位无符号整数的二进制位。

        思路：
        n 从高位开始逐步左， res 从低位（0）开始逐步右移
        逐步判断，如果该位是 1，就 res + 1 , 如果是该位是 0， 就 res + 0
        32 位全部遍历完，则遍历结束

        可以用任何数字和 1 进行位运算的结果都取决于该数字最后一位的特性简化操作和提高性能
    """
    result = 0
    for i in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
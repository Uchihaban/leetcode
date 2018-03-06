# -*- coding: UTF-8 -*-
# 问题：给一个32位的有符号整数，翻转这个数字。
# 注意: 假设我们在一个只能处理32位有符号整数范围的环境中。为了解决这个问题，假如翻转后的数字溢出则函数返回0。



# 32-bit signed integer的补充

# 计算机最小的存储单位是“位” 也就是bit或binary digits，用来存放一个二进制数，即 0或1。 8个二进制位为一个字节Byte。
# 对于 16-bit(16位)的计算机，int是以两个字节来储存的，而32-bit的计算机，则是以4个字节，即32个bit来储存的。
# 正数用原码存储，负数用补码的形式存储（原码取反加1）
# signed的最高位用0，1表示正负，unsigned全部表示数值，以16bit为例，signed的取值范围为(-2^15 to 2^15-1),也就是 -32768 到 +32767的整数，unsigned16位全部用来编码，存储范围便为(0 to 2^16-1),即 0到 65535 的非负整数；
# 你可以声明 int a = 1，或者 int a = -1, 但是不可以声明 unsigned a = -1 。但是需要提到的一点是，不管整数的类型是signed 还是 unsigned，都用了16位来存储，也就是说16位全部用来存储数据
# signed与unsigned的范围是有交集的，即都包含了0到+32767范围的整数
# int占32位的时候，最大可以赋值为：2147483647。也就是0x7fffffff。注意：7的二进制形式最高位为0，如果你对2147483647+1.输出的就是-2147483648。这个数是负数中最大的数，也就是int型可以表示的最小的负数。它的十六进制表示为：0x8fffffff，8的二进制形式最高位是符号位，是1，为负。

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        positive = True
        if x < 0:
            positive = False
        x = abs(x)
        a = 0
        while x > 0:
            a = a * 10 + x % 10
            x = x // 10
        if a > 2 ** 31 - 1:
            return 0
        if not positive:
            return -1 * a
        return a

 # 回顾：应该转化成str类型，再使用切片，后转化为int类型
 # 切片大法：(cool!)
 class Solution:
    def reverse(self,x):
        sign = 1
        if x > 0:
            pass
        else:
            sign = -1
        y = int(str(abs(x))[::-1])
        if y > 2 ** 31 - 1:
            return 0
        else:
            return sign * y

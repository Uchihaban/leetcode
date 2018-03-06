#题目：判断是否是回文数，并且不占用不能使用额外空间
#思路：第一想法是使用切片，核心代码一步解决，一分钟解决，太爽了～
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if str(x)[::1] == str(x)[::-1]:
            return True
        return False

#但是仔细看看，不占用额外空间是什么鬼，（em...）
# 也就是不能通过将数字转为字符串来判断回文，因为使用了额外的空间（即只能使用空间复杂度 O(1) 的方法）
#只能反转了～

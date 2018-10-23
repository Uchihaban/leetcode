#题目：给定一个String类型数组，要求写一个方法，返回数组中这些字符串的最长公共前缀。举个例子：假如数组为["123","12","4"]，经过这个方法返回的结果就应该是""。因为"123"，"12"，"4"并没有共同的前缀，虽然"123"，"12"的公共最长前缀是"12"，但是这个公共前缀"12"与"4"没有公共前缀，所以最后返回的结果就是""。

#第一想法肯定是将str[0]，当作临时最长公共前缀，然后用这个前缀依次和剩下的字符串进行前缀比较，都比较完后，就将最后得到的最新公共最长前缀返回。
#但是这要多加一个循环判断长度，或者一个一个比，好恶心～
#所以我在判断数组不为空之后，首先就做一个字符串数组排序，这样只需要判断第一个和最后一个是否有公共的前缀，太爽了～


class Solution:

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #判断字符串列表是否为空，如果为空，则输出""
        if len(strs) == 0:
            return ""
        else:
            strs2 = sorted(strs) #对数组排序
            length = len(strs2)
            l1 = strs2[0]
            l2 = strs2[length-1]

            prefix = l1
            for i in range(len(l1)):
                if l1[i] != l2[i]:
                    prefix = prefix[0:i]
                    break
            return prefix

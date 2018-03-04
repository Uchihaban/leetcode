
# -*- coding: UTF-8 -*-
# 问题：给你一个整型数组，要你返回两个数的索引使得它们代表的数组中的数相加等于一个给定的目标数字
#     每次输入只会有一个正确结果，同一个数不会用到两次

# 思路：最简单的方法就是穷举,以数组的长度为标准

class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]

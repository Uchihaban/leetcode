
# -*- coding: UTF-8 -*-
# 问题：给一个整数数组，找到两个数使得他们的和等于一个给定的数 target。
#      你需要实现的函数twoSum需要返回这两个数的下标
#      每次输入只会有一个正确结果，同一个数不会用到两次

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
        #无解的情况
        return [-1, -1]

#反思：采用暴力解法，两边循环，复杂度极高。需要注意无解的情况，以及第一个下标小于第二个下标。
#     注意这里下标的范围是 0 到 n-1
#缺点：时间复杂度为o(n^2)

#双指针：时间复杂度为o(n*logn)

#较优解法：使用哈希表，时间复杂度为o(n)
class Solution(object):
    def twoSum(self, nums, target):
        #hash用于建立数值到下标的映射
        hash = {}
        #循环nums数值，并添加映射
        for i in range(len(nums)):
            if target - nums[i] in hash:
                return [hash[target - nums[i]], i]
            hash[nums[i]] = i
        #无解的情况
        return [-1, -1]

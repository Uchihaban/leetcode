class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''罗马数字是阿拉伯数字传入之前使用的一种数码。罗马数字采用七个罗马字母作数字、即Ⅰ（1）、X（10）、C（100）、               M（1000）、V（5）、L（50）、D（500）。记数的方法：
         （1）相同的数字连写，所表示的数等于这些数字相加得到的数，如 Ⅲ=3；
         （2）小的数字在大的数字的右边，所表示的数等于这些数字相加得到的数，如 Ⅷ=8、Ⅻ=12。
         （3）小的数字（限于 Ⅰ、X 和 C）在大的数字的左边，所表示的数等于大数减小数得到的数，如 Ⅳ=4、Ⅸ=9； 
         （4）在一个数的上面画一条横线，表示这个数增值 1,000 倍。
         '''
        numerals = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        sum = 0
        s = s[::-1]
        last = None
        for x in s:
            if last and numerals[x] < last:
                sum -= 2 * numerals[x]
            sum += numerals[x]
            last = numerals[x]
        return sum



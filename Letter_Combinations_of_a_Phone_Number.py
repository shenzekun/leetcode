"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

图片：https://ws4.sinaimg.cn/large/006tNbRwly1fx8h9i5jjrj305k04i3ye.jpg

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


思路：
使用 map 做一层 num - letter 的映射，然后每次取出digits的第一个，s用来记录结果，每次从digits里面去一个，然后寻找其可能的char，加到s中，digits长度减小
digits长度为0时候，把它加入结果
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']
               }
        result = []

        def helper(s, digits):
            if len(digits) == 0:  # 如果digits的长度为0
                result.append(s)
            else:
                cur_digit = digits[0]
                for char in dic[cur_digit]:
                    helper(s + char, digits[1:])

        if not digits or len(digits) == 0:
            return result
        helper('', digits)
        return result

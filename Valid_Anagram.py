""" 
题目：给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？


解决方法：
① 第一种方法就是对字符串进行按 ascii 排序，如果相等就返回 true，否则返回 false，时间复杂度 O(nlogn)
② 第二种就是使用 hashmap，遇到相同单词就加一，最终比较二个map，如果相等就返回 true，否则返回 false，时间复杂度
O(n)
"""
# 方法一
class Solution1(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(t) == sorted(s)

# 方法二
class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1,dict2 = {},{}
        for item in s:
            dict1[item] = dict1.get(item,0) + 1
        for item in t:
            dict2[item] = dict2.get(item,0) + 1
        return dict1 == dict2
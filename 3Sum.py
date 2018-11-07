"""
题目：给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]


思路：
① 两层循环，然后把数放到 set 里面去，看 -a-b 有在 set 吗？如果有就有解，注意要判重
② 先排序，然后再查找,比如[1,2,3,4,-1,0]，排完序之后[-1,0,1,2,3,4],
如何循环一层，[-1,(0,1,2,3,4)],设置一个左值 b和一个右值c，当 a+b+c>0,右值往左走，
当 a+b+c<0 说明b 太小，b 往右走，直至 b与 c 相遇，时间复杂度 O（n^2）
"""

# 方法一
class Solution1(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i,v in enumerate(nums[:-1]):
            if i>=1 and v == nums[i-1]: # 判重
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v,-v-x,x))
        return map(list,res)


# 方法二
class Solution2(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        res = []
        nums.sort()
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i-1]: # 判重
                continue
            l,r = i+1,len(nums) -1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s<0:
                    l += 1
                else:
                    res.append((nums[i],nums[l],nums[r]))
                    while l < r and nums[l] == nums[l+1]: # 判重
                        l+=1
                    while l < r and nums[r] == nums[r-1]: # 判重
                        r-=1
                    l+=1;r-=1
                    
        return res
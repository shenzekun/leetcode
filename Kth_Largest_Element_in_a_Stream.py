""" 
题目：设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。

你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用 KthLargest.add，返回当前数据流中第K大的元素。

示例:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
说明: 
你可以假设 nums 的长度≥ k-1 且k ≥ 1。


解题思路：使用最小堆，k 个元素，一旦遇到比堆顶大的元素就 pop 掉堆顶元素，
加入元素，然后重新构建堆，直到所有元素遍历完成，余留的就是最大的 k 个元素，堆顶就是
第 k 大元素
"""

import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap = nums
        self.size = len(self.heap)
        self.k = k
        heapq.heapify(self.heap)
        while self.size > k:
            heapq.heappop(self.heap)
            self.size -= 1
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.size < self.k:
            heapq.heappush(self.heap, val)
            self.size += 1
        elif self.heap[0] < val:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
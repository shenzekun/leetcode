"""
题目：使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空
注意:

你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。


解题思路：使用两个队列来模拟，一个队列用来进栈和出栈，另外一个用来做中转，当 push 的时候，
将元素 push 到用来进栈和出栈的队列，当 pop 的时候，先让用来进栈和出栈的队列循环 push 到中转的
队列中，当push到最后一个，将这个 pop 出去，同时，两个队列对换就可以了
"""

from Queue import Queue
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input_output_queue = Queue()
        self.transfer = Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.input_output_queue.put(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while self.input_output_queue.qsize() > 1:
            self.transfer.put(self.input_output_queue.get())
        res = self.input_output_queue.get()
        self.input_output_queue,self.transfer = self.transfer,self.input_output_queue
        return res
    
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        while self.input_output_queue.qsize() > 1:
            self.transfer.put(self.input_output_queue.get())
        res = self.input_output_queue.get()
        self.transfer.put(res)
        self.input_output_queue,self.transfer = self.transfer,self.input_output_queue
        return res

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not bool(self.input_output_queue.qsize() + self.transfer.qsize())


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
#! 给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
from typing import List


class Solution:
    """这里涉及到两个点, 一是k值大于数组长度，此时相当于轮转了len(nums)次+(k-len(nums))次
        用一个简单的表达就是相当于轮转了k % len(nums)次
        二是海象表达式 :=
        海象表达式是为了减少赋值次数，使得语法更简单的
        if n := (len(nums) % k) 表示n直接就拿到了后面表达式的值，而不需要先赋值变量再if
    """

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k := (k % len(nums)):
            nums[:] = nums[-k:] + nums[:-k]

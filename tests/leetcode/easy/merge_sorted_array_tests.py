#!/usr/bin/env python3
# https://leetcode.com/problems/merge-sorted-array/

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return
        if m == 0:
            nums1[:] = nums2

        i = 0
        j = 0
        while i < m + n:
            if i == m + j:
                nums1[i:] = nums2
                break
            if not nums2:
                break
            if nums1[i] < nums2[0]:
                i += 1
            else:
                nums1.insert(i, nums2[0])
                nums2.pop(0)
                j += 1

def test_merge1():
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    expected = [1,2,2,3,5,6]
    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    assert nums1[:m+n] == expected

def test_merge2():
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    expected = [1]
    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    assert nums1[:m+n] == expected

def test_merge3():
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    expected = [1]
    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    assert nums1[:m+n] == expected

def test_merge4():
    nums1 = [2,0]
    m = 1
    nums2 = [1]
    n = 1
    expected = [1,2]
    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    assert nums1[:m+n][:m+n] == expected
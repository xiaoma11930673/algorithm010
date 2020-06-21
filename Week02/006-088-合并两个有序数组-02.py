class Solution:
    def merge(self, nums1, m: int, nums2, n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1.extend(nums2)
        nums1.sort()
        for i in range(n):
            nums1.remove(0)
        return nums1
nums1 = [1, 2, 3, 4, 5, 0, 0, 0, 0]
m = 5
nums2 = [1, 3, 5, 6]
n = 4
t1 = Solution()
newnums1 = t1.merge(nums1, m, nums2, n)
print(newnums1)
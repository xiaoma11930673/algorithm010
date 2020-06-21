class Solution:
    def merge(self, nums1, m: int, nums2, n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 这个方法很棒，通过反向的方向把 nums2 插入到 nums1中
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
        # 这里很灵性，只可意会
        nums1[:j + 1] = nums2[:j + 1]
        return  nums1

nums1 = [1, 2, 3, 4, 5, 0, 0, 0, 0]
m = 5
nums2 = [1, 3, 5, 6]
n = 4
t1 = Solution()
newnums1 = t1.merge(nums1, m, nums2, n)
print(newnums1)




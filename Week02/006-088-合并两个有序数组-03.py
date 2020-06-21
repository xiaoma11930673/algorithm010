class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while i < m and j < n:
            # 因为每当 num1 中插入一个元素，num1 当多一个元素，如果 i 不加j 那么相当于 i 往前罗了
            if nums1[i + j] <= nums2[j]:
                i += 1
            else:
                nums1.insert(i + j, nums2[j])
                j += 1

        if j < n:
            nums1[i + j:] = nums2[j:]
        if i < m:
            nums1[i + j:] = nums1[i + j: m + j]
        return nums1

nums1 = [1, 2, 3, 4, 5, 0, 0, 0, 0]
m = 5
nums2 = [1, 3, 5, 6]
n = 4
t1 = Solution()
newnums1 = t1.merge(nums1, m, nums2, n)
print(newnums1)
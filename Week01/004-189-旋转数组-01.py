class Solution:
    # 方法一：通过三次旋转实现。首先旋转最后的 k 个元素， 然后再旋转 前面的 n - k 个元素，最后整体旋转
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        def swap(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        swap(n - k, n - 1)
        swap(0, n - k - 1)
        swap(0, n - 1)
        return nums
nums = [1, 2, 3, 4, 5, 6, 7]
k = 5
t1 = Solution()
newNums = t1.rotate(nums, k)
print(newNums)

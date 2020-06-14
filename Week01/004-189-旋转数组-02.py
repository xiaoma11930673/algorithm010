class Solution:
    # 方法二：通过数组的切片实现
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        nums[:] = nums[n - k:] + nums[:n - k]
        return nums

nums = [1, 2, 3, 4, 5, 6, 7]
k = 5
t1 = Solution()
newNums = t1.rotate(nums, k)
print(newNums)



class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        def swap(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        swap(n - k, n - 1)
        swap(0, n - k - 1)
        swap(0, n - 1)
        return nums
nums = [1, 2, 3, 4, 5, 6, 7]
k = 5
t1 = Solution()
newNums = t1.rotate(nums, k)
print(newNums)


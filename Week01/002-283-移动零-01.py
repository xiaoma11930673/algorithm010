class Solution:
    def moveZeroes(self, nums):
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums

nums = [0, 1, 0, 3, 12, 0, 5]
t1 = Solution()
newNums = t1.moveZeroes(nums)
print(newNums)
class Solution:
    def moveZeroes(self, nums):
        countZeroes = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                countZeroes += 1
            elif countZeroes > 0:
                nums[i - countZeroes], nums[i] = nums[i], 0
        return nums

nums = [0, 1, 0, 3, 12, 0, 5]
t1 = Solution()
newNums = t1.moveZeroes(nums)
print(newNums)
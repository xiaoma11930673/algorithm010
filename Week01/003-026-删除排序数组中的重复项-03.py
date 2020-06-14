class Solution:
    def removeDuplicates(self, nums):
        count = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1  # 计算前面重复的次数
            else:
                nums[i - count] = nums[i]
        return len(nums) - count

nums = [1, 1, 2, 2, 2, 2, 6, 7, 8, 8, 9]
t1 = Solution()
index = t1.removeDuplicates(nums)
newNums = nums[:index]
print(newNums)

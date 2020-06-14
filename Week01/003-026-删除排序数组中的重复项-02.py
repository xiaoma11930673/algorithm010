class Solution:
    def removeDuplicates(self, nums):
        i  = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1
        return i
# 本质与前一种方法一致，将 nums 中不同的元素放到 nums 的最前面去
nums = [1, 1, 2, 2, 2, 2, 6, 7, 8, 8, 9]
t1 = Solution()
index = t1.removeDuplicates(nums)
newNums = nums[:index]
print(newNums)
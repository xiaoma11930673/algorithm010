class Solution:
    def twoSum(self, nums, target):
        dict1 = {}
        for i in range(len(nums)):
            anotherNum = target - nums[i]
            if anotherNum in dict1:
                return [dict1[anotherNum], i]
            dict1[nums[i]] = i

nums = [0, 2, 4, 7]
target = 9
t1 = Solution()
back = t1.twoSum(nums, target)
print(back)
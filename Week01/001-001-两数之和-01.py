class Solution:
    def twoSum(self, nums, target):
        dict1 = {}
        for index, num in enumerate(nums):
            anotherNum = target - num
            if anotherNum in dict1:
                return [dict1[anotherNum], index]
            dict1[num] = index

nums = [3, 2, 4, 7]
target = 6
t1 = Solution()
back = t1.twoSum(nums, target)
print(back)
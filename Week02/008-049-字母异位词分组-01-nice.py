"""
执行结果：通过
执行用时：56 ms, 在所有 Python3 提交中击败了86.31%的用户
内存消耗：16.8 MB, 在所有 Python3 提交中击败了14.29%的用户
"""
class Solution:
    def groupAnagrams(self, strs):
        dict1 = {}
        for i in strs:
            # 对于列表中的字符串进行排序，然后再将排序好的列表转换成元组，转换成元组的目的是，字典中的key值，不能是列表
            key = tuple(sorted(i))
            # 这一步个人感觉很灵性，可认真体会一下
            dict1[key] = [i] + dict1.get(key, [])
        return list(dict1.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
t1 = Solution()
list1 = t1.groupAnagrams(strs)
print(list1)

"""
执行结果：通过
执行用时：48 ms, 在所有 Python3 提交中击败了98.26%的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了14.29%的用户
"""
class Solution:
    def groupAnagrams(self, strs):
        dict1 = {}
        for i in strs:
            #key = "".join(sorted(i))
            key = tuple(sorted(i))
            if key not in dict1:
                dict1[key] = [i]
            else:
                dict1[key].append(i)
        return list(dict1.values())
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
t1 = Solution()
list1 = t1.groupAnagrams(strs)
print(list1)
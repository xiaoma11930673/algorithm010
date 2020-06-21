"""
执行结果：通过
执行用时：48 ms, 在所有 Python3 提交中击败了91.01%的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了8.33%的用户
"""
class Solution:
    def isAnagram(self, s, t):
        # 1. 首先判断字符串 s 和 t 是否都为空，如果都为空的话，直接返回 True
        if not s and not t:
            return True
        # 2. 然后判断长度是否相等，如果不相等的话，直接返回 False
        if len(s) != len(t):
            return False
        else:
            for i in set(s):
                # 3. 判断在 s 中出现元素的次数，与在 t 中出现的次数是否相等，一有不相等的情况出现，直接返回False
                if s.count(i) != t.count(i):
                    return False
            return True

s = "a"
t = "b"
t1 = Solution()
result = t1.isAnagram(s, t)
print(result)

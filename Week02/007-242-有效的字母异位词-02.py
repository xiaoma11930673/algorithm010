"""
执行结果：通过
执行用时：52 ms, 在所有 Python3 提交中击败了85.08%的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了8.33%的用户
"""
class Solution:
    def isAnagram(self, s, t):
        dict1 = {}
        dict2 = {}
        if not s and not t:
            return True
        if len(s) != len(t):
            return False
        # 用一个字典记录 s 中元素出现的次数
        for i in s:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        # 用一个字典记录 t 中元素出现的次数
        for j in t:
            if t in dict2:
                dict2[j] += 1
            else:
                dict2[j] = 1
        # 判断两个字典是否一样
        if dict1 == dict2:
            return True
        else:
            return False
s = "a"
t = "b"
t1 = Solution()
result = t1.isAnagram(s, t)
print(result)
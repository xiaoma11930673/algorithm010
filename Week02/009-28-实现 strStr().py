"""
执行结果：通过
执行用时：40 ms, 在所有 Python3 提交中击败了78.21%的用户
内存消耗：13.4 MB, 在所有 Python3 提交中击败了6.67%的用户
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n1 = len(haystack)
        n2 = len(needle)
        if n2 == 0:
            return 0
        for i in range(n1 - n2 + 1):
            if haystack[i: i + n2] == needle:
                return i
        return -1

haystack = "hello"
needle = "lo"
t1 = Solution()
result = t1.strStr(haystack, needle)
print(result)
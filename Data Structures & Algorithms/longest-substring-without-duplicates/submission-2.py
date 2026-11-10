class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = 0
        cache = set()

        for right in range(len(s)):
            while s[right] in cache:
                cache.remove(s[left])
                left += 1
            cache.add(s[right])
            res = max(res, right - left + 1)

        return res
        
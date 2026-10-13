def lengthOfLongestSubstring(s):
    left = 0
    best = 0
    seen = set()
    for i in range(len(s)):
        while s[i]  in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[i])

        if (i - left + 1) > best:
            best = i  - left + 1

    return best

print(lengthOfLongestSubstring("abcabcbb"))  # 3
print(lengthOfLongestSubstring("bbbbb"))  # 1
print(lengthOfLongestSubstring("pwwkew"))  # 3
print(lengthOfLongestSubstring("dvdf"))  # 3
print(lengthOfLongestSubstring(""))  # 0
# LeetCode 424 - Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/
# Time: O(n) | Space: O(1)   (at most 26 letters)
# Approach: sliding window; valid when length − most frequent count ≤ k.

def characterReplacement(s, k):
    left = 0
    counts = {}
    max_freq = 0
    best = 0

    for right in range(len(s)):
        if s[right] in counts:
            counts[s[right]] += 1
        else:
            counts[s[right]] = 1

        max_freq = max(counts.values())

        while (right - left + 1) - max_freq > k:
            counts[s[left]] -= 1
            left += 1
            max_freq = max(counts.values())

        if (right - left + 1) > best:
            best = (right - left + 1)

    return best

print(characterReplacement("ABAB", 2))      # 4
print(characterReplacement("AABABBA", 1))   # 4
# LeetCode 49 - Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# Time: O(n·k) | Space: O(n·k)   (n words, k letters each)
# Approach: build each word's letter-count, turn it into a tuple key,
# group words with the same key in a dict.

def group_anagrams(strs):
    groups = {}

    for word in strs:
        char_freq = {}

        for char in word:
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1

        key = tuple(sorted(char_freq.items()))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())


print(group_anagrams(["act", "pots", "tops", "cat", "stop", "hat"]))



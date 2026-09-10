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


# # LeetCode 242_valid_anagram
# # https://neetcode.io/problems/is-anagram/question?list=neetcode150
# # Time: O(n) | Space: O(n)
# # Approach: walk the word.keep count of freq in dict, compare
# # if dict does'nt match False.
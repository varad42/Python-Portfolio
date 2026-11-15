def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    freq_s1 = {}
    k = len(s1)
    for i in s1:
        if i in freq_s1:
            freq_s1[i] += 1
        else:
            freq_s1[i] = 1
    freq_s2 = {}

    for b in range(len(s1)):
        if s2[b] in freq_s2:
            freq_s2[s2[b]] += 1
        else:
            freq_s2[s2[b]] = 1

    if freq_s1 == freq_s2:
        return True

    for right in range(len(s1), len(s2)):
        if s2[right] in freq_s2:
            freq_s2[s2[right]] += 1
        else:
            freq_s2[s2[right]] = 1

        leaving = s2[right - k]
        freq_s2[leaving] -= 1

        if freq_s2[leaving] == 0:
            del freq_s2[leaving]
        if freq_s1 == freq_s2:
            return True
    return False

print(checkInclusion("ab", "eidbaooo"))   # True
print(checkInclusion("ab", "eidboaoo"))   # False
print(checkInclusion("abc", "cbadef"))    # True
print(checkInclusion("abcd", "ab"))       # False
print(checkInclusion("ab", "ab"))         # True
print(checkInclusion("aa", "aab"))        # True
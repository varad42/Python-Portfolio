def checkInclusion(s1, s2):
    freq_s1 = {}
    freq_s2 = {}
    for i in s1:
        if i in freq_s1:
            freq_s1[i] += 1
        else:
            freq_s1[i] = 1

    for i in range(0,len(s1)) :
        if s2[i] in freq_s2:
            freq_s2[i] += 1
        else:
            freq_s2[i] = 1
    return freq_s2




print(checkInclusion("ab", "eidbaooo"))  # True
print(checkInclusion("ab", "eidboaoo"))  # False
print(checkInclusion("abc", "cbadef"))  # True
print(checkInclusion("abcd", "ab"))  # False
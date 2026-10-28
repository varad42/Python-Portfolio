# Define function
def checkInclusion(s1, s2):
    # Define dictionary to store the freq of strings
    freq_s1 = {}
    freq_s2 = {}
    k = len(s1)
    # return false if both s1 > s2
    if len(s1) > len(s2):
        return False
    # Loop through s1
    for ch in s1:
        if ch in freq_s1:
            freq_s1[ch] += 1
        else:
            freq_s1[ch] = 1

    # Loop in range of k
    for i in range(k):
        if s2[i] in freq_s2:
            freq_s2[s2[i]] += 1
        else:
            freq_s2[s2[i]] = 1
    # loop through s2
    if freq_s1 == freq_s2:
        return True

    for right in range(len(s1), len(s2)):
        if s2[right] in freq_s2:
            freq_s2[s2[right]] += 1
        else:
            freq_s2[s2[right]] = 1

        leaving = s2[right-k]
        freq_s2[leaving] -= 1

        if freq_s2[leaving] == 0:
            del freq_s2[leaving]

        if freq_s1 == freq_s2:
            return True
    return False


print(checkInclusion("ab", "eidbaooo"))  # True
print(checkInclusion("ab", "eidboaoo"))  # False
print(checkInclusion("abc", "cbadef"))  # True
print(checkInclusion("abcd", "ab"))  # False
def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False

    return True

# Example test
print(isAnagram("anagram", "nagaram"))  # Expected output: True
print(isAnagram("rat", "car"))          # Expected output: False    

# Cheat method

def isAnagramCounter (s, t):
    return Counter(s) == Counter(t)


# Sort method

def isAnagramSort (s, t):
    return sorted(s) == sorted(t)

## If interviewer asks how can you make it O(1) - for this you can use a sorting algorithm and check if the sorted lists are equal. But this isn't actually O(1) - interviewers just assume it is

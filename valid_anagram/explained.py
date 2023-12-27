def isAnagram(s, t):
    if len(s) != len(t):
        print(f"The strings '{s}' and '{t}' are not the same length, so they cannot be anagrams.")
        return False
    
    print(f"Checking if '{s}' and '{t}' are anagrams...")
    countS, countT = {}, {}
    
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
        print(f"After processing character {i+1}:")
        print(f"  countS: {countS}")
        print(f"  countT: {countT}")
    
    for c in countS:
        if countS[c] != countT.get(c, 0):
            print(f"Character '{c}' has {countS[c]} occurrences in '{s}' but {countT.get(c, 0)} occurrences in '{t}'.")
            print("The strings are not anagrams.")
            return False
    
    print("The strings are anagrams.")
    return True

# Example test
print(isAnagram("anagram", "nagaram"))  # Expected output: True
# print(isAnagram("rat", "car"))          # Expected output: False

"""
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    

    Example 1:

    Input: s = "anagram", t = "nagaram"
    Output: true

    Example 2:

    Input: s = "rat", t = "car"
    Output: false
"""

def isAnagram(s, t):
    return sorted(s) == sorted(t)


if __name__ == "__main__":
    s = "rat" 
    t = "car"
    print(isAnagram(s, t))
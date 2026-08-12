class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # U: given two strings s and t, we want to find out if
        # the two strings are anagrams of each other
        # if they are True otherwise False

        # P: anagram is a string that contains same characters
        # doesnt have to be in the same order
        # use a key value pair data structure (hashmap) to keep
        # track of letter as key and value is the count
        # if same return True, otherwise False

        if len(s) != len(t):
            return False

        hashmapS = {}
        hashmapT = {}

        # use one loop instead of two loops to check each string
        # check both s[i] and t[i] and collect their letters (key) and 
        # count (value)

        for i in range(len(s)):
            hashmapS[s[i]] = hashmapS.get(s[i], 0) + 1
            hashmapT[t[i]] = hashmapT.get(t[i], 0) + 1

        return hashmapS == hashmapT
#Simple O(n) solution using a hashmap, faster than 80% of all leetcode solutions with 70% better memory utilization.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        #if s is longer than t, than we cannot make an anagram
        if len(s) > len(t):
            return False
        
        #instantiate a hashmap for the chars in s
        sMap = defaultdict(int)
        
        #iterate through the characters in s
        for char in s:
            #increment the value in the hashmap for a given char
            sMap[char] += 1
        
        #interate through the characters in t
        for char in t:
            #decrement the given character's value in t
            sMap[char] -= 1
            #if the value is less than 1, than we have a char in t that was not in s
            #or there were more instances of that char in t than s and thus t is not 
            #an anagram of s
            if sMap[char] < 0:
                return False
        
        #if we have looped through t without returning False, than t must be an anagram of s
        return True
            
        

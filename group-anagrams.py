# O(nlogn) solution, faster than 97% of leetcode solutions with 45% better memory utilization.

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        #instantiate a hashmap for keeping track of the unique anagrams
        hashMap = dict()
        #instantiate a list for the return values
        ret = []
        #instantiate a count at -1, this will keep track of the indicies for the return list
        count = -1
        
        #iterate by index through strings 
        for i in range(len(strs)):
          
            #first, sort the current word alphabetically
            sort = ''.join(sorted(strs[i]))
            #check if the current sorted word is not in the hashmap
            if sort not in hashMap:
                #if not, increment the count
                count += 1
                #set the value of the unique anagram to the count (this saves the index)
                hashMap[sort] = count
                #append the original string (not sorted version) into the return list
                ret.append([strs[i]])
            else:
                #if the anagram is already in the list, find the correct index from the hashmap and 
                #append the original string into the return list
                ret[hashMap[sort]].append(strs[i])
        
        return ret

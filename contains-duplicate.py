#simple O(n) solution using hashmap, 70% faster and better memory utilization than other leetcode answers.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        #instantiate a hashmap of ints
        hashMap = defaultdict(int)
        
        #loop through all the numbers in the array
        for num in nums:
            #if the value is greater than 0 in the hash map, then num has 
            #already appeared and we return True
            if hashMap[num] > 0:
                return True
            else:
                #if the value is 0 then we update it to show that we have 
                #seen the number
                hashMap[num] += 1
        
        #if we pass through the list without returning True, then the list must be unique
        return False
        
        

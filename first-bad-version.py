#Simple binary-search type solution faster than 90% of leetcode solutions with 60% better memory utilization

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #instantiate low and high pointers
        low, high = 0, n
        
        #loop until low crosses high
        while low < high:
            
            #set the mid point based on low and high pointers
            mid = (high + low) // 2
            
            #check if the version behind mid is bad
            if isBadVersion(mid - 1):
                #if so, set the high to that version
                high = mid - 1
                
            #if the version behind mid is not bad and the version at mid is, then the 
            #version at the mid is the first bad version
            elif isBadVersion(mid):
                return mid
            
            #if both the version at mid and the verison before that are good, set low the 
            #next version
            else:
                low = mid + 1
                
        
        return low
                

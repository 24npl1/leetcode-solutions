#Simple binary search, O(logn) time, faster than 80% of all leetcode solutions with 75% memory utilization

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #instantiate left and right pointers for the list
        left = 0
        right = len(nums) - 1
          
        #loop until the left pointer meets or crosses the right pointer
        while left <= right:
            
            #set the central pivot to the center of the list based on the pointers
            pivot = left + (right - left // 2)
            
            #if the pivot is greater than the pivot, set the right pointer to the pivot - 1
            if nums[pivot] > target:
                right = pivot - 1
            #if the pivot is less than the pivot, set the left pointer to the pivot + 1
            elif nums[pivot] < target:
                left = pivot + 1
            #if the pivot = target, return the pivot 
            elif nums[pivot] == target:
                return pivot
        
        #if we loop without returning the pivot, the target does not exist
        return -1
                

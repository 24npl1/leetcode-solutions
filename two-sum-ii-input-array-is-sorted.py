#Simple O(n) solution using two pointers. Faster than 95% of solutions with 70% better memory utilization

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        #instantiate right and left pointers 
        left, right = 0, len(numbers) - 1
        
        #loop until the pointers meet
        while left < right:
            
            #save the temporary sum of the two numbers at the pointers
            twoSum = numbers[left] + numbers[right]
            #if the twoSum is the target, then we return the indicies
            if twoSum == target:
                return [left + 1, right + 1]
            #if the twoSum is less than the target, we increment left
            elif twoSum < target:
                left += 1
            #if the twoSum is greater than the target, we decrement right
            else:
                right -= 1
            
                
        
                
        

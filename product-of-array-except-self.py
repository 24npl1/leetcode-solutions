# O(n) solution 95% faster than other solutions on leetcode with 70% better memory utilization.

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        #instantiate a list of 1's based on the size of nums
        #instantiate a variable to track the suffix product (product of following numbers
        #in a list)
        ret, sufProd = [1] * len(nums), 1
        
        #iterate through the range of nums
        for i in range(1, len(nums)):
            #set the answer at i equal to the product of the previous product 
            #and the current number
            ret[i] = nums[i - 1] * ret[i - 1]
        
        #iterate through the reverse range of nums
        for i in range(len(nums) - 1, -1, -1):
            #set the current answer to the product of the current answer of the suffix product
            ret[i] *= sufProd
            #set the suffix product to the product of the current suffix product
            #and the current number
            sufProd *= nums[i]
        
        return ret
        
        

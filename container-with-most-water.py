class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #instantiate volume (vol) as 0
        vol = 0
        
        #set a left pointer to 0, and a right pointer to the final index in height
        left, right = 0, (len(height) - 1)
        
        #loop until the left pointer reaches the right pointer
        while left < right:
            
            #check which if the two heights is greater
            if height[left] >= height[right]:
                
                #calculate volume by multipying the height of the shorter tower
                #by the width between them (difference in indicies)
                #update the volume if the current volume is greater than the previous
                vol = max(height[right] * (right - left), vol)
        
                #decrement right by 1
                right -= 1
            else:
                
                #use the same strategy as before, this time with the left tower being the 
                #shorter of the two
                vol = max(height[left] * (right - left), vol)
                
                #increment left by 1
                left += 1
                  
        return vol
